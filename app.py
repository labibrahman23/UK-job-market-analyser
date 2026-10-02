from dash import Dash, html, dcc, dash_table
from src.data_processing.database import create_connection
from src.data_analysis.queries import (
    get_dashboard_metrics,
    get_most_needed_roles,
    get_average_salary,
    get_top_companies,
    get_jobs_by_area,
    get_skill_analysis
)
from src.data_analysis.visualisations import(
    plot_most_needed_roles,
    plot_top_companies,
    plot_top_locations
)


app = Dash(__name__)

connection = create_connection()

metrics = get_dashboard_metrics(connection).iloc[0]

# Create Data frames
df_most_needed_roles = get_most_needed_roles(connection)

df_average_salary = get_average_salary(connection)

df_top_companies = get_top_companies(connection)

df_top_locations = get_jobs_by_area(connection)

df_skills_analysis = get_skill_analysis(connection)

most_needed_roles_graph = plot_most_needed_roles(df_most_needed_roles)

top_companies_graph = plot_top_companies(df_top_companies)

top_locations_graph = plot_top_locations(df_top_locations)

app.layout = html.Div([

    html.H1("UK Tech Job Market Dashboard"),
    

    html.Div([

        # overview
        html.Div([

            # dashboard metrics
            html.Div([
                html.H3("Overview"),

                html.Div([
                    html.Div([
                        html.H4("Jobs"),
                        html.H2(f"{metrics['number_of_jobs']:,}")
                    ]),

                    html.Div([
                        html.H4("Companies"),
                        html.H2(
                            f"{metrics['number_of_companies']:,}")
                    ]),

                    html.Div([
                        html.H4("Locations"),
                        html.H2(f"{metrics['locations']:,}")
                    ]),

                    html.Div([
                        html.H4("Avg Salary"),
                        html.H2(f"£{metrics['average_salary']:,.0f}")
                    ])

                ], style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "gap": "5px"
                })

            ]),

            # average salary per role
            html.Div([
                html.H3("Average Salary Per Role",style={"marginBottom": "7px"}),
                dash_table.DataTable(
                    data=df_average_salary.to_dict(
                        "records"),
                    columns=[
                        {
                            "name": "Role",
                            "id": "role"
                        },
                        {
                            "name": "Average Salary",
                            "id": "average_salary"
                        }
                    ],

                    style_table={
                        "width": "100%",
                        "height": "273px",
                        "overflowY": "auto"
                    },

                    style_cell={
                        "textAlign": "left",
                        "padding": "4px",
                        "fontSize": "16px",
                        "height": "23px"
                    },

                    style_header={
                        "fontWeight": "bold",
                        "fontSize": "18px"
                    }

                )

            ], style={
                "marginTop": "19px"
            })

        ], style={
            "width": "35%"
        }),

        # most needed jobs
        html.Div([

            html.H3("Most Demanded Job Roles"),

            dcc.Graph(
                figure=most_needed_roles_graph,
                style={
                    "height": "500px"
                }
            )

        ], style={
            "width": "65%"
        })

    ], style={
        "display": "flex",
        "gap": "30px",
        "alignItems": "stretch"
    }),


    # top hiring companies and top locations

    html.Div([
        # top hiring companies
        html.Div([
            html.H3("Top Hiring Companies"),
            dcc.Graph(
                figure=top_companies_graph,
                style={"height": "400px"}
            )], 
        style={
            "width": "50%"
        }),

        # top locations
        html.Div([
            html.H3("Top Locations"),
            dcc.Graph(figure=top_locations_graph, style={"height": "400px"})], 
        style={"width": "50%"})], 

    style={
        "display": "flex",
        "gap": "30px",
        "marginTop": "30px"
    }),


    # skills 

    html.Div([
        html.H3("Skills Analysis"),
        dash_table.DataTable(
           data=df_skills_analysis.to_dict("records"),
            columns=[
                {
                    "name": "Skill",
                    "id": "skill"
                },
                {
                    "name": "Vacancies",
                    "id": "number_of_vacancies"
                },
                {
                    "name": "% of Jobs",
                    "id": "percentage_of_jobs"
                },
                {
                    "name": "Average Salary",
                    "id": "average_salary"
                }
            ],

            style_table={
                "width": "100%",
                "overflowX": "auto"
            },

            style_cell={
                "textAlign": "left",
                "padding": "9px",
                "fontSize": "15px"
            },

            style_header={
                "fontWeight": "bold",
                "fontSize": "14px"
            },

            style_data={
                "height": "32px"
            }

        )], 

        style={"marginTop": "32px"})

])


if __name__ == "__main__":
    app.run(debug=True)

    """
References:

dash : https://dash.plotly.com/
dash table: https://dash.plotly.com/datatable
plot: https://plotly.com/python/
dash  layout: https://dash.plotly.com/layout

"""