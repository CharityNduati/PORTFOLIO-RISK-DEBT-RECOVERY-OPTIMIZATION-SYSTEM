────────────────────────────────────────────────────  │
│  High-Propensity Priority Queue Generated Successfully.                 │
└─────────────────────────────────────────────────────────────────────────┘


* **Executive Dashboard:** Macro view of portfolio balances, active account distributions, and potential recoverable value[cite: 1].
* **Propensity Scoring Engine:** Interactive interface to predict payment likelihood for individual delinquent accounts[cite: 1].
* **Collector Resource Allocator:** Filterable queue prioritizing daily collector tasks based on predicted payment probability[cite: 1].
* **Explainability Dashboard:** Interactive SHAP feature attribution graphs showing exactly why an account was scored high or low risk[cite: 1].

---

## 📁 Repository Structure

```text
├── data/
│   └── active_portfolio.xlsx          # Raw active debt portfolio dataset
├── notebooks/
│   └── portfolio_risk_analysis.ipynb  # Complete EDA, feature engineering, modeling & SHAP notebook
├── models/
│   ├── xgboost_model.pkl              # Trained XGBoost classification model
│   └── scaler.pkl                     # Standard scaler transformer object
├── app.py                             # Streamlit web application source code
├── requirements.txt                   # Python dependencies and library versions
└── README.md                          # Project documentation
🛠️ Tech Stack & Libraries
Language: Python 3.x[cite: 1]

Data Processing: pandas, numpy

[cite: 1]

Visualization: matplotlib, seaborn

[cite: 1]

Machine Learning: scikit-learn, xgboost

[cite: 1]

Explainable AI: shap

[cite: 1]

Web Framework: Streamlit[cite: 1]

🚀 Local Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/your-username/portfolio-risk-debt-recovery-optimization.git](https://github.com/your-username/portfolio-risk-debt-recovery-optimization.git)
cd portfolio-risk-debt-recovery-optimization
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages:

Bash
pip install -r requirements.txt
Launch the Streamlit app locally:

Bash
streamlit run app.py
🔮 Future Enhancements
[ ] Real-time Scoring API: Package model endpoints using FastAPI for direct integration into enterprise collection software.

[ ] Automated Collector Assignment: Implement optimization algorithms to auto-assign top-tier accounts to high-performing recovery agents.

[ ] CRM Integration: Sync outputs with platforms like Salesforce or custom dialer systems.

[ ] Model Monitoring & Retraining: Setup automated data drift tracking and quarterly model retraining pipelines.

👤 Author
Charity Nduati

Data Science & Portfolio Analytics Professional


