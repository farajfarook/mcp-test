# PageDown ATS

PageDown ATS is an Applicant Tracking System that uses Model Context Protocol (MCP) to provide a suite of tools for managing candidates, jobs, and job applications. This system helps streamline the recruitment process by providing tools to search candidates, track applications, and manage job postings.

## Overview

The application provides an API through MCP (Model Context Protocol) and connects to a PostgreSQL database to store and retrieve candidate and job information. It allows users to:

- Search for candidates by name
- View detailed candidate profiles including skills, education, work experience, and achievements
- List all available jobs
- Search for jobs by title
- View job applications with candidate details
- Update application statuses (Received, Screening, Interviews, Offer, Hired, Not Proceeding)
- And more

## Installation and Setup

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (for running PostgreSQL database)

### Setup Instructions

1. **Clone the repository**

2. **Set up the database**

   Navigate to the postgres directory and start the database:

   ```bash
   cd postgres
   docker-compose up -d
   ```

   This will start:

   - PostgreSQL database on port 5432
   - pgAdmin interface on port 5050 (accessible at http://localhost:5050)
     - Login: admin@admin.com
     - Password: admin

   The database will be automatically populated with sample data from the migrations folder.

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install dependencies from pyproject.toml:

   ```bash
   pip install -e .
   ```

## Running the Application

Start the MCP server:

```bash
python main.py
```

The server runs in SSE (Server-Sent Events) mode and provides access to all the registered tools.

## Project Structure

- `main.py` - The main entry point that initializes the MCP server
- `pgdb.py` - Database utilities for connecting to and querying PostgreSQL
- `mcp_tools/` - Directory containing all the MCP tools
  - `test_tools.py` - Basic demo tools
  - `get_all_candidate_names.py` - Fetches all candidate names
  - `search_candidates_by_name.py` - Searches candidates by name
  - `get_candidate_details.py` - Gets detailed candidate information
  - `get_job_application_statuses.py` - Fetches all valid application statuses
  - `get_candidate_job_applications.py` - Gets all applications for a candidate
  - `list_all_jobs.py` - Lists all available jobs
  - `get_job_applications_with_candidates.py` - Gets applications with candidate details
  - `search_jobs_by_title.py` - Searches jobs by title
  - `get_job_details.py` - Gets detailed job information
  - `update_job_application_status.py` - Updates application status
- `postgres/` - PostgreSQL Docker setup and migrations
  - `docker-compose.yml` - Docker configuration
  - `migrations/` - Database migration scripts
    - Schema creation and data seeding scripts

## Database Schema

The PostgreSQL database includes the following tables:

- `candidates` - Stores information about job candidates
- `work_experience` - Stores candidates' work history
- `education` - Stores candidates' educational background
- `skills` - Stores available skills
- `candidate_skills` - Junction table linking candidates to their skills
- `achievements` - Stores candidates' achievements
- `jobs` - Stores information about job postings
- `job_applications` - Stores candidate applications for jobs

## Tools API Reference

The following tools are available:

- `hello_world(name)`, `goodbye_world(name)` - Test tools
- `get_all_candidate_names()` - Returns a list of all candidate names
- `search_candidates_by_name(name)` - Searches for candidates by name
- `get_candidate_details(candidate_id)` - Gets detailed info about a candidate
- `get_job_application_statuses()` - Returns all valid application statuses
- `get_candidate_job_applications(candidate_id)` - Gets job applications for a candidate
- `list_all_jobs()` - Lists all job postings
- `get_job_applications_with_candidates(job_id)` - Gets applications for a job
- `search_jobs_by_title(title)` - Searches jobs by title
- `get_job_details(job_id)` - Gets detailed job information
- `update_job_application_status(application_id, new_status)` - Updates an application status

## License

This project is proprietary software and is not licensed for redistribution.
