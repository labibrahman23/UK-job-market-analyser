import pandas as pd


def get_dashboard_metrics(connection):

    query = """
    SELECT
        COUNT(*) AS number_of_jobs,
        COUNT(DISTINCT(company)) AS number_of_companies,
        AVG((salary_max + salary_min) / 2) AS average_salary,
        COUNT(DISTINCT(location)) AS locations
    FROM uk_tech_job_data;
    """

    return pd.read_sql(query, connection)


def get_most_needed_roles(connection):

    query = """
    SELECT
        job_category AS role,
        COUNT(*) AS number_of_vacancies,
        ROUND(AVG((salary_max + salary_min) / 2), 0) AS average_salary
    FROM uk_tech_job_data
    WHERE job_category IS NOT NULL
    GROUP BY job_category
    ORDER BY number_of_vacancies DESC
    LIMIT 10;
    """

    return pd.read_sql(query, connection)