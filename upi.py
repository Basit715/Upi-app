import streamlit as st
from datetime import datetime

st.set_page_config(page_title="UPI Demo • Basit Abass", page_icon="💳", layout="centered")

# Simulation-only UI. No bank, UPI, QR, or payment-network connection.
if "balance" not in st.session_state:
    st.session_state.balance = 11050.00
if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {"name": "Sahil", "amount": 700.00, "kind": "Sent", "status": "Demo", "time": "Today, 01:04 AM"},
        {"name": "Ayaan", "amount": 299.90, "kind": "Received", "status": "Demo", "time": "Yesterday, 07:24 PM"},
        {"name": "Rizwan", "amount": 299.99, "kind": "Sent", "status": "Demo", "time": "Yesterday, 07:22 PM"},
    ]
if "selected_recipient" not in st.session_state:
    st.session_state.selected_recipient = ""

st.markdown("""
<style>
.stApp, [data-testid="stAppViewContainer"] {background:#101010;}
[data-testid="stHeader"] {background:transparent;}
.block-container {max-width:650px;padding:1rem .8rem 5rem;}
html,body,p,label,h1,h2,h3,h4,span,div {color:#f2f2f2;}
h1,h2,h3 {letter-spacing:-.02em;}
div[data-testid="stMarkdownContainer"] p {color:#f2f2f2;}
.demo-note {background:#102c59;border:1px solid #214d8c;color:#e6f0ff;
 padding:10px 12px;border-radius:14px;text-align:center;font-weight:800;margin:8px 0 12px;}
.searchbox {background:#242424;border-radius:30px;padding:12px 18px;margin-bottom:12px;
 color:#ddd;font-size:1rem;border:1px solid #303030;}
.scenic {height:150px;border-radius:18px;margin:6px 0 16px;
 background:linear-gradient(180deg,#151b2b 0%,#20283a 42%,#063b2b 43%,#07502e 75%,#064223 100%);
 position:relative;overflow:hidden;border:1px solid #1c1c1c;}
.scenic:before {content:'🌙     ▪ ▪ ▪ ▪ ▪       ▪ ▪ ▪ ▪';position:absolute;top:18px;left:16px;color:#ffbf4a;}
.scenic:after {content:'🏛️                         🏪 🧍';position:absolute;bottom:12px;left:15px;font-size:28px;}
.demo-banner {background:#153a74;border:1px solid #1d5db5;color:#e8f1ff;
 border-radius:14px;padding:11px 13px;text-align:center;font-weight:900;margin-bottom:15px;}
.quick-card {background:#0752b9;border:1px solid #176bd5;border-radius:19px;
 padding:18px 8px 12px;text-align:center;min-height:96px;}
.quick-card .emoji {font-size:1.8rem;display:block;margin-bottom:6px;}
.quick-card b {font-size:.92rem;color:#fff;}
.pill {background:#171717;border:1px solid #383838;border-radius:25px;
 padding:12px 8px;text-align:center;min-height:55px;}
.section-title {font-size:1.2rem;font-weight:850;margin:1.2rem 0 .8rem;}
.contact {text-align:center;background:#111;padding:4px 2px;}
.avatar {height:64px;width:64px;border-radius:50%;display:flex;align-items:center;
 justify-content:center;font-size:1.5rem;font-weight:800;margin:0 auto 6px;
 background:#07543f;border:1px solid #333;}
.bill {background:#1c1c1c;border:1px solid #2d2d2d;border-radius:18px;
 padding:14px 7px;text-align:center;min-height:85px;}
.tx {background:#171717;border:1px solid #2b2b2b;border-radius:15px;padding:13px;margin:8px 0;}
.small {color:#a8a8a8;font-size:.85rem;}
div.stButton > button, div.stFormSubmitButton > button {
 background:#171717;color:#f2f2f2;border:1px solid #3a3a3a;border-radius:20px;
 min-height:44px;font-weight:650;
}
div.stFormSubmitButton > button {background:#0752b9;border:0;}
[data-testid="stMetric"] {background:#1a1a1a;border:1px solid #333;border-radius:16px;padding:12px;}
[data-testid="stMetricLabel"],[data-testid="stMetricValue"] {color:#f2f2f2 !important;}
hr {border-color:#303030;}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# Top search-style field and profile
st.markdown('<div class="searchbox">🔎 &nbsp; Pay friends and demo merchants &nbsp;&nbsp;&nbsp; <b>🟦 B</b></div>', unsafe_allow_html=True)
st.markdown('<div class="demo-note">DEMO ONLY — NO REAL PAYMENTS</div>', unsafe_allow_html=True)
st.markdown('<div class="scenic"></div>', unsafe_allow_html=True)

# Four quick action tiles
qcols = st.columns(4, gap="small")
items = [("▦", "Scan demo\\nQR"), ("₹↗", "Pay\\ndemo"), ("🏛", "Bank\\ndemo"), ("▣", "Mobile\\nrecharge")]
for col, (emoji, label) in zip(qcols, items):
    with col:
        st.markdown(f'<div class="quick-card"><span class="emoji">{emoji}</span><b>{label.replace(chr(10), "<br>")}</b></div>', unsafe_allow_html=True)

st.write("")
pillcols = st.columns(3, gap="small")
pilllabels = ["🏦 Balance\\nCheck", "🟢 History\\nSee all", "🚀 UPI Demo"]
for col, label in zip(pillcols, pilllabels):
    with col:
        st.markdown(f'<div class="pill">{label.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

# Contacts: fictional names and local simulation only
st.markdown('<div class="section-title">Send money <span style="color:#1688ff">› See all</span></div>', unsafe_allow_html=True)
contacts = [("S", "Sahil"), ("A", "Ayaan"), ("R", "Rizwan"), ("D", "Danish"), ("K", "Kashif")]
ccols = st.columns(5, gap="small")
for col, (initial, name) in zip(ccols, contacts):
    with col:
        st.markdown(f'<div class="contact"><div class="avatar">{initial}</div><div style="font-weight:700">{name}</div></div>', unsafe_allow_html=True)
        if st.button("Select", key=f"select_{name}", use_container_width=True):
            st.session_state.selected_recipient = name

st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Bills & recharges <span style="color:#1688ff">Manage ›</span></div>', unsafe_allow_html=True)
billcols = st.columns(4, gap="small")
billitems = [("📱", "Mobile\\nRecharge"), ("⚡", "Electricity\\nBill"), ("💧", "Water\\nBill"), ("📺", "DTH\\nRecharge")]
for col, (emoji, label) in zip(billcols, billitems):
    with col:
        st.markdown(f'<div class="bill">{emoji}<br><b>{label.replace(chr(10), "<br>")}</b></div>', unsafe_allow_html=True)

# The QR action is deliberately a placeholder, not an actual QR/payment flow.
st.write("")
st.button("▦   Scan QR (demo placeholder)", disabled=True, use_container_width=True)

with st.expander("Demo transfer (simulation)"):
    with st.form("demo_transfer"):
        recipient = st.text_input("Recipient", value=st.session_state.selected_recipient)
        amount = st.number_input("Amount (₹)", min_value=1.0, max_value=100000.0, step=1.0)
        submitted = st.form_submit_button("Simulate transfer", use_container_width=True)
    if submitted:
        if not recipient.strip():
            st.warning("Enter a demo recipient.")
        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")
        else:
            st.session_state.balance -= amount
            st.session_state.transactions.insert(0, {
                "name": recipient.strip(), "amount": amount, "kind": "Sent",
                "status": "Simulated", "time": datetime.now().strftime("%d %b, %I:%M %p")
            })
            st.success(f"Demo only: ₹{amount:,.2f} simulated for {recipient}. No money moved.")
            st.rerun()

with st.expander("Demo balance & transaction history"):
    st.metric("Simulated balance", f"₹{st.session_state.balance:,.2f}")
    for tx in st.session_state.transactions:
        sign = "+" if tx["kind"] == "Received" else "−"
        st.markdown(f"""
        <div class="tx">
          <b>{tx['name']}</b><br><span class="small">{tx['kind']} • {tx['time']}</span>
          <div style="margin-top:8px;font-weight:800">{sign} ₹{tx['amount']:,.2f} &nbsp; <span style="color:#62c98a">{tx['status']}</span></div>
        </div>""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#9a9a9a;font-size:.8rem;padding:20px 4px 10px">
  UPI-style interface prototype • Basit Abass<br>
  Independent demo • No real bank/payment connection • Not affiliated with Google Pay or NPCI
</div>
""", unsafe_allow_html=True)
                               
