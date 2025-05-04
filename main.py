from typing import Any, Dict, List
import httpx
from mcp.server.fastmcp import FastMCP

from pgdb import execute_query, fetch_all

mcp = FastMCP("PageDown ATS", "0.1.0")


@mcp.tool()
def hello_world(name: str) -> str:
    """
    A simple hello world tool that returns a greeting message.
    """
    return f"Hello, {name}!"


@mcp.tool()
def goodbye_world(name: str) -> str:
    """
    A simple goodbye world tool that returns a farewell message.
    """
    return f"Goodbye, {name}!"


@mcp.tool()
def get_all_candidate_names() -> list[str]:
    """
    Fetches all candidate names from the database.
    """
    fetch_all_query = "SELECT name FROM candidates"
    try:
        results = fetch_all(fetch_all_query)
        print("Candidate names:", results)
        return results
    except Exception as e:
        print(f"An error occurred while fetching candidate names: {e}")
        return []


@mcp.tool()
def get_job_application_statuses() -> list[str]:
    """
    Fetches all valid statuses for job applications from the database.
    Returns a list of possible application status values.
    """
    fetch_statuses_query = "SELECT enum_range(NULL::application_status);"
    try:
        results = fetch_all(fetch_statuses_query)
        # The query returns a single row with an array of values
        # We need to extract the actual values from the PostgreSQL array
        if results and len(results) > 0:
            # Convert from tuple to a clean list of strings
            statuses = list(results[0][0])
            print("Application statuses:", statuses)
            return statuses
        return []
    except Exception as e:
        print(f"An error occurred while fetching application statuses: {e}")
        return []


@mcp.tool()
def search_candidates_by_name(name: str) -> List[Dict[str, Any]]:
    """
    Searches for candidates by partial or full name and returns matching candidates.

    Args:
        name: Full or partial candidate name to search for

    Returns:
        A list of dictionaries containing candidate id and name
    """
    search_query = "SELECT id, name FROM candidates WHERE name ILIKE %s ORDER BY name"
    try:
        # Use % wildcards for partial name matching
        search_param = f"%{name}%"
        results = fetch_all(search_query, (search_param,))

        # Convert the results to a list of dictionaries
        candidates = []
        for row in results:
            candidates.append({"id": row[0], "name": row[1]})

        print(f"Found {len(candidates)} candidates matching '{name}'")
        return candidates
    except Exception as e:
        print(f"An error occurred while searching candidates by name: {e}")
        return []


@mcp.tool()
def get_candidate_job_applications(candidate_id: int) -> List[Dict[str, Any]]:
    """
    Gets all job applications for a specific candidate, including job details.

    Args:
        candidate_id: ID of the candidate whose applications to retrieve

    Returns:
        A list of dictionaries containing application details including job title and description
    """
    query = """
    SELECT 
        ja.id AS application_id,
        ja.status,
        ja.application_date,
        ja.last_updated,
        ja.notes,
        j.id AS job_id,
        j.title,
        j.description
    FROM job_applications ja
    JOIN jobs j ON ja.job_id = j.id
    WHERE ja.candidate_id = %s
    ORDER BY ja.application_date DESC
    """

    try:
        results = fetch_all(query, (candidate_id,))

        applications = []
        for row in results:
            applications.append(
                {
                    "application_id": row[0],
                    "status": row[1],
                    "application_date": row[2].isoformat() if row[2] else None,
                    "last_updated": row[3].isoformat() if row[3] else None,
                    "notes": row[4],
                    "job_id": row[5],
                    "job_title": row[6],
                    "job_description": row[7],
                }
            )

        print(
            f"Found {len(applications)} job applications for candidate ID {candidate_id}"
        )
        return applications
    except Exception as e:
        print(f"An error occurred while fetching job applications: {e}")
        return []


@mcp.tool()
def get_candidate_details(candidate_id: int) -> Dict[str, Any]:
    """
    Gets comprehensive details about a candidate by ID including personal info,
    skills, education, work experience, and achievements.

    Args:
        candidate_id: ID of the candidate to retrieve details for

    Returns:
        A dictionary containing all available information about the candidate
    """
    try:
        # Get basic candidate information
        candidate_query = """
        SELECT id, name, current_location, summary
        FROM candidates
        WHERE id = %s
        """
        candidate_result = fetch_all(candidate_query, (candidate_id,))

        if not candidate_result:
            print(f"No candidate found with ID {candidate_id}")
            return {"error": f"Candidate with ID {candidate_id} not found"}

        candidate = {
            "id": candidate_result[0][0],
            "name": candidate_result[0][1],
            "current_location": candidate_result[0][2],
            "summary": candidate_result[0][3],
        }

        # Get candidate skills
        skills_query = """
        SELECT s.id, s.name, s.category
        FROM skills s
        JOIN candidate_skills cs ON s.id = cs.skill_id
        WHERE cs.candidate_id = %s
        ORDER BY s.category, s.name
        """
        skills_result = fetch_all(skills_query, (candidate_id,))

        skills = []
        for row in skills_result:
            skills.append({"id": row[0], "name": row[1], "category": row[2]})

        # Get education history
        education_query = """
        SELECT id, institution, degree, field_of_study, start_year, end_year
        FROM education
        WHERE candidate_id = %s
        ORDER BY end_year DESC
        """
        education_result = fetch_all(education_query, (candidate_id,))

        education = []
        for row in education_result:
            education.append(
                {
                    "id": row[0],
                    "institution": row[1],
                    "degree": row[2],
                    "field_of_study": row[3],
                    "start_year": row[4],
                    "end_year": row[5],
                }
            )

        # Get work experience
        work_experience_query = """
        SELECT id, company_name, role, start_date, end_date, is_current, responsibilities
        FROM work_experience
        WHERE candidate_id = %s
        ORDER BY is_current DESC, end_date DESC
        """
        experience_result = fetch_all(work_experience_query, (candidate_id,))

        experience = []
        for row in experience_result:
            experience.append(
                {
                    "id": row[0],
                    "company_name": row[1],
                    "role": row[2],
                    "start_date": row[3].isoformat() if row[3] else None,
                    "end_date": row[4].isoformat() if row[4] else None,
                    "is_current": row[5],
                    "responsibilities": row[6],
                }
            )

        # Get achievements
        achievements_query = """
        SELECT id, description
        FROM achievements
        WHERE candidate_id = %s
        """
        achievements_result = fetch_all(achievements_query, (candidate_id,))

        achievements = []
        for row in achievements_result:
            achievements.append({"id": row[0], "description": row[1]})

        # Compile all information
        candidate_details = {
            "candidate": candidate,
            "skills": skills,
            "education": education,
            "work_experience": experience,
            "achievements": achievements,
        }

        print(f"Retrieved full details for candidate ID {candidate_id}")
        return candidate_details

    except Exception as e:
        print(f"An error occurred while retrieving candidate details: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run("sse")
