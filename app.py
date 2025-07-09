import streamlit as st
from exercises import bicep_curls, dips, situps, plank, squats

st.set_page_config(page_title="AI Fitness Trainer", layout="centered")
st.title("🏋️ AI-Powered Fitness Trainer")

st.markdown("Select an exercise to begin:")

exercises = {
    "Bicep Curls": {
        "desc": "Track your bicep curl reps using pose estimation.",
        "func": bicep_curls
    },
    "Dips": {
        "desc": "Bodyweight dips using elbow angle tracking.",
        "func": dips
    },
    "Sit-Ups": {
        "desc": "Track sit-up reps by measuring torso angle.",
        "func": situps
    },
    "Plank": {
        "desc": "Real-time plank posture checker with timer.",
        "func": plank
    },
    "Squats": {
        "desc": "Count squat reps using knee and hip angles.",
        "func": squats
    }
}

for name, val in exercises.items():
    with st.container():
        st.subheader(name)
        with st.expander("ℹ️ Description"):
            st.write(val["desc"])
            if st.button(f"▶️ Start {name}"):
                st.info("Press 'q' in webcam window to quit.")
                val["func"]()
