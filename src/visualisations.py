import plotly.express as px


def plot_most_needed_roles(df):

    df = df.sort_values("number_of_vacancies", ascending=True)

    fig = px.bar(
        df,
        x="number_of_vacancies",
        y="role",
        labels={
            "number_of_vacancies": "Number of Vacancies",
            "role": "Job Role",
            "average_salary": "Average Salary"
        },
        orientation="h",
        hover_data={
            "average_salary": True,
            "number_of_vacancies": True,
            "role": False
        }
    )

    return fig


def plot_top_companies(df):

    df = df.sort_values("number_of_vacancies",ascending=True)

    fig = px.bar(
        df,
        x="number_of_vacancies",
        y="company",
        labels={
            "number_of_vacancies": "Vacancies",
            "company" : "Company"
        },
        orientation="h"
        )
    return fig


def plot_top_locations(df):

    fig = px.pie(
        df,
        names="location",
        values="number_of_vacancies",
        title="Job Vacancies by Location"
    )

    return fig

"""REFERENCING
https://plotly.com/python/bar-charts/ 
https://plotly.com/python/pie-charts/ 
"""