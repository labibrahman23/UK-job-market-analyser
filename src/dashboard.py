import streamlit as st

from queries import (
    get_dashboard_metrics,
    get_most_needed_roles,
    get_jobs_by_area
)

from visualisations import (
    plot_most_needed_roles,
    plot_top_locations
)

from database import create_connection


st.set_page_config(
    layout="wide",
    page_title="UK Tech Job Market Dashboard"
)


connection = create_connection()


left_side, right_side = st.columns([1.3, 1.8])


with left_side:

    with st.container():

        st.subheader("UK Tech Job Market Dashboard")

        st.write("""
        This dashboard analyses:
        """)

        metrics = get_dashboard_metrics(connection).iloc[0]

        col1, col2, col3, col4 = st.columns(4)


    with st.container():

        with col1:
            st.metric(
                "Jobs Analysed:",
                metrics["number_of_jobs"]
            )

        with col2:
            st.metric(
                "Companies Analysed:",
                metrics["number_of_companies"]
            )

        with col3:
            st.metric(
                "Locations Analysed:",
                metrics["locations"]
            )

        with col4:
            st.metric(
                "Average Salary:",
                f"£{metrics['average_salary']:,.0f}"
            )


with right_side:

    with st.container():

        st.subheader("Most needed Job roles")

        df_most_needed_roles = get_most_needed_roles(connection)

        most_needed_roles_graph = plot_most_needed_roles(
            df_most_needed_roles
        )

        st.plotly_chart(
            most_needed_roles_graph,
            use_container_width=True
        )


connection.close()