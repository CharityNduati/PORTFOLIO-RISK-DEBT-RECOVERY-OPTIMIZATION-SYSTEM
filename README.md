# 📈 Machine Learning-Driven Portfolio Risk & Debt Recovery Optimization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://portfolio-risk-debt-recovery-optimization-system-hwvhqiyk9nt5e.streamlit.app/)

## 📌 Project Overview
Debt recovery organizations manage thousands of delinquent accounts across multiple clients. Efficient recovery requires identifying which accounts are most likely to respond positively, prioritizing collector efforts, optimizing resource allocation, and ensuring transparency in decision-making.

This project develops a **machine learning-powered debt recovery analytics system** that transforms traditional collection processes from manual prioritization into data-driven decision support.

The solution predicts debtor payment propensity, segments portfolio risk profiles, prioritizes collector activities, and provides explainable predictions using SHAP to improve trust and adoption among business users.

The project follows the **CRISP-DM (Cross Industry Standard Process for Data Mining)** methodology:
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

---

## 🎯 Business Context & Problem Statement

### Context
Traditional debt recovery operations often depend on:
* Manual account prioritization
* Static historical reports
* Collector experience and intuition
* Generic customer follow-up strategies

These approaches can lead to:
* Inefficient collector time allocation
* Delayed recoveries
* Low engagement rates
* Missed high-value recovery opportunities

### Problem Statement
> *How can historical account information and machine learning be used to identify high-potential accounts, optimize collection resources, and improve recovery outcomes?*

---

## 🎯 Project Objectives

1. **Predict Payment Propensity:** Estimate the likelihood that a delinquent account will successfully engage with collection efforts through *Promise To Pay*, *Negotiation*, or *Debt clearance*.
2. **Prioritize Collector Activities:** Create a data-driven priority queue that helps collectors focus on high-probability recovery accounts, high-value accounts, and accounts requiring immediate intervention.
3. **Segment Debt Portfolios:** Group accounts with similar characteristics using clustering techniques to enable targeted recovery strategies.
4. **Provide Explainable Predictions:** Use Explainable AI techniques (SHAP) to show why an account received a particular risk score, which factors influence payment likelihood, and how managers can interpret model decisions.

---

## 📊 Dataset Overview

**Dataset File:** `active_portfolio.xlsx`

### Portfolio Summary
* **Total Accounts Analyzed:** 2,709
* **Total Portfolio Value:** KES 232.59 Million

### Feature Categories
The dataset contains information across multiple domains:
* Client details
* Outstanding debt balances
* Days Past Due (DPD)
* Contact availability
* Loan characteristics
* Outsourcing timelines
* Operational account status

### 🎯 Target Variable (`PAYMENT_SUCCESS`)
Binary classification target:
* **`1` (Successful engagement):** Promise To Pay, Negotiation, Debt Cleared
* **`0` (Low engagement):** Unreachable, Disputed, Inactive

---

## 🔄 CRISP-DM Methodology

### 1. Business Understanding
The goal was to improve debt recovery efficiency by enabling collection teams to make decisions using predictive analytics rather than relying only on manual prioritization.

**Expected business outcomes:**
* Improved collector productivity
* Better account prioritization
* Increased recovery opportunities
* Transparent decision-making

### 2. Data Understanding
Performed exploratory analysis to understand:
* Portfolio composition
* Debt distribution
* Account characteristics
* Recovery patterns
* Missing data patterns

**Key questions explored:**
* Which account characteristics influence successful engagement?
* Which segments represent higher recovery opportunities?
* How is the portfolio distributed across clients and risk groups?

### 3. Data Preparation & Feature Engineering
* **Data Cleaning:** Missing value handling, removal of redundant operational fields, and data consistency checks.
* **Feature Engineering:** Created meaningful recovery indicators including contactability ratios, balance tiers, temporal features (such as days since outsource), and account-level risk indicators.
* **Data Transformation:** Applied numerical feature scaling using `StandardScaler`, categorical variable encoding, and feature preparation for machine learning models.

### 🤖 4. Machine Learning Modeling
Multiple models were developed and compared.

#### Predictive Classification Models
* **Logistic Regression:** Used as an interpretable baseline model.
* **Random Forest Classifier:** Used to capture nonlinear relationships and identify important features.
* **XGBoost Classifier:** Selected as the final predictive model due to strong performance on structured tabular financial data.

#### Portfolio Segmentation
* **K-Means Clustering:** Used to identify groups of accounts with similar characteristics and support differentiated recovery strategies (e.g., high-value/high-probability accounts, low-engagement accounts, accounts requiring specialized intervention).

---

## 📈 5. Model Evaluation

Classification models were evaluated using Accuracy, Precision, Recall, F1-score, and ROC-AUC metrics. Model comparison focused on predictive performance, generalization capability, business usefulness, and interpretability.

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.82 | 0.79 | 0.76 | 0.77 | 0.85 |
| **Random Forest** | 0.88 | 0.86 | 0.83 | 0.84 | 0.91 |
| **XGBoost (Best Model)** | **0.91** | **0.89** | **0.87** | **0.88** | **0.94** |

---

## 🧠 Explainable AI

To improve transparency and trust, **SHAP (SHapley Additive exPlanations)** was implemented.

SHAP provides:
* **Global Explainability:** Understanding the most influential features and portfolio-level drivers of repayment behaviour.
* **Individual Account Explanations:** Understanding why an account received a specific prediction and which factors increased or decreased payment probability.

This enables collection managers to make informed decisions while maintaining human oversight.

---

## 🚀 Streamlit Application

A public Streamlit web application was developed to make the machine learning solution accessible to non-technical users.

🔗 **Live Application:** [Portfolio Risk & Debt Recovery System](https://portfolio-risk-debt-recovery-optimization-system-hwvhqiyk9nt5e.streamlit.app/)

### Application Features
* 📊 **Executive Dashboard:** Portfolio overview, active account distribution, outstanding balance insights, and recovery opportunity analysis.
* 🎯 **Payment Propensity Predictor:** Input account characteristics, generate payment likelihood predictions, and identify promising recovery opportunities.
* 👥 **Collector Resource Allocator:** Generates a prioritized account queue based on predicted payment probability, account characteristics, and recovery potential.
* 🔍 **Explainability Dashboard:** Displays SHAP visualizations showing key prediction drivers, feature contribution, and model reasoning.

---

## 📁 Repository Structure

```text
portfolio-risk-debt-recovery-optimization/
│
├── data/
│   └── active_portfolio.xlsx
│
├── notebooks/
│   └── portfolio_risk_analysis.ipynb
│
├── models/
│   ├── xgboost_model.pkl
│   └── scaler.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
🛠️ Technology Stack
Programming Language: Python 3.x

Data Processing: pandas, numpy

Visualization: matplotlib, seaborn

Machine Learning: scikit-learn, xgboost

Explainable AI: shap

Deployment: streamlit

Model Persistence: joblib

💻 Local Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/portfolio-risk-debt-recovery-optimization.git](https://github.com/YOUR_USERNAME/portfolio-risk-debt-recovery-optimization.git)
cd portfolio-risk-debt-recovery-optimization
Create a virtual environment:

Bash
python -m venv venv
Activate environment:

Windows:

Bash
venv\Scripts\activate
Mac/Linux:

Bash
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Run Streamlit:

Bash
streamlit run app.py
🔮 Future Enhancements
[ ] Real-time prediction API using FastAPI

[ ] Integration with CRM and collection platforms

[ ] Automated collector assignment optimization

[ ] Model monitoring and drift detection

[ ] Continuous model retraining pipelines

⚠️ Disclaimer
This project is developed for educational and portfolio demonstration purposes. Any sensitive customer information should be anonymized before deployment in a production environment.

👩🏽‍💻 Author
Charity Nduati

Data Science & Portfolio Analytics Professional

Specializing in:

Machine Learning

Financial Analytics

Predictive Modeling

Portfolio Risk Analysis

Business Intelligence

📧 Email: charitynduati17@gmail.com

💼 LinkedIn: [YOUR_LINKEDIN_URL]

🐙 GitHub: [YOUR_GITHUB_URL]
