import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import Simulation

st.set_page_config(page_title="ChangePro-AI (Prototype)", layout="wide")

# ---- Utilities ----
def kpi_box(label, value, suffix=""):
    c1, c2 = st.columns([1,2])
    with c1:
        st.caption(label)
    with c2:
        st.markdown(f"### **{value}{suffix}**")

# ---- Init session ----
if "sim" not in st.session_state:
    st.session_state.sim = Simulation()

sim = st.session_state.sim

# Sidebar controls
with st.sidebar:
    st.title("ChangePro‑AI")
    st.write("Prototype simulation for enterprise-wide AI adoption.")
    if st.button("🔁 Reset simulation", type="secondary"):
        st.session_state.sim = Simulation()
        st.experimental_rerun()
    st.markdown("---")
    st.subheader("Settings")
    speed = st.slider("S-curve speed multiplier", 0.5, 1.5, 1.0, 0.05,
                      help="Global multiplier applied to adoption dynamics.")
    sim.speed_multiplier = speed

st.title("🏢 ChangePro‑AI — Enterprise AI Rollout Simulator (Prototype)")

# KPIs
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.metric("Budget remaining", f"${sim.budget:,.0f}")
with k2:
    st.metric("Overall adoption", f"{sim.overall_adoption():.1f}%")
with k3:
    st.metric("Employee sentiment", f"{sim.sentiment:.0f}/100")
with k4:
    st.metric("Rounds played", f"{sim.round} / {sim.total_rounds}")

st.progress(min(sim.overall_adoption()/100, 1.0))

# Adoption per unit chart
df = pd.DataFrame({
    "Business Unit": [d['name'] for d in sim.departments],
    "Adoption %": [d['adoption']*100 for d in sim.departments],
    "Readiness": [d['readiness'] for d in sim.departments],
})
st.subheader("Adoption by Business Unit")
fig, ax = plt.subplots()
ax.bar(df["Business Unit"], df["Adoption %"])
ax.set_ylabel("Adoption (%)")
ax.set_ylim(0, 100)
ax.grid(True, axis="y", linestyle="--", alpha=0.4)
plt.xticks(rotation=20)
st.pyplot(fig, clear_figure=True)

with st.expander("View data table"):
    st.dataframe(df.set_index("Business Unit"))

st.markdown("---")

# Event & choices
if sim.round <= sim.total_rounds:
    ev = sim.current_event()
    st.header(f"Round {sim.round}: {ev['title']}")
    st.write(ev["description"])

    # Show options
    choice = st.radio("Choose an action:", [o["label"] for o in ev["options"]])
    picked = next(o for o in ev["options"] if o["label"] == choice)

    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("**Action details**")
        st.write(picked["detail"])
        st.caption(f"Cost: ${picked['cost']:,.0f}")
        if picked.get("risks"):
            st.warning("Risks: " + picked["risks"])
        if picked.get("note"):
            st.info(picked["note"])
    with c2:
        st.markdown("**Affected Units**")
        st.write(", ".join(picked.get("units", ["Enterprise"])))

    # Confirm button
    if st.button("Apply decision ➜"):
        if sim.budget < picked['cost']:
            st.error("Not enough budget for this action.")
        else:
            sim.apply_decision(picked)
            sim.advance_round()
            st.success("Decision applied. State updated.")
            st.experimental_rerun()
else:
    st.header("🏁 Simulation Complete")
    st.write("**Results**")
    st.write(f"- Overall adoption: **{sim.overall_adoption():.1f}%**")
    st.write(f"- Employee sentiment: **{sim.sentiment:.0f}/100**")
    st.write(f"- Budget remaining: **${sim.budget:,.0f}**")
    st.write(f"- Success criteria: adoption ≥ 85%, sentiment ≥ 70.")
    success = (sim.overall_adoption() >= 85) and (sim.sentiment >= 70)
    if success:
        st.success("🎉 You achieved the transformation goals!")
    else:
        st.error("You fell short of one or more goals. Try a different strategy.")
    if st.download_button("Download run log (JSON)",
                          data=json.dumps(sim.log, indent=2),
                          file_name="changepro_ai_run.json",
                          mime="application/json"):
        pass

st.markdown("---")
with st.expander("How it works (model)"):
    st.markdown("""
- Adoption follows a modified Bass diffusion with innovation **p** and imitation **q**, 
  modulated by sentiment and readiness.
- Each decision changes **p/q**, sentiment, and/or a specific unit's adoption.
- Random events may alter risk, budget, and resistance.
- Tune difficulty using the S-curve multiplier in the sidebar.
    """)
