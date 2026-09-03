import json
import requests
import pandas as pd

API_ID = "fc9a8b18"
API_KEY = "0c4a5a30ec2959e61c8f9eeecd99c9c7"



def download_data():

    jobs = []

    for i in range(1,100):
        url = f"https://api.adzuna.com/v1/api/jobs/gb/search/{i}?app_id={API_ID}&app_key={API_KEY}&results_per_page=100&category=it-jobs"

        response = requests.get(url)

        data = response.json()

        jobs.extend(data["results"])

    with open("data/raw/data.json", "w") as json_file:
        json.dump(jobs, json_file, indent= 4)

    """ References:
    https://stackabuse.com/how-to-get-json-from-a-url-in-python/ 
    https://www.geeksforgeeks.org/python/json-dump-in-python/ 
    """

    
    df = pd.DataFrame(jobs)


    """References:
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html 
    """

    df.to_csv('data/raw/data.csv', index=False)


    """References: 
    https://www.geeksforgeeks.org/pandas/saving-a-pandas-dataframe-as-a-csv/ 
    """

    print("Data downloaded")

    


"""
DATA SOURCE: 
https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=fc9a8b18&app_key=0c4a5a30ec2959e61c8f9eeecd99c9c7&results_per_page=100&category=it-jobs 
"""