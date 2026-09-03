import streamlit as st

st.title("Salary Prediction")
st.subheader("Can job characteristics be used to predict salaries for UK technology jobs?")


st.title("Recommended Solution")
st.markdown("""I used a random forest regression model to investigate if data from job postings could be used to predict salaries for UK technology jobs \n
Data for this model was collected from Adzuna, an online job postings page, with an estimated 40,000 technology postings.\n
The features I investigated included: 

- Job description
- Location
- Skills required
- Contract Type
- Job category
""")



st.title("How this could be valuable?")

st.markdown(""" 

    **Market Analysis**\n
    The model could present which characteristics are associated with different salary ranges \n

    **Employers**\n
    Employers can use findings to create job listings with accurate salaries \n

    **Job seekers**\n
    The model can help job seekers understand which salaries are associated with which salary levels\n


    **In the future**\n
    As more data is used to train this model, it may produce more accurate results, helping to reduce confusion between employeers and job seekers.

""")

st.title("Created solution")

results = {
    "Features": [
        "Contract Type",
        "Job Category",
        "Location",
        "Contract Type + Job category",
        "Contract Type + Job category + Skills"],

    "R²" : [
        0.031,
        0.049,
        0.050,
        0.089,
        0.097],
   
     "RMSE": [
         "£34.9k",
         "34.5k",
         "30.1k",
         "£33.8k",
         "£33.6k"],
}



st.dataframe(results, hide_index=True, use_container_width=True)

st.subheader("What does this show?")
st.markdown("""

    Using multiple job charactersistics usually gave me more accurate readings.
    However the R2 value is not very high therefore the model does not accurately explain variations in salaries.
    The RMSE shows that the predicted salary is typically £30,000 off the actual salary.

    **Evaluation**

    This model is not accurate enough to be used to create reliable salary predictions.
    However, it shows that there are some characteristics are related to salary ranges such as job category and contract type.

    These results could be more accurate which greater feature range and a large dataset.
""")


st.title("Improvments")

st.markdown("""

    **More Data**

    A larger volume of data could have been used in training the model.
    I could have pulled more data from adzuna as there are over 40,000 technology job postings.
    
    **Better feature selection**

    More effective features to predict salary such as company, as this is known to be a large factor in salaries offered.
    I could also have used more features, e.g using a combination of location, company, skills and category, as more features tend to create more accurate results.

    **Better skill extraction**
    The skills data column only contained a limited number of possible values.
    To make this model more accurate, this list could be expanded further to match more skills to different salary ranges
""")


st.title("Overall")

st.markdown("""
    Currently, the model does not provide accurate presults to correctly predict UK technology job salaries

    However, there are some features which show that this data can be used to predict salaries if they were such as category and contract_type.
    
    Overall, I will aim to improve this project by improving the cleaning of data, improving feature engineering and experiemnting with different modelling techniques.
""")