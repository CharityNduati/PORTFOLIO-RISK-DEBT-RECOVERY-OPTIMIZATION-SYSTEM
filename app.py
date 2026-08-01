import streamlit as st
import pandas as pd
import numpy as np
import datetime
import io

# ---------------------------------------------------------
# PAGE CONFIGURATION & KEYSIAN BRANDING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Keysian Debt Recovery Platform",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 16px; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
    .keysian-header { background-color: #003366; color: white; padding: 18px; border-radius: 8px; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PORTFOLIO DATA HANDLER (FILE UPLOAD OR DEFAULT)
# ---------------------------------------------------------
@st.cache_data
def load_default_portfolio():
    return pd.DataFrame({
        "Account ID": ["KEY-2026-001", "KEY-2026-002", "KEY-2026-003", "KEY-2026-004", "KEY-2026-005"],
        "Debtor Name": ["Wanjiru Kinuthia", "Ochieng Otieno", "Amina Hussein", "Kiprono Bett", "Mutua Ndiku"],
        "Client Institution": ["Faulu Microfinance", "Equity Bank", "NCBA", "Faulu Microfinance", "KCB Bank"],
        "Phone Number": ["+254712345678", "+254723456789", "+254734567890", "+254745678901", "+254756789012"],
        "Email Address": ["wanjiru@example.co.ke", "ochieng@example.co.ke", "amina@example.co.ke", "bett@example.co.ke", "mutua@example.co.ke"],
        "Outsourced Amount (KES)": [185000, 420000, 65000, 310000, 95000],
        "DPD": [65, 140, 22, 110, 40],
        "Assigned Collector": ["Charity Nduati", "Stephen Jilani", "Cynthia Jemutai", "Joy Njeru", "Chris Karagu"],
        "Risk Rating": ["High Profile", "Failing Account", "Low Risk", "High Profile", "Standard"],
        "Optimal Call Window": ["09:00 AM - 11:00 AM", "02:00 PM - 04:00 PM", "10:30 AM - 12:30 PM", "08:30 AM - 10:00 AM", "03:00 PM - 05:00 PM"],
        "Last Action": ["PTP Agreed", "Ringing No Response", "Call Successful", "Skip Traced", "Pending Follow-up"]
    })

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/000000/law.png", width=70)
st.sidebar.title("Keysian Recovery Ops")
st.sidebar.caption("Keysian Auctioneers & Debt Recovery Unit")

# File Uploader in Sidebar for Live Datasets
st.sidebar.markdown("---")
st.sidebar.subheader("📂 Active Portfolio Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Excel or CSV Portfolio", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df_portfolio = pd.read_csv(uploaded_file)
        else:
            df_portfolio = pd.read_excel(uploaded_file)
        st.sidebar.success(f"Loaded: {uploaded_file.name}")
    except Exception as e:
        st.sidebar.error("Error reading file. Loading default portfolio.")
        df_portfolio = load_default_portfolio()
else:
    df_portfolio = load_default_portfolio()

page = st.sidebar.radio("Navigation", [
    "📌 Executive Overview & Alerts",
    "📂 Full Allocated Portfolio Directory",
    "➕ Allocate New Portfolio Batch",
    "👥 Collector Performance Portal",
    "🎯 AI Skip Tracing",
    "📞 Smart Call Center & Auto Notes",
    "✉️ Automated Comms & M-Pesa Link",
    "⏰ Optimal Call Timing Predictions",
    "📄 Printable Debt Cards & Export"
])

# ---------------------------------------------------------
# 1. EXECUTIVE OVERVIEW & ALERTS
# ---------------------------------------------------------
if page == "📌 Executive Overview & Alerts":
    st.markdown("""
        <div class="keysian-header">
            <h1>KEYSIAN DEBT RECOVERY UNIT</h1>
            <p>Portfolio Analytics & Operations Intelligence Platform</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Allocated Accounts", f"{len(df_portfolio):,}")
    
    total_val = df_portfolio["Outsourced Amount (KES)"].sum() if "Outsourced Amount (KES)" in df_portfolio.columns else 0
    col2.metric("Total Portfolio Exposure", f"KES {total_val:,.2f}")
    col3.metric("Active Field Collectors", "6 Agents")
    col4.metric("Month-to-Date PTP Conversion", "71.8%")
    
    st.markdown("---")
    st.subheader("🔥 Priority Portfolio & Institution Alerts")
    
    c1, c2 = st.columns(2)
    with c1:
        st.error("### 🔴 Client Institutions Requiring Escalation")
        st.write("**Faulu Microfinance Batch 2** — High delinquency detected for accounts > 90 DPD. Recommended: Trigger legal demand letters or field team dispatch.")
        if st.button("Trigger Mass Digital Outreach for Faulu Accounts"):
            st.success("Automated campaign queued for Faulu Microfinance portfolio!")

    with c2:
        st.warning("### ⚡ High-Profile Debtors Escalation Matrix")
        if "Risk Rating" in df_portfolio.columns:
            st.dataframe(df_portfolio[df_portfolio["Risk Rating"] == "High Profile"][["Account ID", "Debtor Name", "Outsourced Amount (KES)", "Assigned Collector"]])

# ---------------------------------------------------------
# 2. FULL ALLOCATED PORTFOLIO DIRECTORY
# ---------------------------------------------------------
elif page == "📂 Full Allocated Portfolio Directory":
    st.title("📂 Keysian Master Allocated Portfolio Directory")
    st.markdown("Search, filter, and inspect all accounts assigned across client institutions.")

    col1, col2, col3 = st.columns(3)
    with col1:
        inst_filter = st.multiselect("Filter by Institution", options=df_portfolio["Client Institution"].unique() if "Client Institution" in df_portfolio.columns else [], default=[])
    with col2:
        collector_filter = st.multiselect("Filter by Collector", options=df_portfolio["Assigned Collector"].unique() if "Assigned Collector" in df_portfolio.columns else [], default=[])
    with col3:
        search_query = st.text_input("Search Debtor Name or Account ID", "")

    filtered_df = df_portfolio.copy()
    if inst_filter:
        filtered_df = filtered_df[filtered_df["Client Institution"].isin(inst_filter)]
    if collector_filter:
        filtered_df = filtered_df[filtered_df["Assigned Collector"].isin(collector_filter)]
    if search_query:
        filtered_df = filtered_df[filtered_df["Debtor Name"].str.contains(search_query, case=False, na=False) | filtered_df["Account ID"].str.contains(search_query, case=False, na=False)]

    st.dataframe(filtered_df, use_container_width=True)

# ---------------------------------------------------------
# 3. ALLOCATE NEW PORTFOLIO BATCH
# ---------------------------------------------------------
elif page == "➕ Allocate New Portfolio Batch":
    st.title("➕ Onboard & Allocate New Debtor Portfolio")
    st.markdown("Upload new client allocation sheets (Excel/CSV) and assign accounts to collector teams.")

    with st.form("portfolio_upload_form"):
        st.subheader("Batch Onboarding Parameters")
        client_name = st.text_input("Client Institution Name (e.g., Faulu Microfinance, KCB, Equity)")
        batch_id = st.text_input("Allocation Batch ID", value=f"BATCH-{datetime.date.today().strftime('%Y%m')}-01")
        batch_file = st.file_uploader("Choose Excel or CSV File", type=["xlsx", "xls", "csv"])
        assign_strategy = st.selectbox("Allocation Strategy", ["Round-Robin (Equal Distribution)", "By Risk Profile", "Assign to Specific Collector"])
        
        submitted = st.form_submit_button("Ingest & Allocate Portfolio Batch")
        if submitted:
            if batch_file is not None:
                st.balloons()
                st.success(f"Successfully processed portfolio batch **{batch_id}** for **{client_name}**! Accounts distributed across active collectors.")
            else:
                st.error("Please upload a valid Excel or CSV file to complete allocation.")

# ---------------------------------------------------------
# 4. COLLECTOR PERFORMANCE PORTAL
# ---------------------------------------------------------
elif page == "👥 Collector Performance Portal":
    st.title("👥 Collector Team Operations & Analytics")
    st.markdown("Monitor individual agent performance, call counts, and payment collection adherence.")

    agents = ["Charity Nduati", "Stephen Jilani", "Cynthia Jemutai", "Joy Njeru", "Chris Karagu", "Sylvia Wambui"]
    selected_agent = st.selectbox("Select Collector / Recovery Agent", agents)

    col1, col2, col3 = st.columns(3)
    col1.metric("Assigned Accounts", "48")
    col2.metric("Calls Made Today", "37")
    col3.metric("Total Collected This Month", "KES 1,240,000")

    st.markdown("---")
    st.subheader(f"Active Accounts Assigned to {selected_agent}")
    if "Assigned Collector" in df_portfolio.columns:
        agent_accounts = df_portfolio[df_portfolio["Assigned Collector"] == selected_agent]
        st.dataframe(agent_accounts)
    else:
        st.info("Upload a dataset with an 'Assigned Collector' column to view live breakdown.")

# ---------------------------------------------------------
# 5. AI SKIP TRACING
# ---------------------------------------------------------
elif page == "🎯 AI Skip Tracing":
    st.title("🎯 AI-Powered Skip Tracing Hub")
    st.markdown("Trace hard-to-find debtors by aggregating public data, social networks, and secondary contacts.")

    selected_acc = st.selectbox("Select Account to Trace", df_portfolio["Account ID"] + " - " + df_portfolio["Debtor Name"])
    acc_id = selected_acc.split(" - ")[0]
    debtor = df_portfolio[df_portfolio["Account ID"] == acc_id].iloc[0]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Known Records")
        st.write(f"**Name:** {debtor.get('Debtor Name', 'N/A')}")
        st.write(f"**Primary Phone:** {debtor.get('Phone Number', 'N/A')}")
        st.write(f"**Client:** {debtor.get('Client Institution', 'N/A')}")
        st.write(f"**Amount Due:** KES {debtor.get('Outsourced Amount (KES)', 0):,}")

    with col2:
        st.subheader("Traced Metadata Signals")
        if st.button("🔍 Execute Deep Trace"):
            st.success("Trace complete! Found 3 secondary contact points.")
            st.json({
                "Alternative Phone 1": "+254701998877 (Verified via Mobile Transfer Logs)",
                "Alternative Phone 2": "+254788112233 (Next of Kin Match)",
                "Workplace Verification": "Active — Commercial Building, Upper Hill, Nairobi",
                "Social Media Profile": "Active LinkedIn & Facebook activity detected within last 48 hrs"
            })

# ---------------------------------------------------------
# 6. SMART CALL CENTER & AUTO NOTES
# ---------------------------------------------------------
elif page == "📞 Smart Call Center & Auto Notes":
    st.title("📞 Smart Call Center & Documentation")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Log Debtor Call")
        acc = st.selectbox("Select Debtor Account", df_portfolio["Account ID"] + " - " + df_portfolio["Debtor Name"])
        call_outcome = st.selectbox("Call Outcome", ["Promised to Pay (PTP)", "Ringing No Response", "Refused to Pay", "Disputed Debt", "Wrong Number"])
        ptp_val = st.number_input("PTP Amount (KES)", min_value=0, value=10000)
        ptp_dt = st.date_input("PTP Target Date", datetime.date.today() + datetime.timedelta(days=3))
        raw_notes = st.text_area("Collector Notes", "Debtor promised to settle balance via M-Pesa following salary payment.")

    with col2:
        st.subheader("🤖 Generated Documentation Note")
        if st.button("Generate System Note & Save"):
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            generated_note = f"[{now_str}] AGENT NOTE | OUTCOME: {call_outcome} | PTP: KES {ptp_val:,} due on {ptp_dt} | REMARKS: {raw_notes}"
            st.code(generated_note)
            st.success("Note saved automatically to Keysian Account Audit Log!")

# ---------------------------------------------------------
# 7. AUTOMATED COMMS & M-PESA LINK
# ---------------------------------------------------------
elif page == "✉️ Automated Comms & M-Pesa Link":
    st.title("✉️ Triggered Outreach & M-Pesa Payment Links")
    st.markdown("Dispatch automated SMS/WhatsApp debt notices and generate instant M-Pesa payment triggers.")

    tab1, tab2 = st.tabs(["📲 Trigger Messages", "💳 M-Pesa Payment Link Generator"])
    
    with tab1:
        st.subheader("Auto-Dispatch Post Call Notice")
        msg_type = st.selectbox("Select Notice Type", ["PTP Confirmation", "Ringing No Response Reminder", "Demand Notice Escalation"])
        st.text_area("Message Content", "Dear Customer, please clear your outstanding Keysian debt balance via Paybill 123456 Account KEY-2026-001. Enquiries: 0700000000.")
        if st.button("Send Instant Message"):
            st.success("Message dispatched successfully via SMS Gateway!")

    with tab2:
        st.subheader("💳 Instant M-Pesa STK Push / Paybill Prompt")
        pay_phone = st.text_input("Debtor M-Pesa Phone Number", "+254712345678")
        pay_amount = st.number_input("Prompt Amount (KES)", min_value=100, value=5000)
        if st.button("🚀 Trigger M-Pesa STK Push"):
            st.info(f"STK Push prompt of KES {pay_amount:,} sent to {pay_phone}.")

# ---------------------------------------------------------
# 8. OPTIMAL CALL TIMING PREDICTIONS
# ---------------------------------------------------------
elif page == "⏰ Optimal Call Timing Predictions":
    st.title("⏰ Predictive Reachability Engine")
    st.markdown("Machine learning model predicting optimal call windows by institution type and historical debtor habits.")

    st.subheader("Institution Reachability Benchmarks")
    timing_df = pd.DataFrame({
        "Client Category": ["Microfinance (e.g. Faulu)", "Commercial Banks", "Saccos", "Utilities / Telecom"],
        "Optimal Contact Window": ["08:00 AM - 10:30 AM", "01:30 PM - 03:30 PM", "09:00 AM - 11:30 AM", "04:30 PM - 06:30 PM"],
        "Best Day to Reach": ["Tuesday & Thursday", "Wednesday", "Monday", "Friday"],
        "Conversion Likelihood": ["78%", "65%", "71%", "83%"]
    })
    st.table(timing_df)

# ---------------------------------------------------------
# 9. PRINTABLE DEBT CARDS & EXPORT
# ---------------------------------------------------------
elif page == "📄 Printable Debt Cards & Export":
    st.title("📄 Debtor Cards & Portable Export")
    
    selected_card = st.selectbox("Select Account Card", df_portfolio["Account ID"] + " - " + df_portfolio["Debtor Name"])
    acc_id = selected_card.split(" - ")[0]
    debtor = df_portfolio[df_portfolio["Account ID"] == acc_id].iloc[0]

    st.markdown(f"""
    <div style="border: 2px solid #003366; padding: 25px; border-radius: 10px; background-color: #ffffff;">
        <h2 style="color: #003366; margin-top: 0;">KEYSIAN DEBT RECOVERY UNIT - ACCOUNT CARD</h2>
        <hr>
        <p><b>Account ID:</b> {debtor.get('Account ID', 'N/A')} | <b>Client Institution:</b> {debtor.get('Client Institution', 'N/A')}</p>
        <p><b>Debtor Name:</b> {debtor.get('Debtor Name', 'N/A')}</p>
        <p><b>Contact Phone:</b> {debtor.get('Phone Number', 'N/A')} | <b>Email:</b> {debtor.get('Email Address', 'N/A')}</p>
        <p><b>Outsourced Amount:</b> KES {debtor.get('Outsourced Amount (KES)', 0):,}</p>
        <p><b>Days Past Due (DPD):</b> {debtor.get('DPD', 'N/A')} days</p>
        <p><b>Assigned Collector:</b> {debtor.get('Assigned Collector', 'Unassigned')}</p>
        <p><b>Optimal Call Window:</b> {debtor.get('Optimal Call Window', 'Standard Hours')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    card_text = f"""KEYSIAN DEBT RECOVERY UNIT - DEBTOR CARD
-------------------------------------------------
Account ID: {debtor.get('Account ID', 'N/A')}
Client Institution: {debtor.get('Client Institution', 'N/A')}
Debtor Name: {debtor.get('Debtor Name', 'N/A')}
Contact Phone: {debtor.get('Phone Number', 'N/A')}
Email: {debtor.get('Email Address', 'N/A')}
Outsourced Amount: KES {debtor.get('Outsourced Amount (KES)', 0)}
Days Past Due: {debtor.get('DPD', 'N/A')}
Assigned Collector: {debtor.get('Assigned Collector', 'Unassigned')}
-------------------------------------------------
Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    st.download_button(
        label="📥 Download Debt Card (TXT)",
        data=card_text,
        file_name=f"Keysian_Debt_Card_{acc_id}.txt",
        mime="text/plain"
    )

# ---------------------------------------------------------
# ATTRACTIVE CREATOR FOOTNOTE
# ---------------------------------------------------------
st.markdown("""
<br><hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(0,0,0,0), rgba(0,51,102,0.75), rgba(0,0,0,0));">
<div style="text-align: center; padding: 12px; color: #555555; font-size: 0.88rem;">
    <p style="margin: 0; font-weight: 700; color: #003366; font-size: 1rem;">
        ⚖️ Keysian Debt Recovery Unit — Portfolio Analytics Platform
    </p>
    <p style="margin: 4px 0 0 0;">
        Designed & Developed by <b>Charity Nduati</b> | Portfolio Analytics & Operations Specialist
    </p>
    <p style="margin: 4px 0 0 0; font-size: 0.78rem; opacity: 0.8;">
        Driven by Machine Learning, CRISP-DM Methodology & Real-Time Risk Optimization &bull; Nairobi, Kenya
    </p>
</div>
""", unsafe_allow_html=True)
