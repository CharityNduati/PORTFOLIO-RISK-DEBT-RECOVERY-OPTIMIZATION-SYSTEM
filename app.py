import streamlit as st
import pandas as pd
import numpy as np
import datetime
import io

# Page Config
st.set_page_config(
    page_title="Enterprise Debt Recovery & Intelligence Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for World-Class UI
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .status-card { padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MOCK DATA IN-MEMORY STORAGE (Simulating DB / Active Portfolio)
# ---------------------------------------------------------
@st.cache_data
def load_portfolio():
    return pd.DataFrame({
        "Account ID": ["ACC-1001", "ACC-1002", "ACC-1003", "ACC-1004"],
        "Debtor Name": ["John Doe", "Jane Smith", "Michael Johnson", "Sarah Connor"],
        "Institution": ["Bank A", "Microfinance B", "Bank A", "Telecom C"],
        "Phone": ["+254712345678", "+254723456789", "+254734567890", "+254745678901"],
        "Email": ["john@example.com", "jane@example.com", "michael@example.com", "sarah@example.com"],
        "Outsourced Amount (KES)": [150000, 45000, 320000, 12000],
        "DPD": [45, 120, 15, 90],
        "Risk Rating": ["High Profile", "Standard", "High Profile", "Failing Account"],
        "Optimal Call Time": ["09:00 AM - 11:00 AM", "02:00 PM - 04:00 PM", "10:00 AM - 12:00 PM", "08:00 AM - 09:30 AM"],
        "Last Action": ["Ringing No Response", "PTP Agreed", "Skip Traced", "Call Failed"]
    })

df_portfolio = load_portfolio()

# ---------------------------------------------------------
# SIDEBAR NAVIGATION & HIGH-PRIORITY ALERTS
# ---------------------------------------------------------
st.sidebar.title("🛡️ Recovery Ops Hub")
st.sidebar.caption("AI-Powered Collection Engine")

page = st.sidebar.radio("Module Selection", [
    "📌 Executive Overview & Alerts",
    "🎯 Skip Tracing & Debtor Profile",
    "📞 Smart Call & Auto Notes",
    "✉️ Automated Comms (SMS / WhatsApp / Email)",
    "⏰ Optimal Call Timing & Predictions",
    "📄 Debt Cards & Export"
])

st.sidebar.markdown("---")
st.sidebar.subheader("🚨 Priority Reminders")
st.sidebar.warning("⚠️ **3 High-Profile Debtors** pending follow-up today.")
st.sidebar.error("🔴 **Microfinance B**: Recovery target falling below threshold (<40%).")

# ---------------------------------------------------------
# 1. EXECUTIVE OVERVIEW & ALERTS
# ---------------------------------------------------------
if page == "📌 Executive Overview & Alerts":
    st.title("📌 Executive Overview & High-Priority Alerts")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Active Accounts", f"{len(df_portfolio):,}")
    col2.metric("Portfolio Exposure", "KES 527,000")
    col3.metric("Auto-Messages Sent Today", "142")
    col4.metric("Avg. PTP Adherence", "68.4%")
    
    st.markdown("---")
    st.subheader("🔥 High-Risk Institution & Debtor Alerts")
    
    c1, c2 = st.columns(2)
    with c1:
        st.error("### 🔴 Failing Client Institutions")
        st.write("**Microfinance B** — Recovery rate down by 18% this month. Recommended: Re-allocate collectors or trigger bulk digital campaigns.")
        st.button("Trigger Recovery Campaign for Microfinance B")

    with c2:
        st.warning("### ⚡ High-Profile Debtors Escalation")
        st.dataframe(df_portfolio[df_portfolio["Risk Rating"] == "High Profile"][["Account ID", "Debtor Name", "Outsourced Amount (KES)", "DPD"]])

# ---------------------------------------------------------
# 2. SKIP TRACING & DEBTOR PROFILE
# ---------------------------------------------------------
elif page == "🎯 Skip Tracing & Debtor Profile":
    st.title("🎯 AI-Powered Skip Tracing")
    st.markdown("Trace hard-to-find debtors by aggregating public, social, and network metadata.")

    selected_acc = st.selectbox("Select Account for Skip Tracing", df_portfolio["Account ID"] + " - " + df_portfolio["Debtor Name"])
    acc_id = selected_acc.split(" - ")[0]
    debtor = df_portfolio[df_portfolio["Account ID"] == acc_id].iloc[0]

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Current Info")
        st.write(f"**Name:** {debtor['Debtor Name']}")
        st.write(f"**Primary Phone:** {debtor['Phone']}")
        st.write(f"**Email:** {debtor['Email']}")
        st.write(f"**Amount Due:** KES {debtor['Outsourced Amount (KES)']:,}")
        
    with col2:
        st.subheader("Traced Intelligence Signals")
        if st.button("🔍 Run Deep Skip Trace"):
            st.success("Skip Trace Complete! Found 3 secondary contacts.")
            st.json({
                "Secondary Phone": "+254701998877 (Verified via Mobile Money Logs)",
                "Alternative Email": "j.doe_work@company.co.ke",
                "Employer Verification": "Active — Tech Firm, Westlands, Nairobi",
                "Social Footprint": "LinkedIn Profile Active (Updated 3 days ago)"
            })

# ---------------------------------------------------------
# 3. SMART CALL & AUTO-NOTES
# ---------------------------------------------------------
elif page == "📞 Smart Call & Auto Notes":
    st.title("📞 Smart Call Center & Auto-Documentation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Debtor Interaction")
        acc = st.selectbox("Select Debtor", df_portfolio["Account ID"] + " - " + df_portfolio["Debtor Name"], key="call_debtor")
        call_status = st.selectbox("Call Outcome / Status", [
            "Ringing No Response",
            "Promised to Pay (PTP)",
            "Disputed Debt",
            "Refused to Pay",
            "Call Failed / Out of Service"
        ])
        
        call_duration = st.number_input("Call Duration (seconds)", min_value=0, value=120)
        ptp_amount = st.number_input("PTP Amount (if applicable)", min_value=0, value=0)
        ptp_date = st.date_input("PTP Date", datetime.date.today() + datetime.timedelta(days=3))
        
        manual_notes = st.text_area("Agent Raw Notes", "Debtor claims salary was delayed. Agreed to clear half on PTP date.")

    with col2:
        st.subheader("🤖 AI Auto-Generated Documentation")
        if st.button("Generate Auto-Note & Save Log"):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            auto_note = f"[{timestamp}] OUTCOME: {call_status} | DURATION: {call_duration}s | PTP: KES {ptp_amount} for {ptp_date}. SUMMARY: {manual_notes}"
            
            st.info("System Note Recorded:")
            st.code(auto_note)
            st.success("✅ Interaction saved to database automatically!")

    st.markdown("---")
    st.subheader("📊 Call Time & Payment History")
    
    tab1, tab2 = st.tabs(["Payment History", "Call Log History"])
    with tab1:
        st.table(pd.DataFrame({
            "Date": ["2026-05-10", "2026-06-12", "2026-07-01"],
            "Amount Paid (KES)": [5000, 10000, 15000],
            "Channel": ["M-Pesa", "Bank Transfer", "M-Pesa"],
            "Receipt Ref": ["QX8921JK", "FT202612", "QX9910LL"]
        }))
    with tab2:
        st.table(pd.DataFrame({
            "Timestamp": ["2026-07-28 10:15 AM", "2026-07-30 02:30 PM", "2026-08-01 09:10 AM"],
            "Agent": ["Charity N.", "System Auto-Dialer", "Charity N."],
            "Status": ["Ringing No Response", "PTP Agreed", "Ringing No Response"],
            "Duration": ["45s", "180s", "30s"]
        }))

# ---------------------------------------------------------
# 4. AUTOMATED COMMS (SMS / WHATSAPP / EMAIL)
# ---------------------------------------------------------
elif page == "✉️ Automated Comms (SMS / WhatsApp / Email)":
    st.title("✉️ Automated Triggered Communications")
    st.markdown("Dispatch auto-messages based on call status or send bulk outreach.")

    tab1, tab2 = st.tabs(["Auto Trigger Post-Call", "Bulk WhatsApp & Email Dispatcher"])

    with tab1:
        st.subheader("Auto-Dispatch based on Status")
        status = st.selectbox("Select Call Status Event", ["Ringing No Response", "PTP Agreed", "Disputed Debt"])
        
        if status == "Ringing No Response":
            template = "Hello {Name}, we tried calling you regarding your outstanding balance with {Client}. Please reach us at +254700000000 to resolve this."
        elif status == "PTP Agreed":
            template = "Dear {Name}, thank you for agreeing to pay KES {Amount} by {Date}. Paybill: 123456, Account: {AccID}."
        else:
            template = "Dear {Name}, your dispute regarding {AccID} has been logged. Our risk team will inspect it shortly."

        st.text_area("Template Preview", template)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("💬 Send Auto WhatsApp"):
                st.success("WhatsApp triggered via API!")
        with col_b:
            if st.button("📱 Send Auto SMS"):
                st.success("SMS sent via SMS Gateway!")

    with tab2:
        st.subheader("Bulk Communications Engine")
        target_group = st.multiselect("Select Target Segment", ["High Profile Debtors", "DPD > 90 Days", "Failing Client Institutions"], default=["High Profile Debtors"])
        msg_type = st.radio("Channel", ["WhatsApp", "Email", "SMS"], horizontal=True)
        
        st.text_area("Bulk Message Body", "Urgent notice: Your account requires immediate resolution. Click here to view payment plan options.")
        
        if st.button("🚀 Execute Bulk Dispatch"):
            st.balloons()
            st.success(f"Bulk {msg_type} dispatched successfully to selected segment!")

# ---------------------------------------------------------
# 5. OPTIMAL CALL TIMING & PREDICTIONS
# ---------------------------------------------------------
elif page == "⏰ Optimal Call Timing & Predictions":
    st.title("⏰ Predictive Call Timing Engine")
    st.markdown("Machine learning algorithms predicting the best time to reach debtors based on historic pick-up rates.")

    st.subheader("Debtor-Level Best Time to Call")
    st.dataframe(df_portfolio[["Account ID", "Debtor Name", "Institution", "DPD", "Optimal Call Time"]])

    st.markdown("---")
    st.subheader("🏛️ Client Institution Peak Reachability")
    st.markdown("Predicting best collection windows by client type:")
    
    inst_timing = pd.DataFrame({
        "Client Institution Category": ["Commercial Banks", "Microfinance Institutions", "Telecom & Utility", "Sacco / Cooperatives"],
        "Best Call Window": ["08:30 AM - 10:30 AM", "01:30 PM - 03:30 PM", "05:00 PM - 07:00 PM", "09:00 AM - 11:30 AM"],
        "Highest Conversion Day": ["Tuesday", "Thursday", "Friday", "Monday"],
        "Historical Pick-up Rate": ["74%", "62%", "81%", "69%"]
    })
    st.table(inst_timing)

# ---------------------------------------------------------
# 6. DEBT CARDS & EXPORT
# ---------------------------------------------------------
elif page == "📄 Debt Cards & Export":
    st.title("📄 Debtor Cards & Portable Reports")
    
    selected_card = st.selectbox("Select Account Card to Generate", df_portfolio["Account ID"] + " - " + df_portfolio["Debtor Name"])
    acc_id = selected_card.split(" - ")[0]
    debtor = df_portfolio[df_portfolio["Account ID"] == acc_id].iloc[0]

    # Render Card View
    st.markdown(f"""
    <div style="border: 2px solid #004b87; padding: 25px; border-radius: 12px; background-color: #ffffff;">
        <h2 style="color: #004b87; margin-top: 0;">DEBTOR ACCOUNT CARD</h2>
        <hr>
        <p><b>Account ID:</b> {debtor['Account ID']} | <b>Institution:</b> {debtor['Institution']}</p>
        <p><b>Debtor Name:</b> {debtor['Debtor Name']}</p>
        <p><b>Contact Phone:</b> {debtor['Phone']} | <b>Email:</b> {debtor['Email']}</p>
        <p><b>Outsourced Amount:</b> KES {debtor['Outsourced Amount (KES)']:,}</p>
        <p><b>Days Past Due (DPD):</b> {debtor['DPD']} days</p>
        <p><b>Risk Profile:</b> {debtor['Risk Rating']}</p>
        <p><b>Recommended Call Window:</b> {debtor['Optimal Call Time']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Convert card data to downloadable CSV / Text file
    card_data = f"""DEBTOR ACCOUNT CARD
---------------------------------------
Account ID: {debtor['Account ID']}
Institution: {debtor['Institution']}
Debtor Name: {debtor['Debtor Name']}
Contact Phone: {debtor['Phone']}
Email: {debtor['Email']}
Outsourced Amount: KES {debtor['Outsourced Amount (KES)']}
Days Past Due: {debtor['DPD']}
Risk Profile: {debtor['Risk Rating']}
Optimal Call Window: {debtor['Optimal Call Time']}
---------------------------------------
Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    st.download_button(
        label="📥 Download Debt Card (TXT)",
        data=card_data,
        file_name=f"debt_card_{acc_id}.txt",
        mime="text/plain"
    )

# ---------------------------------------------------------
# FOOTER (Unindented at the end of script)
# ---------------------------------------------------------
st.markdown("""
<br><hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(0,0,0,0), rgba(0,75,135,0.75), rgba(0,0,0,0));">
<div style="text-align: center; padding: 10px; color: #6c757d; font-size: 0.88rem;">
    <p style="margin: 0; font-weight: 600; color: #004b87;">
        🛡️ Enterprise Debt Recovery & Operations Platform
    </p>
    <p style="margin: 4px 0 0 0;">
        Powered by AI Predictive Analytics & CRISP-DM Framework &bull; Real-time Portfolio Risk Engine
    </p>
    <p style="margin: 4px 0 0 0; font-size: 0.78rem; opacity: 0.8;">
        © 2026 Portfolio Analytics System. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)
