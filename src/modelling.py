import pandas as pd
import warnings

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline


warnings.filterwarnings('ignore')
df = pd.read_csv("data/cleaned/data.csv")
df = df.dropna(subset=['salary_max'])



train_df = df.copy()

X = df[['job_category', 'contract_type']]

y = df['average_salary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

independent_variables = ['job_category', 'contract_type' ]


categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

preprocessor = ColumnTransformer([
    ('categorical', categorical_pipeline, independent_variables)
    ])



regressor = RandomForestRegressor(
    n_estimators=100,
    random_state=42
    )
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', regressor)
])

model.fit(X_train,y_train)

predictions = model.predict(X_test)
mse = mean_squared_error(y_test,predictions)
r2 = r2_score(y_test,predictions)

print("MSE : ", mse)
print("R2:", r2)



"""Experimenting

Independent variables: contract_type
MSE: 1215209328.5242314
R2: 0.03089077719848765

Independent variables: job_category
MSE: 1192605627.4028146
R2: 0.04891685279882585


Independent variables: location_region
MSE: 904,953,051.6975726
R²: 0.05016847032921912

Independent variables: skills
MSE: 1251104103.3580492
R2: 0.0022652914279983616

Independent variables: location
MSE: 1248212974.2002292
R2: 0.0045709188334068784

Independent variables: contract_type, job_category
MSE: 1142591441.692544
R2: 0.08880233384725766

Independent variables: contract_type, job_category, skills
MSE: 1132339912.2256737
R2: 0.0969777580486425

Independent variables: contract_type, job_category, skills, location
MSE: 1181895740.4363008
R2: 0.05745780948076207


"""
"""Referencing
https://www.geeksforgeeks.org/machine-learning/random-forest-regression-in-python/ 
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html?
https://www.geeksforgeeks.org/machine-learning/ml-one-hot-encoding/ 
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html 
https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
"""