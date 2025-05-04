-- Data migration for jobs and job applications

DO $$
DECLARE
    software_eng_id INTEGER;
    data_scientist_id INTEGER;
    product_manager_id INTEGER;
    ux_designer_id INTEGER;
    devops_engineer_id INTEGER;
    security_analyst_id INTEGER;
    project_manager_id INTEGER;
    full_stack_id INTEGER;
    alex_id INTEGER;
    emma_id INTEGER;
    daniel_id INTEGER;
    sophia_id INTEGER;
    nathan_id INTEGER;
    olivia_id INTEGER;
    ethan_id INTEGER;
    maya_id INTEGER;
BEGIN
    -- Get candidate IDs
    SELECT id INTO alex_id FROM candidates WHERE name = 'Alex Thompson';
    SELECT id INTO emma_id FROM candidates WHERE name = 'Emma Collins';
    SELECT id INTO daniel_id FROM candidates WHERE name = 'Daniel Wilson';
    SELECT id INTO sophia_id FROM candidates WHERE name = 'Sophia Garcia';
    SELECT id INTO nathan_id FROM candidates WHERE name = 'Nathan Rodriguez';
    SELECT id INTO olivia_id FROM candidates WHERE name = 'Olivia Martinez';
    SELECT id INTO ethan_id FROM candidates WHERE name = 'Ethan Parker';
    SELECT id INTO maya_id FROM candidates WHERE name = 'Maya Johnson';

    -- Insert Jobs
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('Senior Software Engineer', 'We are looking for a Senior Software Engineer to design, develop and implement high-quality software solutions. The ideal candidate has strong experience with C#, Java, and microservices architecture.', '2025-03-15T09:00:00')
    RETURNING id INTO software_eng_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('Data Scientist', 'Join our data science team to develop machine learning models and predictive analytics solutions. Expertise in Python, SQL, and statistical analysis required.', '2025-03-20T14:30:00')
    RETURNING id INTO data_scientist_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('Product Manager', 'Lead product development initiatives from conception to launch. Strong experience in agile methodologies and stakeholder management required.', '2025-03-22T11:15:00')
    RETURNING id INTO product_manager_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('UX/UI Designer', 'Create intuitive and engaging user experiences for our digital products. Proficiency in design tools and user research methodologies required.', '2025-03-25T10:00:00')
    RETURNING id INTO ux_designer_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('DevOps Engineer', 'Design and implement CI/CD pipelines and infrastructure as code solutions. Experience with cloud platforms and container orchestration necessary.', '2025-03-28T16:45:00')
    RETURNING id INTO devops_engineer_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('Cybersecurity Analyst', 'Protect our systems by implementing security measures and conducting vulnerability assessments. Experience with security frameworks and threat detection required.', '2025-04-02T13:20:00')
    RETURNING id INTO security_analyst_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('Project Manager', 'Oversee the planning and execution of complex technical projects. Certification in project management methodologies preferred.', '2025-04-05T09:30:00')
    RETURNING id INTO project_manager_id;
    
    INSERT INTO jobs (title, description, created_at)
    VALUES 
        ('Full Stack Developer', 'Develop and maintain web applications using modern technologies. Experience with both frontend and backend development required.', '2025-04-10T11:00:00')
    RETURNING id INTO full_stack_id;
    
    -- Insert Job Applications
    -- Alex Thompson applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (alex_id, software_eng_id, 'Interviews', '2025-04-01T10:30:00', 'Strong technical skills, good cultural fit. Scheduled for final interview with CTO.');
    
    -- Emma Collins applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (emma_id, data_scientist_id, 'Offer', '2025-03-25T14:45:00', 'Excellent candidate with strong ML background. Offer extended on April 15.');
    
    -- Daniel Wilson applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (daniel_id, product_manager_id, 'Hired', '2025-03-28T09:15:00', 'Perfect fit for the role. Started on May 1.');
    
    -- Sophia Garcia applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (sophia_id, full_stack_id, 'Screening', '2025-04-12T16:20:00', 'Strong portfolio. Technical assessment sent.');
    
    -- Nathan Rodriguez applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (nathan_id, security_analyst_id, 'Received', '2025-04-20T11:10:00', 'Resume looks promising. Initial review pending.');
    
    -- Olivia Martinez applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (olivia_id, ux_designer_id, 'Interviews', '2025-04-05T13:40:00', 'Impressive portfolio. First interview went well, second scheduled for May 10.');
    
    -- Ethan Parker applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (ethan_id, devops_engineer_id, 'Not Proceeding', '2025-04-02T10:00:00', 'Good technical skills but looking for higher compensation than we can offer.');
    
    -- Maya Johnson applications
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (maya_id, project_manager_id, 'Screening', '2025-04-15T09:30:00', 'Extensive experience in similar roles. Phone screening scheduled.');
    
    -- Additional applications (candidates applying for multiple positions)
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (alex_id, devops_engineer_id, 'Received', '2025-04-18T14:25:00', 'Interested in transition to DevOps role. Has some relevant experience.');
    
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (emma_id, software_eng_id, 'Not Proceeding', '2025-03-30T11:20:00', 'Strong candidate but more specialized in data science than general software engineering.');
    
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (sophia_id, ux_designer_id, 'Received', '2025-04-22T15:10:00', 'Has some design experience alongside development skills. Worth considering for hybrid role.');
    
    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes)
    VALUES 
        (nathan_id, devops_engineer_id, 'Screening', '2025-04-10T09:45:00', 'Security background with some DevOps experience. Technical assessment sent.');
END $$;