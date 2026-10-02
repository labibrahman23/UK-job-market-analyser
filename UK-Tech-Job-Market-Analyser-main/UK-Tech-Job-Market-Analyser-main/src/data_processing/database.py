import psycopg2

def create_connection():
        
    """Create and return a connection to the PostgreSQL database."""    
        

    connection = psycopg2.connect(
    host=("localhost"),
    port=("5432"),
    database=("uk_job_market_data"),
    user=("postgres"),
    password=("LabibDataProjects")
    )

    return connection





    """
    Load cleaned CSV data into PostgreSQL using COPY.
    """

def load_csv_to_postgres(csv_path):

    

    connection = create_connection()

    with connection.cursor() as cursor:

        with open("data/load_data.sql", "r") as sql_file:
            query = sql_file.read()

        

        with open(csv_path, "r", encoding="utf-8") as file:
            cursor.copy_expert(query,file)


    connection.commit()

    connection.close()
    