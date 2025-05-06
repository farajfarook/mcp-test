from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_get_job_details(mcp: FastMCP):
    """Register get_job_details tool with the MCP server"""

    @mcp.tool()
    def get_job_details(job_id: int) -> Dict[str, Any]:
        """
        Gets comprehensive details about a job by ID.

        Args:
            job_id: ID of the job to retrieve details for

        Returns:
            A dictionary containing all available information about the job
        """
        try:
            # Get job information
            job_query = """
            SELECT id, title, description, created_at
            FROM jobs
            WHERE id = %s
            """
            job_result = fetch_all(job_query, (job_id,))

            if not job_result:
                print(f"No job found with ID {job_id}")
                return {"error": f"Job with ID {job_id} not found"}

            job = {
                "id": job_result[0][0],
                "title": job_result[0][1],
                "description": job_result[0][2],
                "created_at": (
                    job_result[0][3].isoformat() if job_result[0][3] else None
                ),
            }

            # Get application statistics for this job
            stats_query = """
            SELECT 
                COUNT(*) as total_applications,
                COUNT(CASE WHEN status = 'Received' THEN 1 END) as received,
                COUNT(CASE WHEN status = 'Screening' THEN 1 END) as screening,
                COUNT(CASE WHEN status = 'Interviews' THEN 1 END) as interviews,
                COUNT(CASE WHEN status = 'Offer' THEN 1 END) as offer,
                COUNT(CASE WHEN status = 'Hired' THEN 1 END) as hired,
                COUNT(CASE WHEN status = 'Not Proceeding' THEN 1 END) as not_proceeding
            FROM job_applications
            WHERE job_id = %s
            """
            stats_result = fetch_all(stats_query, (job_id,))

            application_stats = {
                "total_applications": stats_result[0][0],
                "received": stats_result[0][1],
                "screening": stats_result[0][2],
                "interviews": stats_result[0][3],
                "offer": stats_result[0][4],
                "hired": stats_result[0][5],
                "not_proceeding": stats_result[0][6],
            }

            # Compile all information
            job_details = {"job": job, "application_stats": application_stats}

            print(f"Retrieved full details for job ID {job_id}")
            return job_details

        except Exception as e:
            print(f"An error occurred while retrieving job details: {e}")
            return {"error": str(e)}
