-- Bulk seed for additional candidates, jobs, and natural job applications distribution

DO $$
DECLARE
    -- Candidate IDs
    candidate_ids INTEGER[] := ARRAY[]::INTEGER[];
    -- Job IDs
    job_ids INTEGER[] := ARRAY[]::INTEGER[];
    -- For loop variables
    i INTEGER;
    j INTEGER;
    job_count INTEGER;
    candidate_count INTEGER;
    app_count INTEGER;
    jobless_job1_id INTEGER;
    jobless_job2_id INTEGER;
    temp_id INTEGER;
BEGIN
    -- Insert 39 new candidates (to reach ~50 total)
    FOR i IN 1..39 LOOP
        INSERT INTO candidates (name, current_location, summary)
        VALUES (
            'Candidate ' || i + 11,
            'City ' || i,
            'Generated candidate profile for testing bulk allocation.'
        ) RETURNING id INTO temp_id;
        candidate_ids := array_append(candidate_ids, temp_id);
    END LOOP;

    -- Insert 2 new jobs with no candidates
    INSERT INTO jobs (title, description, created_at)
    VALUES ('Blockchain Engineer', 'Work on distributed ledger technologies and smart contracts.', '2025-04-20T10:00:00')
    RETURNING id INTO jobless_job1_id;
    INSERT INTO jobs (title, description, created_at)
    VALUES ('AI Prompt Engineer', 'Design and optimize prompts for generative AI systems.', '2025-04-22T11:00:00')
    RETURNING id INTO jobless_job2_id;

    -- Get all job IDs (excluding the two new jobless jobs)
    SELECT id FROM jobs WHERE title NOT IN ('Blockchain Engineer', 'AI Prompt Engineer') INTO job_ids;
    job_count := array_length(job_ids, 1);
    candidate_count := array_length(candidate_ids, 1);
    app_count := 0;

    -- Allocate ~80% of new candidates to jobs, unevenly
    FOR i IN 1..candidate_count LOOP
        IF random() < 0.8 THEN
            -- Each candidate applies to 1-3 jobs, but not all jobs get equal numbers
            FOR j IN 1..(1 + (random() * 2)::INTEGER) LOOP
                -- Skew: jobs 1-3 get more, jobs 4-6 get some, jobs 7-8 get few
                IF j = 1 THEN
                    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
                    VALUES (
                        candidate_ids[i], job_ids[(1 + (random() * 2)::INTEGER)], 'Received', '2025-04-25', 'Bulk seeded application.'
                    );
                ELSIF j = 2 THEN
                    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
                    VALUES (
                        candidate_ids[i], job_ids[(3 + (random() * 2)::INTEGER)], 'Received', '2025-04-25', 'Bulk seeded application.'
                    );
                ELSE
                    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
                    VALUES (
                        candidate_ids[i], job_ids[(5 + (random() * 2)::INTEGER)], 'Received', '2025-04-25', 'Bulk seeded application.'
                    );
                END IF;
                app_count := app_count + 1;
            END LOOP;
        END IF;
    END LOOP;
END $$;