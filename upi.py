import streamlit as st
from datetime import datetime

st.set_page_config(page_title="UPI Pay — Demo", page_icon="💸", layout="wide")

# DEMO ONLY: This app does not connect to banks, UPI, or payment networks.
if "balance" not in st.session_state:
    st.session_state.balance = 11050.00
if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {"name": "Ram Singh", "amount": 700.00, "kind": "Sent", "status": "Success", "time": "Today, 01:04 AM"},
        {"name": "KHUSHBOO", "amount": 299.90, "kind": "Received", "status": "Received", "time": "Yesterday, 07:24 PM"},
        {"name": "Sudeep Das Saha", "amount": 299.99, "kind": "Sent", "status": "Failed", "time": "Yesterday, 07:22 PM"},
    ]

st.markdown("""
<style>
.demo-banner {background:#fff3cd;color:#664d03;border:1px solid #ffecb5;
 padding:10px 14px;border-radius:10px;font-weight:700;text-align:center;margin-bottom:15px;}
.hero {background:linear-gradient(120deg,#4f20d8,#7856f4);padding:24px;border-radius:18px;color:white;}
.hero h1 {color:white;margin:0;} .hero p {margin-bottom:0;}
</style>
<div class="demo-banner">DEMO SIMULATOR — No real money or bank connection</div>
<div class="hero"><h1>💸 UPI Pay</h1><p>Pay. Send. Receive. (Simulated)</p><p><b>Demo profile: Basit Abass</b></p></div>
""", unsafe_allow_html=True)

st.subheader("Accounts")
left, right = st.columns([1, 2])
with left:
    st.markdown("### 🏦 ICICI Bank")
    st.caption("Saving A/c • 0456")
with right:
    st.metric("Demo available balance", f"₹{st.session_state.balance:,.2f}")

st.subheader("Quick actions")
a, b, c = st.columns(3)
a.button("➤ Send money", use_container_width=True)
b.button("▦ Scan & pay (disabled)", disabled=True, use_container_width=True)
c.button("↓ Receive money", use_container_width=True)

st.subheader("Demo transfer")
with st.form("transfer_form"):
    recipient = st.text_input("Recipient name")
    amount = st.number_input("Amount (₹)", min_value=1.0, max_value=100000.0, step=1.0)
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Simulate transfer")

if submitted:
    if not recipient.strip():
        st.warning("Enter a recipient name to run the simulation.")
    elif amount > st.session_state.balance:
        st.error("Insufficient demo balance.")
    else:
        st.session_state.balance -= amount
        st.session_state.transactions.insert(0, {
            "name": recipient.strip(), "amount": amount, "kind": "Sent",
            "status": "Demo success", "time": datetime.now().strftime("%d %b, %I:%M %p")
        })
        st.success(f"Demo transfer of ₹{amount:,.2f} to {recipient} simulated. No payment was made.")
        st.rerun()

st.subheader("Shortcuts")
cols = st.columns(5)
for col, label in zip(cols, ["📱 Mobile recharge", "💡 Electricity", "📺 DTH", "💧 Water", "🔥 Gas"]):
    col.button(label, disabled=True, use_container_width=True)

st.subheader("Recent transactions")
for tx in st.session_state.transactions:
    with st.container(border=True):
        x, y = st.columns([3, 1])
        x.markdown(f"**{tx['name']}**  \n{tx['kind']} • {tx['time']}")
        sign = "+" if tx["kind"] == "Received" else "−"
        y.markdown(f"**{sign} ₹{tx['amount']:,.2f}**  \n{tx['status']}")

st.caption("Educational UI prototype. Not affiliated with ICICI Bank, NPCI, or Paytm. No real payment, QR scanning, authentication, or banking API is implemented.")
