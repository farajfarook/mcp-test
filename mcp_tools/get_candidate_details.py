from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_get_candidate_details(mcp: FastMCP):
    """Register get_candidate_details tool with the MCP server"""

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
