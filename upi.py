import streamlit as st
from datetime import datetime

st.set_page_config(page_title="UPI Pay • Demo", page_icon="💠", layout="centered")

# Simulation only. No real bank or payment-network connectivity.
if "balance" not in st.session_state:
    st.session_state.balance = 11050.00
if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {"name": "Ram Singh", "amount": 700.00, "kind": "Sent", "status": "Demo success", "time": "Today, 01:04 AM"},
        {"name": "KHUSHBOO", "amount": 299.90, "kind": "Received", "status": "Demo received", "time": "Yesterday, 07:24 PM"},
        {"name": "Sudeep Das Saha", "amount": 299.99, "kind": "Sent", "status": "Demo failed", "time": "Yesterday, 07:22 PM"},
    ]

st.markdown("""
<style>
:root { color-scheme: light; }
.stApp { background:#f4f7ff; }
[data-testid="stAppViewContainer"] { background:#f4f7ff; }
[data-testid="stHeader"] { background:transparent; }
.block-container { max-width:760px; padding:1.15rem 1rem 3rem; }
html, body, [class*="css"], p, label, h1, h2, h3, h4, span {
  color:#15213b !important;
}
h1,h2,h3 { letter-spacing:-.02em; }
.demo-pill {
  background:#e4efff; border:1px solid #c3d9ff; color:#124a9c !important;
  padding:12px 14px; border-radius:15px; font-weight:800; text-align:center;
  margin-bottom:16px;
}
.hero {
  background:linear-gradient(135deg,#175be8,#3988f6);
  border-radius:25px; padding:24px 22px; color:white !important;
  box-shadow:0 10px 28px #215fe52b; margin-bottom:18px;
}
.hero * { color:white !important; }
.hero h1 { font-size:2rem; margin:0; }
.hero p { margin:.35rem 0 0; opacity:.9; }
.profile {
  background:white; border:1px solid #e1eaff; border-radius:20px;
  padding:16px 18px; margin:12px 0 18px; box-shadow:0 4px 18px #244f9c0d;
}
.bankcard {
  background:linear-gradient(135deg,#ffffff,#eaf2ff);
  border:1px solid #d9e6ff; border-radius:22px; padding:20px;
  box-shadow:0 8px 22px #315eab18; margin-bottom:18px;
}
.bankcard .bank {font-size:1.05rem;font-weight:800;color:#174b98 !important;}
.bankcard .amount {font-size:2rem;font-weight:900;color:#13284d !important;}
.section { font-size:1.25rem;font-weight:850;margin:1.25rem 0 .7rem; }
.actionbox {
  background:white; border:1px solid #e1eaff; border-radius:18px;
  padding:12px 8px; text-align:center; box-shadow:0 4px 14px #244f9c0d;
}
.tx {
  background:white; border:1px solid #e5edff; border-radius:16px;
  padding:14px 16px; margin:8px 0; box-shadow:0 3px 12px #244f9c08;
}
.small { color:#65738d !important; font-size:.88rem; }
div.stButton > button, div.stFormSubmitButton > button {
  border-radius:13px; border:1px solid #d4e2ff; min-height:44px;
  background:#edf4ff; color:#124a9c !important; font-weight:700;
}
div.stFormSubmitButton > button {background:#175be8;color:white !important;border:0;}
[data-testid="stMetric"] {
  background:white;border:1px solid #e1eaff;border-radius:18px;
  padding:14px; box-shadow:0 4px 16px #244f9c0d;
}
[data-testid="stMetricLabel"], [data-testid="stMetricValue"] {color:#13284d !important;}
[data-testid="stVerticalBlockBorderWrapper"] {border-radius:18px;}
</style>
<div class="demo-pill">DEMO ONLY • NO REAL PAYMENTS OR BANK CONNECTION</div>
<div class="hero">
  <h1>💠 UPI Pay</h1>
  <p>Simple • Fast • Simulated</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="profile">
  <div style="font-size:1.15rem;font-weight:800">👤 Basit Abass</div>
  <div class="small">Demo profile</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="bankcard">
  <div class="bank">🏦 ICICI Bank • DEMO ACCOUNT</div>
  <div class="small">Account ending •••• 0456</div>
  <div style="margin-top:12px;font-size:.9rem;color:#65738d">Simulated available balance</div>
  <div class="amount">₹{st.session_state.balance:,.2f}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">Quick Actions</div>', unsafe_allow_html=True)
a, b, c = st.columns(3)
with a:
    st.markdown('<div class="actionbox">➤<br><b>Send</b></div>', unsafe_allow_html=True)
with b:
    st.markdown('<div class="actionbox">▦<br><b>Scan</b></div>', unsafe_allow_html=True)
with c:
    st.markdown('<div class="actionbox">↓<br><b>Receive</b></div>', unsafe_allow_html=True)
st.caption("Scan and receive actions are visual placeholders in this demo.")

st.markdown('<div class="section">Demo Transfer</div>', unsafe_allow_html=True)
with st.form("transfer_form"):
    recipient = st.text_input("Recipient name")
    amount = st.number_input("Amount (₹)", min_value=1.0, max_value=100000.0, step=1.0)
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Simulate transfer", use_container_width=True)

if submitted:
    if not recipient.strip():
        st.warning("Enter a recipient name to simulate a transfer.")
    elif amount > st.session_state.balance:
        st.error("Insufficient demo balance.")
    else:
        st.session_state.balance -= amount
        st.session_state.transactions.insert(0, {
            "name": recipient.strip(), "amount": amount, "kind": "Sent",
            "status": "Demo success", "time": datetime.now().strftime("%d %b, %I:%M %p")
        })
        st.success(f"Simulation complete: ₹{amount:,.2f} to {recipient}. No money was sent.")
        st.rerun()

st.markdown('<div class="section">Quick Services</div>', unsafe_allow_html=True)
services = st.columns(5)
for col, label in zip(services, ["📱\\nRecharge", "💡\\nElectricity", "📺\\nDTH", "💧\\nWater", "🔥\\nGas"]):
    with col:
        st.button(label, disabled=True, use_container_width=True)

st.markdown('<div class="section">Recent Transactions</div>', unsafe_allow_html=True)
for tx in st.session_state.transactions:
    sign = "+" if tx["kind"] == "Received" else "−"
    st.markdown(f"""
    <div class="tx">
      <div style="font-weight:800">{tx['name']}</div>
      <div class="small">{tx['kind']} • {tx['time']}</div>
      <div style="display:flex;justify-content:space-between;gap:10px;margin-top:8px">
        <b>{sign} ₹{tx['amount']:,.2f}</b>
        <span style="font-weight:700;color:#16794a">{tx['status']}</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:18px;color:#66738d;font-size:.85rem">
  UPI Pay demo • Educational prototype only<br>
  Not affiliated with ICICI Bank, Google Pay, NPCI, or Paytm.
  No real payments, QR scanning, or bank API.
</div>
""", unsafe_allow_html=True)
