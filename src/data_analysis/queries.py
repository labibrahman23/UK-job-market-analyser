import pandas as pd


def get_dashboard_metrics(connection):

    """createa a dataframe of dashboard metrics including:
     -number of jobs analysed
     -number of unique companies which were analysed
     -average Salary overall
     -number of unique locations analysed"""

    query = """
    SELECT COUNT(*) AS number_of_jobs, COUNT(DISTINCT(company)) AS number_of_companies, AVG((salary_max + salary_min) / 2) AS average_salary, COUNT(DISTINCT(location)) AS locations
    FROM uk_tech_job_data;
    """

    return pd.read_sql(query, connection)


def get_most_needed_roles(connection):

    """ 
    Create a dataframe of the most needed job roles
    Get job categories from new column we created, the number of vacancies and average salary rounded to nearest £
    Ensure that the Null values are not selected
    Order the data by number of jobs DESC, with limit 10 to get the top 10 values

    """

    query = """
    SELECT job_category AS role, COUNT(*) AS number_of_vacancies, ROUND(AVG((salary_max + salary_min)/2), 0) AS average_salary 
    from uk_tech_job_data
    WHERE job_category IS NOT NULL
    GROUP BY job_category
    ORDER BY number_of_vacancies DESC
    LIMIT 10;
    """

    return pd.read_sql(query, connection)

def get_average_salary(connection):

    """ 
    Create a dataframe of average salary per role, using previous most_needed_job roles
    This creates average salaries for the top 10 most needed job roles
    Using .loc to take the columns from the previous data frame
    """
    df = get_most_needed_roles(connection)

    return df.loc[:, ['role', 'average_salary']]

def get_top_companies(connection):

    """ 
    create a dataframe with the top 6 most hiring companies
    Group by the company column I created"""

    query = """
    SELECT company, COUNT(*) AS number_of_vacancies
    from uk_tech_job_data
    WHERE company IS NOT NULL
    GROUP BY company
    ORDER BY number_of_vacancies DESC
    LIMIT 6;
    """

    return pd.read_sql(query, connection)


def get_jobs_by_area(connection):

    
    """Get the number of jobs by area
    Using ILIKE, match jobs with top 5 cities and other
    ""
    Group the records which have the same cities together and get the count of each city
    """
    query = """
    SELECT
        CASE
            WHEN location ILIKE '%London%' THEN 'London'
            WHEN location ILIKE '%Birmingham%' THEN 'Birmingham'
            WHEN location ILIKE '%Manchester%' THEN 'Manchester'
            WHEN location ILIKE '%Bristol%' THEN 'Bristol'
            WHEN location ILIKE '%Belfast%' THEN 'Belfast'
            ELSE 'Other'
        END AS location,

        COUNT(*) AS number_of_vacancies

    FROM uk_tech_job_data

    WHERE location IS NOT NULL

    GROUP BY
        CASE
            WHEN location ILIKE '%London%' THEN 'London'
            WHEN location ILIKE '%Birmingham%' THEN 'Birmingham'
            WHEN location ILIKE '%Manchester%' THEN 'Manchester'
            WHEN location ILIKE '%Bristol%' THEN 'Bristol'
            WHEN location ILIKE '%Belfast%' THEN 'Belfast'
            ELSE 'Other'
        END

    ORDER BY number_of_vacancies DESC;
    """

    """
     REFERENCNG : https://www.datacamp.com/doc/postgresql/ilike
        https://stackoverflow.com/questions/62969613/conditional-case-and-like-ilike 
        """

    return pd.read_sql(query, connection)

def get_skill_analysis(connection):

    """
    Get the top skills
    Using ILIKE, skills with top skills which are commonly needed
    Group the records which have the same skills needed together
    Get the number of each group
    Create a perctanage of job market column by rounding and calculating percentage ( group total / total job maret)
    Return a dataframe with skill, number of jobs it is listed in, percentage of job market and average salary"""

    query = """
    SELECT
        CASE
            WHEN skills ILIKE '%python%' THEN 'Python'
            WHEN skills ILIKE '%sql%' THEN 'SQL'
            WHEN skills ILIKE '%java%' THEN 'Java'
            WHEN skills ILIKE '%aws%' THEN 'AWS'
            WHEN skills ILIKE '%docker%' THEN 'Docker'
            WHEN skills ILIKE '%machine learning%' THEN 'Machine Learning'
            WHEN skills ILIKE '%pandas%' THEN 'Pandas'
        END AS skill,

        COUNT(*) AS number_of_vacancies,

        ROUND(COUNT(*) * 100.0/ (SELECT COUNT(*) FROM uk_tech_job_data),1) AS percentage_of_jobs,

        ROUND(AVG((salary_max + salary_min)/2),0) AS average_salary

    FROM uk_tech_job_data

    WHERE
        skills ILIKE '%python%'
        OR skills ILIKE '%sql%'
        OR skills ILIKE '%java%'
        OR skills ILIKE '%aws%'
        OR skills ILIKE '%docker%'
        OR skills ILIKE '%machine learning%'
        OR skills ILIKE '%pandas%'

    GROUP BY skill

    ORDER BY number_of_vacancies DESC;
    """

    return pd.read_sql(query, connection)

"""REFERENCNG : https://www.datacamp.com/doc/postgresql/ilike """