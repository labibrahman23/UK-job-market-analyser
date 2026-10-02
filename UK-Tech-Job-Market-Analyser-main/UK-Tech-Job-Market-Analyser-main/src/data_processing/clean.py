import pandas as pd
import ast
import numpy as np

def fill_null_values(df):
    """ 
        Replace null values with appropriate place holder
        for numerical values, use NaN
        for text values, use Unkown
    """

    df['longitude'] = df['longitude'].fillna((np.nan))
    df['latitude'] = df['latitude'].fillna((np.nan))

    df['contract_time'] = df['contract_time'].fillna('Unknown')
    df['contract_type'] = df['contract_type'].fillna('Unknown')

    return df


def drop_columns(df):

    """     
        Drop Uncessesary columns
        __CLASS__ , category and adref
    """

    df = df.drop(columns= ['__CLASS__','category','adref'])

    return df

def clean_company(df):

    """
        Clean the company column to only contain company name
        Convert the str to dictionary data type
        Pull value using the display_name key
        Save the company column as only display_name
    
      """

    df['company'] = df['company'].apply(ast.literal_eval)
    df['company'] = df['company'].apply(lambda x: x.get('display_name'))


    """Reference
    https://stackoverflow.com/questions/35711059/extract-dictionary-value-from-column-in-data-frame? 
    https://stackoverflow.com/questions/52232742/how-to-use-ast-literal-eval-in-a-pandas-dataframe-and-handle-exceptions 
    https://www.geeksforgeeks.org/python/python-program-to-create-a-dictionary-from-a-string/ 
    """
    return df

def create_location_region(df):

    """
        Clean the location column to only contain region
        Match location against a list of pre-determined regions

        
    """

    regions = [
        "London",
        "South East",
        "South West",
        "East of England",
        "West Midlands",
        "East Midlands",
        "North West",
        "North East",
        "Yorkshire and the Humber",
        "Wales",
        "Scotland",
        "Northern Ireland"
        ]

    def get_location(location):
            if pd.isna(location):
                return pd.NA
            
            for region in regions:
                if region.lower().strip() in location.lower().strip():
                    return region
    
            return pd.NA
    
    df['location_region'] = df['location'].apply(get_location)

    return df


def convert_salary_predicted(df):

    """
        Convert salary is predicted to boolean data type
        Map 1 to True and 0 to False
        Apply mapping to column
    """

    mappings = {
        1:True, 
        0:False
        }

    df['salary_is_predicted'] = df['salary_is_predicted'].map(mappings)

    """
    Referenec:
    https://www.geeksforgeeks.org/python/python-pandas-map/ 
    """

    return df

def round_longitude_latitude(df):

    """
        Round latitude and longitude to 2 dp
    """

    df['longitude'] = round(df['longitude'],2)
    df['latitude'] = round(df['latitude'],2)


    return df

def convert_created(df):
    """
        Convert created to datetime data type
        Create year and month column
        
        
    """
    

    """Reference: https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column?"""

    df['created'] = pd.to_datetime(df['created'])
    df['created_year'] = df['created'].dt.year
    df['created_month'] = df['created'].dt.month

    df = df.drop('created', axis=1)
    
    return df

def find_skills(df):

    """
        Create new column with skills derived from description

        Create list of potential skills
        Search a description for each skill in list, add to new list if found
        Apply to entire column, adding findings to new skills column

    """


    technical_skills = ['python', 'sql', 'java', 'aws', 'docker', 'kubernetes', 'machine learning', 'pandas']
    
    def create_list(singular_description):
        skills_found = []
        for skill in technical_skills:
            if skill.lower() in singular_description.lower():
                skills_found.append(skill)

        return skills_found
    
    df['skills'] = df['description'].apply(create_list)

        
    return df


def create_average_salary(df):

    df['average_salary'] = (df['salary_max'] + df['salary_min']) / 2 

    return df

def find_job_categories(df):

    """
        Create new column with job categories derived from title

        Create list of potential job categories
        Search a title for each job in list,
        Apply to entire column, adding findings to job_category column

        LIST OF JOB CATEGORIES - seperated by job title, most common titles matched against role

    """


    job_categories = {
        # Software
        "developer": "Software Engineering",
        "software": "Software Engineering",
        "computer programmer": "Software Engineering",
        "full-stack": "Software Engineering",
        "front-end": "Software Engineering",
        "back-end": "Software Engineering",
        "web developer": "Software Engineering",
        "application developer": "Software Engineering",
        "programmer": "Software Engineering",


        "data engineer": "Data Engineering",
        "data architect": "Data Engineering",
        "data scientist": "Data Science",

        "data analyst": "Data Analytics",
        "business intelligence": "Data Analytics",
        "financial analyst": "Data Analytics",
        "risk data": "Data Analytics",
        "operations analyst": "Data Analytics",
        "reporting analyst": "Data Analytics",
        "market analyst": "Data Analytics",
        "market research": "Data Analytics",
        "business intelligence": "Data Analytics",
        "machine learning": "AI/ML",
        "ai": "AI/ML",

        "cloud": "Cloud Engineering",
        "devops": "DevOps",
        "infrastructure": "Infrastructure",
        "systems": "Systems Engineering",
        "network": "Network Engineering",

        "security": "Cyber Security",
        "cyber": "Cyber Security",
        "manager": "Management",
        "director": "Management",
        "lead": "Leadership",
        "architect": "Architecture",
        "engineer": "Software Engineering",
        "support": "Technical Support",
        "consultant": "Consulting",
        "project": "Project Management",
        "python": "Software Engineering"
    }



    def get_category(job_title):
        if pd.isna(job_title):
            return pd.NA
        
        for keyword, category in job_categories.items():
            if keyword.lower().strip() in job_title.lower().strip():
                return category

        return pd.NA
    df['job_category'] = df['title'].apply(get_category)

        
    return df


def clean_data(df):

    """
        Run main cleaning operations

    """

    df = df.drop_duplicates(subset="id")

    df = fill_null_values(df)
    

    df = drop_columns(df)

    

    df = clean_company(df)
    

    df = create_location_region(df)
    

    df = convert_salary_predicted(df)
  

    df = round_longitude_latitude(df)

    df = create_average_salary(df)
    

    df = convert_created(df)
    
    df = find_skills(df)

    df = find_job_categories(df)

    print("Data cleaned")
    return df


"""References:

 https://stackoverflow.com/questions/35711059/extract-dictionary-value-from-column-in-data-frame? 
 https://stackoverflow.com/questions/52232742/how-to-use-ast-literal-eval-in-a-pandas-dataframe-and-handle-exceptions 
 https://www.geeksforgeeks.org/python/python-program-to-create-a-dictionary-from-a-string/ 
 https://www.trymito.io/excel-to-python/functions/text/TRIM 

https://stackoverflow.com/questions/36226083/how-to-find-which-columns-contain-any-nan-value-in-pandas-dataframe 


"""