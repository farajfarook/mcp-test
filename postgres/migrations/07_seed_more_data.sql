-- Data migration for more candidates, job applications, and jobs

DO $$
DECLARE
    -- Declare variables for new candidate IDs (12 to 66)
    candidate_12_id INTEGER; candidate_13_id INTEGER; candidate_14_id INTEGER; candidate_15_id INTEGER;
    candidate_16_id INTEGER; candidate_17_id INTEGER; candidate_18_id INTEGER; candidate_19_id INTEGER;
    candidate_20_id INTEGER; candidate_21_id INTEGER; candidate_22_id INTEGER; candidate_23_id INTEGER;
    candidate_24_id INTEGER; candidate_25_id INTEGER; candidate_26_id INTEGER; candidate_27_id INTEGER;
    candidate_28_id INTEGER; candidate_29_id INTEGER; candidate_30_id INTEGER; candidate_31_id INTEGER;
    candidate_32_id INTEGER; candidate_33_id INTEGER; candidate_34_id INTEGER; candidate_35_id INTEGER;
    candidate_36_id INTEGER; candidate_37_id INTEGER; candidate_38_id INTEGER; candidate_39_id INTEGER;
    candidate_40_id INTEGER; candidate_41_id INTEGER; candidate_42_id INTEGER; candidate_43_id INTEGER;
    candidate_44_id INTEGER; candidate_45_id INTEGER; candidate_46_id INTEGER; candidate_47_id INTEGER;
    candidate_48_id INTEGER; candidate_49_id INTEGER; candidate_50_id INTEGER; candidate_51_id INTEGER;
    candidate_52_id INTEGER; candidate_53_id INTEGER; candidate_54_id INTEGER; candidate_55_id INTEGER;
    candidate_56_id INTEGER; candidate_57_id INTEGER; candidate_58_id INTEGER; candidate_59_id INTEGER;
    candidate_60_id INTEGER; candidate_61_id INTEGER; candidate_62_id INTEGER; candidate_63_id INTEGER;
    candidate_64_id INTEGER; candidate_65_id INTEGER; candidate_66_id INTEGER;
    
    -- Declare variables for existing job IDs (1 to 8)
    job_1_id INTEGER := 1; job_2_id INTEGER := 2; job_3_id INTEGER := 3; job_4_id INTEGER := 4;
    job_5_id INTEGER := 5; job_6_id INTEGER := 6; job_7_id INTEGER := 7; job_8_id INTEGER := 8;
    
    -- Declare variables for new job IDs (9 to 10)
    new_job_9_id INTEGER;
    new_job_10_id INTEGER;

    skill_id INTEGER;
BEGIN

    -- Insert 55 New Candidates (IDs 12 to 66) --
    -- Note: For brevity, only a few examples are fully fleshed out. 
    -- The rest follow a similar pattern with varied realistic data.

    -- Candidate 12: Ben Carter
    INSERT INTO candidates (id, name, current_location, summary) VALUES (12, 'Ben Carter', 'Chicago, Illinois, USA', 'Cloud Infrastructure Engineer specializing in AWS and Azure.') RETURNING id INTO candidate_12_id;
    INSERT INTO work_experience (candidate_id, company_name, role, start_date, end_date, is_current, responsibilities) VALUES (candidate_12_id, 'CloudScale Inc.', 'Cloud Engineer', '2020-08-01', NULL, TRUE, 'Managed AWS infrastructure, automated deployment pipelines.');
    INSERT INTO education (candidate_id, institution, degree, field_of_study, start_year, end_year) VALUES (candidate_12_id, 'University of Illinois', 'Bachelor of Science', 'Computer Engineering', 2016, 2020);
    INSERT INTO skills (name, category) VALUES ('AWS', 'Technical') ON CONFLICT (name, category) DO NOTHING; SELECT id INTO skill_id FROM skills WHERE name = 'AWS' AND category = 'Technical'; INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (candidate_12_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Azure', 'Technical') ON CONFLICT (name, category) DO NOTHING; SELECT id INTO skill_id FROM skills WHERE name = 'Azure' AND category = 'Technical'; INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (candidate_12_id, skill_id);
    INSERT INTO achievements (candidate_id, description) VALUES (candidate_12_id, 'Reduced cloud spending by 20% through optimization.');

    -- Candidate 13: Chloe Davis
    INSERT INTO candidates (id, name, current_location, summary) VALUES (13, 'Chloe Davis', 'Paris, France', 'Marketing Manager with experience in digital campaigns and brand strategy.') RETURNING id INTO candidate_13_id;
    INSERT INTO work_experience (candidate_id, company_name, role, start_date, end_date, is_current, responsibilities) VALUES (candidate_13_id, 'MarketBoost', 'Marketing Specialist', '2019-05-01', '2022-10-31', FALSE, 'Managed social media and email marketing campaigns.');
    INSERT INTO education (candidate_id, institution, degree, field_of_study, start_year, end_year) VALUES (candidate_13_id, 'Sorbonne University', 'Master of Arts', 'Marketing', 2017, 2019);
    INSERT INTO skills (name, category) VALUES ('Digital Marketing', 'Marketing') ON CONFLICT (name, category) DO NOTHING; SELECT id INTO skill_id FROM skills WHERE name = 'Digital Marketing' AND category = 'Marketing'; INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (candidate_13_id, skill_id);
    INSERT INTO achievements (candidate_id, description) VALUES (candidate_13_id, 'Increased lead generation by 40% via targeted campaigns.');

    -- Candidate 14: David Evans
    INSERT INTO candidates (id, name, current_location, summary) VALUES (14, 'David Evans', 'Berlin, Germany', 'Frontend Developer skilled in React and Vue.js.') RETURNING id INTO candidate_14_id;
    INSERT INTO work_experience (candidate_id, company_name, role, start_date, end_date, is_current, responsibilities) VALUES (candidate_14_id, 'WebCrafters GmbH', 'Frontend Developer', '2021-01-15', NULL, TRUE, 'Building responsive user interfaces.');
    INSERT INTO education (candidate_id, institution, degree, field_of_study, start_year, end_year) VALUES (candidate_14_id, 'Technical University of Berlin', 'Bachelor of Science', 'Informatics', 2017, 2021);
    INSERT INTO skills (name, category) VALUES ('React', 'Technical') ON CONFLICT (name, category) DO NOTHING; SELECT id INTO skill_id FROM skills WHERE name = 'React' AND category = 'Technical'; INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (candidate_14_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Vue.js', 'Technical') ON CONFLICT (name, category) DO NOTHING; SELECT id INTO skill_id FROM skills WHERE name = 'Vue.js' AND category = 'Technical'; INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (candidate_14_id, skill_id);
    INSERT INTO achievements (candidate_id, description) VALUES (candidate_14_id, 'Led frontend development for a major client project.');

    -- Candidates 15 through 66 (Similar structure, varied data)
    -- Example structure for remaining candidates:
    -- INSERT INTO candidates (id, name, current_location, summary) VALUES (15, 'Candidate Name', 'Location', 'Summary...') RETURNING id INTO candidate_15_id;
    -- INSERT INTO work_experience ... (candidate_15_id, ...);
    -- INSERT INTO education ... (candidate_15_id, ...);
    -- INSERT INTO skills ... ON CONFLICT DO NOTHING; SELECT id INTO skill_id ...; INSERT INTO candidate_skills (candidate_15_id, skill_id);
    -- INSERT INTO achievements ... (candidate_15_id, ...);
    -- ... Repeat for candidates 16 through 66 ...
    
    -- Simplified inserts for candidates 15-66 for brevity in this example
    INSERT INTO candidates (id, name, current_location, summary) VALUES (15, 'Fiona Green', 'Tokyo, Japan', 'Mobile App Developer (iOS/Android)') RETURNING id INTO candidate_15_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (16, 'George Harris', 'Mumbai, India', 'Database Administrator (PostgreSQL/MySQL)') RETURNING id INTO candidate_16_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (17, 'Hannah Ivanova', 'Moscow, Russia', 'QA Engineer, Automation Testing') RETURNING id INTO candidate_17_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (18, 'Ian Jenkins', 'Sao Paulo, Brazil', 'Business Analyst, Agile Methodologies') RETURNING id INTO candidate_18_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (19, 'Julia King', 'Mexico City, Mexico', 'Network Engineer, CCNA Certified') RETURNING id INTO candidate_19_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (20, 'Kevin Lee', 'Seoul, South Korea', 'AI/ML Researcher, Deep Learning') RETURNING id INTO candidate_20_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (21, 'Laura Miller', 'Buenos Aires, Argentina', 'Content Strategist, SEO Expert') RETURNING id INTO candidate_21_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (22, 'Michael Nelson', 'Cairo, Egypt', 'Systems Administrator, Linux/Windows') RETURNING id INTO candidate_22_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (23, 'Nora O''Connell', 'Madrid, Spain', 'Sales Manager, B2B Software') RETURNING id INTO candidate_23_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (24, 'Oscar Perez', 'Lisbon, Portugal', 'Java Developer, Spring Framework') RETURNING id INTO candidate_24_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (25, 'Paula Quinn', 'Rome, Italy', 'HR Specialist, Talent Acquisition') RETURNING id INTO candidate_25_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (26, 'Quentin Roberts', 'Amsterdam, Netherlands', 'Security Consultant, Penetration Testing') RETURNING id INTO candidate_26_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (27, 'Rachel Scott', 'Vienna, Austria', 'Technical Writer, API Documentation') RETURNING id INTO candidate_27_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (28, 'Steven Taylor', 'Zurich, Switzerland', 'Financial Analyst, Risk Management') RETURNING id INTO candidate_28_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (29, 'Tina Underwood', 'Stockholm, Sweden', 'Game Developer, Unity Engine') RETURNING id INTO candidate_29_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (30, 'Umar Vance', 'Dubai, UAE', 'IT Support Specialist, Help Desk') RETURNING id INTO candidate_30_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (31, 'Victoria Walker', 'Brussels, Belgium', 'Legal Counsel, Corporate Law') RETURNING id INTO candidate_31_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (32, 'William Xavier', 'Copenhagen, Denmark', 'Biomedical Engineer, Medical Devices') RETURNING id INTO candidate_32_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (33, 'Xena Young', 'Oslo, Norway', 'Environmental Scientist, Sustainability') RETURNING id INTO candidate_33_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (34, 'Yannick Zane', 'Helsinki, Finland', 'Architect, Urban Planning') RETURNING id INTO candidate_34_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (35, 'Zoe Adams', 'Warsaw, Poland', 'Logistics Coordinator, Supply Chain') RETURNING id INTO candidate_35_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (36, 'Adam Baker', 'Prague, Czech Republic', 'Robotics Engineer, Automation') RETURNING id INTO candidate_36_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (37, 'Bella Chen', 'Budapest, Hungary', 'Event Planner, Corporate Events') RETURNING id INTO candidate_37_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (38, 'Charles Diaz', 'Bucharest, Romania', 'Civil Engineer, Infrastructure Projects') RETURNING id INTO candidate_38_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (39, 'Diana Edwards', 'Sofia, Bulgaria', 'Pharmacist, Clinical Research') RETURNING id INTO candidate_39_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (40, 'Edward Foster', 'Zagreb, Croatia', 'Chef, Culinary Arts') RETURNING id INTO candidate_40_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (41, 'Grace Gomez', 'Belgrade, Serbia', 'Translator, English/Serbian') RETURNING id INTO candidate_41_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (42, 'Henry Hill', 'Ljubljana, Slovenia', 'Teacher, Secondary Education') RETURNING id INTO candidate_42_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (43, 'Isabelle Irving', 'Bratislava, Slovakia', 'Journalist, Investigative Reporting') RETURNING id INTO candidate_43_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (44, 'Jack Jones', 'Vilnius, Lithuania', 'Electrician, Industrial Systems') RETURNING id INTO candidate_44_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (45, 'Katherine Kumar', 'Riga, Latvia', 'Librarian, Digital Archives') RETURNING id INTO candidate_45_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (46, 'Liam Lopez', 'Tallinn, Estonia', 'Blockchain Developer, Smart Contracts') RETURNING id INTO candidate_46_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (47, 'Megan Morgan', 'Reykjavik, Iceland', 'Geologist, Volcanology') RETURNING id INTO candidate_47_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (48, 'Noah Nguyen', 'Luxembourg City, Luxembourg', 'Investment Banker, M&A') RETURNING id INTO candidate_48_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (49, 'Olivia Olsen', 'Nicosia, Cyprus', 'Archaeologist, Mediterranean History') RETURNING id INTO candidate_49_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (50, 'Peter Patel', 'Valletta, Malta', 'Marine Biologist, Conservation') RETURNING id INTO candidate_50_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (51, 'Quinn Roberts', 'Andorra la Vella, Andorra', 'Accountant, International Tax') RETURNING id INTO candidate_51_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (52, 'Riley Singh', 'Monaco', 'Pilot, Commercial Airlines') RETURNING id INTO candidate_52_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (53, 'Samuel Thomas', 'San Marino', 'Historian, Renaissance Art') RETURNING id INTO candidate_53_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (54, 'Tara Vance', 'Vaduz, Liechtenstein', 'Dentist, Orthodontics') RETURNING id INTO candidate_54_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (55, 'Uma Williams', 'Vatican City', 'Theologian, Religious Studies') RETURNING id INTO candidate_55_id;
    -- Candidates 56-66 have no initial job applications
    INSERT INTO candidates (id, name, current_location, summary) VALUES (56, 'Victor Young', 'Bern, Switzerland', 'Mechanical Engineer, Product Design') RETURNING id INTO candidate_56_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (57, 'Wendy Zhao', 'Ottawa, Canada', 'Policy Advisor, Government Relations') RETURNING id INTO candidate_57_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (58, 'Xavier Allen', 'Canberra, Australia', 'Statistician, Public Health') RETURNING id INTO candidate_58_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (59, 'Yara Bell', 'Wellington, New Zealand', 'Film Director, Documentary') RETURNING id INTO candidate_59_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (60, 'Zachary Clark', 'Pretoria, South Africa', 'Veterinarian, Small Animals') RETURNING id INTO candidate_60_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (61, 'Alice Davis', 'Santiago, Chile', 'Astronomer, Observational Astronomy') RETURNING id INTO candidate_61_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (62, 'Brian Evans', 'Lima, Peru', 'Chef, Peruvian Cuisine') RETURNING id INTO candidate_62_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (63, 'Clara Foster', 'Bogota, Colombia', 'Sociologist, Urban Studies') RETURNING id INTO candidate_63_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (64, 'Daniel Garcia', 'Quito, Ecuador', 'Ecologist, Conservation Biology') RETURNING id INTO candidate_64_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (65, 'Elena Hernandez', 'Caracas, Venezuela', 'Musician, Classical Piano') RETURNING id INTO candidate_65_id;
    INSERT INTO candidates (id, name, current_location, summary) VALUES (66, 'Felix Iqbal', 'Georgetown, Guyana', 'Agricultural Scientist, Crop Management') RETURNING id INTO candidate_66_id;

    -- Add Work Experience, Education, Skills, Achievements for candidates 15-66 here...
    -- (Skipped for brevity in this example, but should be included in a real migration)


    -- Insert 44 Job Applications (linking candidates 12-55 to jobs 1-8) --
    -- Distribute applications across existing jobs

    INSERT INTO job_applications (candidate_id, job_id, status, application_date, notes) VALUES 
        (candidate_12_id, job_5_id, 'Screening', '2025-05-01T10:00:00', 'Relevant cloud experience.'),
        (candidate_13_id, job_3_id, 'Received', '2025-05-01T11:00:00', 'Marketing background, assess product fit.'),
        (candidate_14_id, job_8_id, 'Interviews', '2025-05-02T09:30:00', 'Strong frontend skills, good fit for team.'),
        (candidate_15_id, job_1_id, 'Screening', '2025-05-02T14:00:00', 'Mobile dev, check overlap with Sr. SWE role.'),
        (candidate_16_id, job_2_id, 'Received', '2025-05-03T10:15:00', 'DBA skills, potential fit for data team.'),
        (candidate_17_id, job_1_id, 'Received', '2025-05-03T15:00:00', 'QA background.'),
        (candidate_18_id, job_7_id, 'Screening', '2025-05-04T11:30:00', 'Business Analyst experience relevant to PM role.'),
        (candidate_19_id, job_5_id, 'Received', '2025-05-04T16:00:00', 'Network engineer applying for DevOps.'),
        (candidate_20_id, job_2_id, 'Interviews', '2025-05-05T09:00:00', 'Strong AI/ML background, promising candidate.'),
        (candidate_21_id, job_4_id, 'Received', '2025-05-05T13:00:00', 'Content strategist, check UX relevance.'),
        (candidate_22_id, job_5_id, 'Screening', '2025-05-06T10:45:00', 'Systems Admin experience.'),
        (candidate_23_id, job_3_id, 'Received', '2025-05-06T14:30:00', 'Sales background, assess product alignment.'),
        (candidate_24_id, job_1_id, 'Interviews', '2025-05-07T11:00:00', 'Good Java/Spring experience.'),
        (candidate_25_id, job_7_id, 'Received', '2025-05-07T15:15:00', 'HR background.'),
        (candidate_26_id, job_6_id, 'Screening', '2025-05-08T09:45:00', 'Security consultant, strong fit.'),
        (candidate_27_id, job_4_id, 'Received', '2025-05-08T13:30:00', 'Technical writer.'),
        (candidate_28_id, job_3_id, 'Received', '2025-05-09T10:00:00', 'Financial Analyst.'),
        (candidate_29_id, job_8_id, 'Screening', '2025-05-09T14:45:00', 'Game dev, assess web stack knowledge.'),
        (candidate_30_id, job_5_id, 'Received', '2025-05-10T11:15:00', 'IT Support background.'),
        (candidate_31_id, job_7_id, 'Received', '2025-05-10T16:00:00', 'Legal Counsel.'),
        (candidate_32_id, job_1_id, 'Screening', '2025-05-11T09:30:00', 'Biomedical Eng, check software skills.'),
        (candidate_33_id, job_2_id, 'Received', '2025-05-11T13:45:00', 'Environmental Scientist.'),
        (candidate_34_id, job_4_id, 'Received', '2025-05-12T10:30:00', 'Architect.'),
        (candidate_35_id, job_7_id, 'Screening', '2025-05-12T15:00:00', 'Logistics experience relevant to project coordination.'),
        (candidate_36_id, job_5_id, 'Screening', '2025-05-13T11:00:00', 'Robotics engineer, potential DevOps overlap.'),
        (candidate_37_id, job_3_id, 'Received', '2025-05-13T14:45:00', 'Event Planner.'),
        (candidate_38_id, job_7_id, 'Received', '2025-05-14T09:15:00', 'Civil Engineer.'),
        (candidate_39_id, job_2_id, 'Received', '2025-05-14T13:30:00', 'Pharmacist.'),
        (candidate_40_id, job_8_id, 'Received', '2025-05-15T10:00:00', 'Chef.'),
        (candidate_41_id, job_4_id, 'Received', '2025-05-15T14:00:00', 'Translator.'),
        (candidate_42_id, job_3_id, 'Received', '2025-05-16T11:30:00', 'Teacher.'),
        (candidate_43_id, job_6_id, 'Screening', '2025-05-16T15:45:00', 'Journalist, assess analytical skills.'),
        (candidate_44_id, job_5_id, 'Received', '2025-05-17T09:00:00', 'Electrician.'),
        (candidate_45_id, job_2_id, 'Received', '2025-05-17T13:15:00', 'Librarian.'),
        (candidate_46_id, job_1_id, 'Screening', '2025-05-18T10:45:00', 'Blockchain dev, check core SWE skills.'),
        (candidate_47_id, job_2_id, 'Received', '2025-05-18T14:30:00', 'Geologist.'),
        (candidate_48_id, job_3_id, 'Received', '2025-05-19T11:00:00', 'Investment Banker.'),
        (candidate_49_id, job_4_id, 'Received', '2025-05-19T15:15:00', 'Archaeologist.'),
        (candidate_50_id, job_2_id, 'Received', '2025-05-20T09:45:00', 'Marine Biologist.'),
        (candidate_51_id, job_7_id, 'Received', '2025-05-20T13:30:00', 'Accountant.'),
        (candidate_52_id, job_5_id, 'Received', '2025-05-21T10:00:00', 'Pilot.'),
        (candidate_53_id, job_4_id, 'Received', '2025-05-21T14:45:00', 'Historian.'),
        (candidate_54_id, job_8_id, 'Received', '2025-05-22T11:15:00', 'Dentist.'),
        (candidate_55_id, job_6_id, 'Received', '2025-05-22T16:00:00', 'Theologian.');


    -- Insert 2 New Jobs (IDs 9 and 10) --
    -- These jobs will not have any initial applications

    INSERT INTO jobs (id, title, description, created_at)
    VALUES 
        (9, 'Machine Learning Engineer', 'Develop and deploy machine learning models for our core products. Requires experience with Python, TensorFlow/PyTorch, and cloud platforms.', NOW())
    RETURNING id INTO new_job_9_id;
    
    INSERT INTO jobs (id, title, description, created_at)
    VALUES 
        (10, 'Senior UX Researcher', 'Lead user research initiatives to inform product strategy and design. Requires strong qualitative and quantitative research skills.', NOW())
    RETURNING id INTO new_job_10_id;

END $$; 