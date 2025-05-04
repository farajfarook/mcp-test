-- Schema migration for job applications

-- Create enum type for application status
CREATE TYPE application_status AS ENUM (
    'Received',     -- Application has been submitted
    'Screening',    -- In the screening process
    'Interviews',   -- In the interview process
    'Offer',        -- An offer has been extended or accepted
    'Hired',        -- Candidate has been hired
    'Not Proceeding' -- No longer being considered (rejected or withdrawn)
);

-- Create job applications table
CREATE TABLE IF NOT EXISTS job_applications (
    id SERIAL PRIMARY KEY,
    candidate_id INTEGER NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
    job_id INTEGER NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    status application_status NOT NULL DEFAULT 'Received',
    application_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    UNIQUE(candidate_id, job_id)
);

-- Index for faster lookups by status
CREATE INDEX IF NOT EXISTS idx_job_applications_status ON job_applications(status);

-- Trigger to update last_updated timestamp automatically
CREATE OR REPLACE FUNCTION update_last_updated_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_updated = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_job_application_last_updated
    BEFORE UPDATE ON job_applications
    FOR EACH ROW
    EXECUTE FUNCTION update_last_updated_column();