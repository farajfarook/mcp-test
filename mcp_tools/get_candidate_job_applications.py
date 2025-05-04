from typing import Any, Dict, List
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_get_candidate_job_applications(mcp: FastMCP):
    """Register get_candidate_job_applications tool with the MCP server"""

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
