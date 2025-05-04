from typing import Any, Dict, List
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_get_job_applications_with_candidates(mcp: FastMCP):
    """Register get_job_applications_with_candidates tool with the MCP server"""

    @mcp.tool()
    def get_job_applications_with_candidates(job_id: int) -> List[Dict[str, Any]]:
        """
        Gets all applications for a specific job, including candidate details.

        Args:
            job_id: ID of the job to retrieve applications for

        Returns:
            A list of dictionaries containing application details with candidate name and information
        """
        query = """
        SELECT 
            ja.id AS application_id,
            ja.status,
            ja.application_date,
            ja.last_updated,
            ja.notes,
            c.id AS candidate_id,
            c.name AS candidate_name,
            c.current_location,
            c.summary
        FROM job_applications ja
        JOIN candidates c ON ja.candidate_id = c.id
        WHERE ja.job_id = %s
        ORDER BY ja.application_date DESC
        """

        try:
            results = fetch_all(query, (job_id,))

            applications = []
            for row in results:
                applications.append(
                    {
                        "application_id": row[0],
                        "status": row[1],
                        "application_date": row[2].isoformat() if row[2] else None,
                        "last_updated": row[3].isoformat() if row[3] else None,
                        "notes": row[4],
                        "candidate": {
                            "id": row[5],
                            "name": row[6],
                            "location": row[7],
                            "summary": row[8],
                        },
                    }
                )

            print(f"Found {len(applications)} applications for job ID {job_id}")
            return applications
        except Exception as e:
            print(f"An error occurred while fetching job applications: {e}")
            return []
