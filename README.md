# 🏠 House Price Prediction

A Machine Learning project that predicts median house values using the California Housing Dataset. The project includes Exploratory Data Analysis, data preprocessing, model training, model evaluation, and a web application built using FastAPI and Streamlit.

## 📌 Project Overview

The objective of this project is to build a regression model that predicts house prices based on different housing and demographic features.

The project compares multiple regression algorithms and uses the best-performing model to create an interactive house price prediction application.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Model Serialization:** Joblib
- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit
- **API Requests:** Requests
- **Development Environment:** Jupyter Notebook, VS Code

## 📂 Dataset

**California Housing Dataset**

The dataset is obtained using Scikit-learn's `fetch_california_housing()` function.

- Total records: 20,640
- Input features: 8
- Target variable: Median House Value

### Features

| Feature | Description |
|---|---|
| MedInc | Median income in the block group |
| HouseAge | Median house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Block group population |
| AveOccup | Average household occupancy |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

**Target Variable:** `Price`

The target values are expressed in units of $100,000. The application converts predictions into dollar values for display.

## 🔍 Exploratory Data Analysis

The following analysis was performed:

- Target variable distribution analysis
- Median income vs. house price analysis
- Average rooms vs. house price analysis
- House age vs. house price analysis
- Correlation heatmap
- Identification of relationships between input features and the target variable

## ⚙️ Machine Learning Workflow

1. Load the California Housing Dataset.
2. Convert the dataset into a Pandas DataFrame.
3. Perform Exploratory Data Analysis.
4. Separate input features and target variable.
5. Split the data into training and testing sets.
6. Apply StandardScaler for Linear Regression.
7. Train multiple regression models.
8. Evaluate models using MAE, RMSE, and R² Score.
9. Analyze overfitting and experiment with model tuning.
10. Select the best-performing model.
11. Save the trained model using Joblib.

## 🤖 Models Implemented

The following regression algorithms were implemented:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Tuned Random Forest Regressor

## 📊 Model Performance

The models were evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Random Forest | 0.327543 | 0.505340 | 0.805123 |
| Tuned Random Forest | 0.333221 | 0.511471 | 0.800366 |
| Decision Tree | 0.454679 | 0.703729 | 0.622076 |
| Linear Regression | 0.533200 | 0.745581 | 0.575788 |

### Best Performing Model

**Random Forest Regressor**

- MAE: 0.327543
- RMSE: 0.505340
- R² Score: 0.805123

The Random Forest model achieved an R² score of approximately 80.51% on the test dataset.

The tuned Random Forest model showed a smaller training-testing performance gap, but its test performance was slightly lower. Therefore, the original Random Forest model was selected as the final model.

## 🌐 Web Application

The trained model is integrated into a web application using FastAPI and Streamlit.

### Application Features

- User-friendly interface for entering house details.
- Eight input fields corresponding to the model features.
- FastAPI endpoint for making predictions.
- Real-time prediction when the user submits the input.
- Predicted house price displayed in dollars.

### Application Architecture

1. User enters house details in the Streamlit interface.
2. Streamlit sends the input data to the FastAPI backend.
3. FastAPI loads the saved Random Forest model.
4. The model generates a house price prediction.
5. The predicted price is returned to Streamlit and displayed to the user.

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── .streamlit/
│   └── config.toml
│
├── app/
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── house_price_model.pkl
├── model.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/kaushiki2024/House-Price-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd House-Price-Prediction
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI Backend

Open the first terminal and run:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

`http://127.0.0.1:8000`

### 6. Start the Streamlit Frontend

Open a second terminal, activate the same virtual environment, navigate to the project directory, and run:

```bash
streamlit run frontend/streamlit_app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

**Note:** Keep both terminals running while using the application.

## 📚 Key Learnings

- Exploratory Data Analysis and feature relationships.
- Data preprocessing and train-test splitting.
- Feature scaling and prevention of data leakage.
- Regression algorithms and model comparison.
- Model evaluation using regression metrics.
- Understanding overfitting and model tuning.
- Saving and loading trained models using Joblib.
- Building REST APIs using FastAPI.
- Integrating a Machine Learning model with Streamlit.

## 🎯 Conclusion

This project demonstrates an end-to-end Machine Learning workflow, from dataset exploration and model development to application development.

The Random Forest Regressor achieved the best test performance among the implemented models, with an R² score of approximately 80.51%.

The trained model was integrated into a web application using FastAPI and Streamlit, allowing users to enter house-related information and obtain estimated house prices.

---

**Developed using Python and Machine Learning.**