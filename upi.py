import streamlit as st
from datetime import datetime

st.set_page_config(page_title="gpay", page_icon="💸", layout="wide")

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
.stApp {
  background:
    radial-gradient(circle at 8% 4%, #d9e9ff 0, transparent 24%),
    radial-gradient(circle at 95% 15%, #dff5e8 0, transparent 22%),
    radial-gradient(circle at 90% 65%, #fff1d2 0, transparent 20%),
    #f8fbff;
}
.block-container {padding-top:1.3rem; max-width:1100px;}
.demo-banner {background:#e7f0ff;color:#174ea6;border:1px solid #c5dcff;
 padding:10px 14px;border-radius:14px;font-weight:800;text-align:center;margin-bottom:15px;}
.hero {background:linear-gradient(120deg,#4285f4,#34a853 55%,#fbbc05 78%,#ea4335);
 padding:24px;border-radius:22px;color:white;box-shadow:0 8px 22px #9db8ef55;}
.hero h1 {color:white;margin:0;} .hero p {margin-bottom:0;}
div[data-testid="stMetric"] {background:white;padding:14px;border-radius:18px;
 border:1px solid #e4ecff;box-shadow:0 4px 12px #9db8ef22;}
div[data-testid="stVerticalBlockBorderWrapper"] {border-radius:18px;}
</style>
<div class="demo-banner"></div>
<div class="hero"><h1>💠 </h1><p>Pay. Send. Receive. (Simulated)</p><p><b>Basit Abass</b></p></div>
""", unsafe_allow_html=True)

st.subheader("Accounts")
left, right = st.columns([1, 2])
with left:
    st.markdown("### 🏦 ICICI Bank")
    st.caption("Saving A/c • 0456")
with right:
    st.metric("Available balance", f"₹{st.session_state.balance:,.2f}")

st.subheader("Quick actions")
a, b, c = st.columns(3)
a.button("➤ Send money", use_container_width=True)
b.button("▦ Scan & pay", disabled=False, use_container_width=True)
c.button("↓ Receive money", use_container_width=True)

st.subheader("transfer")
with st.form("transfer_form"):
    recipient = st.text_input("Recipient name")
    amount = st.number_input("Amount (₹)", min_value=1.0, max_value=100000.0, step=1.0)
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Simulate transfer")

if submitted:
    if not recipient.strip():
        st.warning("Enter a recipient name to run the simulation.")
    elif amount > st.session_state.balance:
        st.error("Insufficient  balance.")
    else:
        st.session_state.balance -= amount
        st.session_state.transactions.insert(0, {
            "name": recipient.strip(), "amount": amount, "kind": "Sent",
            "status": "success", "time": datetime.now().strftime("%d %b, %I:%M %p")
        })
        st.success(f"transfer of ₹{amount:,.2f} to {recipient} simulated. No payment was made.")
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


