import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="Convelio Japan Strategy", layout="wide", page_icon="⛩️")

# --- Header Section ---
st.title("Convelio Japan: Operational Logic Prototype")
st.markdown("""
**[Strategic Proposal]** Translating Japanese high-context market friction into executable digital logic.  
This dashboard mitigates legal risks at the source and enforces physical warehouse discipline.
""")

# ==========================================
# MODULE 1: UPSTREAM COMPLIANCE (Legal & Regulatory)
# ==========================================
st.divider()
st.header("1. 🏛️ Export Compliance & Risk Radar (Upstream)")
st.caption("Automates detection of Japan's '50-Year Rule' and material restrictions to prevent customs seizures.")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("#### 📦 Artwork Input")
    category = st.selectbox("Category", ["Contemporary Art", "Antiques / Traditional Art", "Furniture", "Other"])
    year = st.number_input("Year of Creation", min_value=1000, max_value=2026, value=2010)
    # Retained Japanese characters in parentheses to demonstrate handling of localized data input
    materials = st.multiselect("Regulated Materials?", ["None", "Ivory (象牙)", "Rosewood (紫檀)", "Tortoiseshell (べっ甲)"])

with col2:
    st.markdown("#### 🚨 Automated Assessment")
    is_older_than_50 = (2026 - year) > 50
    
    # Logic: Checking against Japanese Cultural Property Protection Law and CITES
    if category == "Antiques / Traditional Art" and is_older_than_50:
        st.error("🛑 HIGH RISK: Agency for Cultural Affairs Review Required")
        st.write("**Bottleneck:** Flagged under Cultural Property Protection Law. Requires a 'Certificate of Non-Cultural Property'.")
    elif any(m in ["Ivory (象牙)", "Tortoiseshell (べっ甲)"] for m in materials):
        st.error("🛑 FATAL RISK: CITES Violation Detected")
        st.write("**Action:** Immediate export ban. CITES permit from METI required.")
    else:
        st.success("✅ GREEN LIGHT: Standard Export Clearance")
        st.write("No specific historical or material restrictions detected. Safe to proceed.")

# ==========================================
# MODULE 2: DOWNSTREAM EXECUTION (Warehouse Quality)
# ==========================================
st.divider()
st.header("2. 🔒 Digital Quality Gate (Warehouse Execution)")
st.caption("Standardizes 'Japanese Quality' expectations into binary logic gates before label generation.")

col3, col4 = st.columns(2)

with col3:
    st.markdown("#### 🔍 Physical Inspection Input")
    gap = st.slider("Internal Gap Size (cm)", 0.0, 5.0, 1.2, help="Japanese expectation requires < 0.5cm")
    photo = st.radio("Pre-shipment Photo Quality", ["Missing", "Low-Res", "4K High-Res"])
    tape = st.checkbox("Tape Alignment Verified")

with col4:
    st.markdown("#### 📋 Audit Result")
    # Logic: Bridging physical handling with digital QA
    if gap > 0.5:
        st.error("❌ STATUS: LOCKED (Aesthetic Failure)")
        st.write("**Reason:** Gap exceeds 0.5cm. Perceived as lack of professional care, leading to claim risks.")
    elif photo != "4K High-Res":
        st.warning("⚠️ STATUS: PENDING (Documentation Issue)")
        st.write("**Reason:** High-res evidence is mandatory for Japanese insurance claims.")
    elif not tape:
        st.warning("⚠️ STATUS: PENDING (Presentation Issue)")
        st.write("**Reason:** Visual presentation directly reflects gallery brand trust.")
    else:
        st.success("✅ STATUS: APPROVED TO SHIP")
        st.write("Meets Japanese Tier-1 gallery physical standards. Label generation authorized.")

# --- Footer Section ---
st.divider()
st.caption("Developed for strategic validation. Designed to bridge the gap between legal frameworks and on-site warehouse execution.")
