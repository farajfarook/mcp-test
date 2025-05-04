-- Data migration for additional candidates who have not applied for any jobs

DO $$
DECLARE
    lily_id INTEGER;
    james_id INTEGER;
    mia_id INTEGER;
    skill_id INTEGER;
BEGIN
    -- Insert candidate: Lily Evans
    INSERT INTO candidates (name, current_location, summary)
    VALUES (
        'Lily Evans', 
        'Dublin, Ireland',
        'Data analyst with a strong background in statistical modeling and data visualization, passionate about turning raw data into actionable insights.'
    ) RETURNING id INTO lily_id;

    -- Lily Evans - Work Experience
    INSERT INTO work_experience (candidate_id, company_name, role, start_date, end_date, is_current, responsibilities)
    VALUES 
    (lily_id, 'Insight Analytics', 'Data Analyst', '2022-01-01', NULL, TRUE, 'Developing dashboards, analyzing large datasets, and presenting actionable insights to clients.'),
    (lily_id, 'MarketView', 'Junior Data Analyst', '2020-06-01', '2021-12-31', FALSE, 'Supported senior analysts in data cleaning, visualization, and reporting.');

    -- Lily Evans - Education
    INSERT INTO education (candidate_id, institution, degree, field_of_study, start_year, end_year)
    VALUES
    (lily_id, 'Trinity College Dublin', 'Bachelor of Science', 'Statistics', 2016, 2020);

    -- Lily Evans - Skills
    INSERT INTO skills (name, category) VALUES ('Python', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Python' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (lily_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Data Visualization', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Data Visualization' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (lily_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Statistical Analysis', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Statistical Analysis' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (lily_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Communication', 'Soft') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Communication' AND category = 'Soft';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (lily_id, skill_id);

    -- Lily Evans - Achievements
    INSERT INTO achievements (candidate_id, description)
    VALUES
    (lily_id, 'Developed a predictive model that improved client retention by 15%'),
    (lily_id, 'Presented at the Irish Data Science Conference 2023');

    -- Insert candidate: James Brown
    INSERT INTO candidates (name, current_location, summary)
    VALUES (
        'James Brown', 
        'Cape Town, South Africa',
        'Software developer with expertise in Python and Django, focused on building scalable web applications and APIs.'
    ) RETURNING id INTO james_id;

    -- James Brown - Work Experience
    INSERT INTO work_experience (candidate_id, company_name, role, start_date, end_date, is_current, responsibilities)
    VALUES 
    (james_id, 'WebWorks', 'Software Developer', '2021-03-01', NULL, TRUE, 'Developing and maintaining Django-based web applications and REST APIs.'),
    (james_id, 'CodeBase Africa', 'Intern Developer', '2020-01-01', '2021-02-28', FALSE, 'Assisted in backend development and testing.');

    -- James Brown - Education
    INSERT INTO education (candidate_id, institution, degree, field_of_study, start_year, end_year)
    VALUES
    (james_id, 'University of Cape Town', 'Bachelor of Science', 'Computer Science', 2016, 2019);

    -- James Brown - Skills
    INSERT INTO skills (name, category) VALUES ('Python', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Python' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (james_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Django', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Django' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (james_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('REST APIs', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'REST APIs' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (james_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Teamwork', 'Soft') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Teamwork' AND category = 'Soft';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (james_id, skill_id);

    -- James Brown - Achievements
    INSERT INTO achievements (candidate_id, description)
    VALUES
    (james_id, 'Built a scalable e-commerce backend serving 10,000+ users'),
    (james_id, 'Awarded Best Intern Developer 2020 at CodeBase Africa');

    -- Insert candidate: Mia Wong
    INSERT INTO candidates (name, current_location, summary)
    VALUES (
        'Mia Wong', 
        'Hong Kong',
        'Graphic designer with a flair for creating visually compelling designs and a strong understanding of branding and marketing strategies.'
    ) RETURNING id INTO mia_id;

    -- Mia Wong - Work Experience
    INSERT INTO work_experience (candidate_id, company_name, role, start_date, end_date, is_current, responsibilities)
    VALUES 
    (mia_id, 'Creative Studio HK', 'Graphic Designer', '2021-07-01', NULL, TRUE, 'Designing marketing materials, branding assets, and digital content for clients.'),
    (mia_id, 'BrandLab', 'Junior Designer', '2019-09-01', '2021-06-30', FALSE, 'Assisted in branding projects and social media campaigns.');

    -- Mia Wong - Education
    INSERT INTO education (candidate_id, institution, degree, field_of_study, start_year, end_year)
    VALUES
    (mia_id, 'Hong Kong Polytechnic University', 'Bachelor of Arts', 'Design', 2015, 2019);

    -- Mia Wong - Skills
    INSERT INTO skills (name, category) VALUES ('Adobe Photoshop', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Adobe Photoshop' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (mia_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Branding', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Branding' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (mia_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Illustration', 'Technical') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Illustration' AND category = 'Technical';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (mia_id, skill_id);
    INSERT INTO skills (name, category) VALUES ('Creativity', 'Soft') ON CONFLICT (name, category) DO NOTHING;
    SELECT id INTO skill_id FROM skills WHERE name = 'Creativity' AND category = 'Soft';
    INSERT INTO candidate_skills (candidate_id, skill_id) VALUES (mia_id, skill_id);

    -- Mia Wong - Achievements
    INSERT INTO achievements (candidate_id, description)
    VALUES
    (mia_id, 'Designed the winning logo for HK Startup Fest 2023'),
    (mia_id, 'Featured in Asia Creative Magazine, 2024');
END $$;