# Bus_Timeprediction
Daily Report: Bus Trip Duration Prediction Project
1. Overview
Objective: To predict bus trip durations using machine learning models to optimize scheduling and improve operational efficiency.

2. Activities Completed
Ongoing

Data Collection and Preprocessing

Data File: Loaded Trip Data for ML Model.csv.
Preprocessing Steps:
Converted date columns to datetime format.
Handled missing values.
Engineered features including route names, trip start hours, and trip day-of-week.
Removed unnecessary features (Km_Difference, Actual_Km, Route_Hour_Interaction).
Model Development

Models Implemented:
ExtraTreesRegressor
GradientBoostingRegressor
Hyperparameter Tuning:
Used GridSearchCV and RandomizedSearchCV to find the best parameters.
Model Evaluation:
Evaluated using metrics: Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
Frontend Development

Tools Used: Flask and Tkinter.
Tasks Completed:
Created a Flask-based web application to input data and display predictions.
Implemented a Tkinter GUI for local testing.
Issues Encountered and Solutions

Issue: ModuleNotFoundError due to missing _loss module.
Solution: Ensured all required modules were installed and verified environment compatibility.
3. Key Findings
Model Performance:

ExtraTreesRegressor:
MAE: 22.116332176356348
RMSE: 76.31539226017614

GradientBoostingRegressor:
MAE: 26.365829681955272
RMSE: 72.24567273159064

Best Model: Ongoing but for now ExtraTreesRegressor:
Frontend Usability:

Flask-based web application provides an intuitive interface for users to input features and get predictions.
Tkinter GUI has been useful for quick local testing.
4. Next Steps
Refinement of Models:

Explore additional feature engineering techniques.
Consider other regression models for comparison.
Enhancements to Frontend:

Improve user interface for better experience.
Add validation and error handling for input data.
Testing and Validation:

Conduct comprehensive testing with real-world data.
Validate predictions against actual trip durations.
5. Summary
The project has made significant progress in predicting bus trip durations using machine learning models. Key achievements include successful model training, evaluation, and the development of user-friendly interfaces. Moving forward, the focus will be on refining models and enhancing the frontend to ensure robustness and ease of use.

Prepared by: Kavya Bhardwaj
