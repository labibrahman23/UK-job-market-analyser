COPY uk_tech_job_data (
    description,
    title,
    salary_min,
    location,
    longitude,
    redirect_url,
    latitude,
    salary_max,
    salary_is_predicted,
    company,
    id,
    contract_time,
    contract_type,
    skills,
    job_category,
    location_region,
    average_salary,
    created_month,
    created_year
)
FROM STDIN
WITH (
    FORMAT CSV,
    HEADER TRUE
);