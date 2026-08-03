# 📈 Portfolio Intelligence & Predictive Debt Recovery Analytics

[![Methodology](https://img.shields.io/badge/Methodology-CRISP--DM-orange.svg)](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](#-interactive-streamlit-application)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

---

## 📌 Project Overview

Debt recovery agents manage thousands of delinquent accounts across multiple clients. Traditional collection approaches typically rely on manual prioritization, static reports, and collector intuition. 

This project develops an end-to-end **machine learning-powered debt recovery analytics system** that transforms traditional collection operations into a data-driven decision support framework. 

The solution predicts debtor payment propensity, segments portfolio risk profiles, prioritizes collector activities, integrates **SHAP (SHapley Additive exPlanations)** for explainability, and deploys everything into an interactive **Streamlit web application** designed for business users and collection managers.

---

## 🎯 Business Context & Problem Statement

* **The Portfolio:** Manages **2,700+ outsourced accounts** representing a high-value portfolio.
* **The Challenge:** Traditional manual prioritization leads to inefficient collector time allocation, delayed recoveries, low engagement rates, and missed high-value opportunities.
* **The Objective:** Leverage historical account data and machine learning to identify high-potential accounts, optimize collection resources, segment portfolios for targeted outreach, and provide transparent, actionable predictions through a user-friendly app.

---

## 🔄 CRISP-DM Methodology

This project follows the **CRISP-DM** framework:

[ Business Understanding ] ➔ [ Data Understanding ] ➔ [ Data Preparation ]
│
[ Deployment ] ⇦────────────── [ Evaluation ] ⇦───────────── [ Modeling ]


1. **Business Understanding:** Defined key performance drivers to improve collector productivity and increase recovery yields.
2. **Data Understanding:** Explored portfolio data across multiple variables covering client details, balances, Days Past Due (DPD), and contact metrics.
3. **Data Preparation:** Handled missing values, engineered recovery indicators (contactability ratios, balance tiers, temporal features), and prepared variables for modeling.
4. **Modeling:** Developed supervised classification models (Logistic Regression, Random Forest, **XGBoost**) and unsupervised clustering (**K-Means**) to group accounts and predict payment success.
5. **Evaluation:** Evaluated models using Accuracy, Precision, Recall, F1-score, and ROC-AUC. **XGBoost** emerged as the top performer with an **ROC-AUC of 0.94**.
6. **Deployment:** Deployed an interactive **Streamlit** web application to bridge the gap between machine learning insights and daily collection operations.

---

## 📊 Model Performance Summary

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.82 | 0.79 | 0.76 | 0.77 | 0.85 |
| Random Forest | 0.88 | 0.86 | 0.83 | 0.84 | 0.91 |
| **XGBoost (Best Model)** | **0.91** | **0.89** | **0.87** | **0.88** | **0.94** |

---

## 🚀 Interactive Streamlit Application

The interactive web application makes analytics and machine learning predictions accessible to operational teams without requiring any technical setup:

👉 **[Launch Live Streamlit Application](https://github.com/CharityNduati/PORTFOLIO-RISK-DEBT-RECOVERY-OPTIMIZATION-SYSTEM)**

### Key Application Features:
* **📊 Executive Dashboard:** Portfolio overview, active account distribution, outstanding balance insights, and recovery opportunity analysis.
* **🎯 Payment Propensity Predictor:** Input account characteristics to generate real-time payment likelihood scores.
* **👥 Collector Resource Allocator:** Generates a prioritized outreach queue based on recovery potential and risk profiles.
* **🔍 Explainability Dashboard:** Visualizes SHAP feature contributions to explain individual and portfolio-level predictions clearly.

---

## 📂 Repository Structure

```text
PORTFOLIO-RISK-DEBT-RECOVERY-OPTIMIZATION-SYSTEM/
│
├── active_portfolio - 2026-07-31...xlsx  # Outsourced active accounts dataset
├── Notebook.ipynb                         # Complete CRISP-DM analytical workflow notebook
├── app.py                                 # Streamlit web application entry point
├── portfolio_recovery_xgb_model.pkl       # Trained XGBoost classification artifact
├── portfolio_scaler.pkl                   # Fitted StandardScaler artifact
├── model_features.pkl                     # Saved model feature columns mapping
├── requirements.txt                       # Python package dependencies
└── README.md                              # Project documentation
🔮 Future Enhancements
[ ] Real-time prediction API integration using FastAPI.

[ ] Direct CRM and collection platform connectors.

[ ] Automated collector assignment optimization algorithms.

[ ] Model performance monitoring and data drift detection pipelines.

⚠️ Disclaimer
This project was developed for portfolio demonstration purposes. All sensitive customer information has been anonymized.

👩🏽‍💻 Author
Charity Nduati

Data Science & Portfolio Analytics Professional

Specializations: Machine Learning | Financial Analytics | Predictive Modeling | Portfolio Risk Analysis | Business Intelligence

Email: charitynduati17@gmail.com

LinkedIn: [Your LinkedIn URL]

GitHub: https://github.com/CharityNduati

