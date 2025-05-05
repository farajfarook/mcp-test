from mcp.server.fastmcp import FastMCP

from mcp_tools.test_tools import register_test_tools
from mcp_tools.get_all_candidate_names import register_get_all_candidate_names
from mcp_tools.search_candidates_by_name import register_search_candidates_by_name
from mcp_tools.get_candidate_details import register_get_candidate_details
from mcp_tools.get_job_application_statuses import register_get_job_application_statuses
from mcp_tools.get_candidate_job_applications import (
    register_get_candidate_job_applications,
)
from mcp_tools.list_all_jobs import register_list_all_jobs
from mcp_tools.get_job_applications_with_candidates import (
    register_get_job_applications_with_candidates,
)
from mcp_tools.search_jobs_by_title import register_search_jobs_by_title
from mcp_tools.get_job_details import register_get_job_details
from mcp_tools.update_job_application_status import (
    register_update_job_application_status,
)
from mcp_resources.jobs import register_jobs_resource

# Initialize MCP server
mcp = FastMCP("PageDown ATS", "0.1.0")

# Register resources
register_jobs_resource(mcp)
# Register Tools
register_test_tools(mcp)
register_get_all_candidate_names(mcp)
register_search_candidates_by_name(mcp)
register_get_candidate_details(mcp)
register_get_job_application_statuses(mcp)
register_get_candidate_job_applications(mcp)
register_list_all_jobs(mcp)
register_get_job_applications_with_candidates(mcp)
register_search_jobs_by_title(mcp)
register_get_job_details(mcp)
register_update_job_application_status(mcp)

if __name__ == "__main__":
    mcp.run("sse")
