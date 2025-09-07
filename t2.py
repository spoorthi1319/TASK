import streamlit as st
import datetime
import random

# ----------------- Custom CSS Styling -----------------
st.markdown(
    <style>
    body {
        background-color: #f0f4f8;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    h1 {
        color: #4a90e2;
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
    }
    h2, h3 {
        color: #333333;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(135deg, #4a90e2, #63cdda);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #63cdda, #4a90e2);
    }
    .stTextInput, .stTextArea, .stDateInput, .stSelectbox {
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    </style>
, unsafe_allow_html=True)

# ----------------- Session State -----------------
if "moods" not in st.session_state:
    st.session_state.moods = []
if "date" not in st.session_state:
    st.session_state.date = datetime.date.today()
if "mood" not in st.session_state:
    st.session_state.mood = "😊 Happy"
if "note" not in st.session_state:
    st.session_state.note = ""

# ----------------- App Title -----------------
st.title(" Mood Journal App")

# ----------------- Create Entry -----------------
st.subheader("📝 Add Your Mood Entry")
st.session_state.date = st.date_input("📅 Date", st.session_state.date)
st.session_state.mood = st.selectbox(
    "💭 Your mood",
    ["😊 Happy", "😔 Sad", "😐 Neutral", "😡 Angry", "😴 Tired", "🤩 Excited"],
    index=["😊 Happy", "😔 Sad", "😐 Neutral", "😡 Angry", "😴 Tired", "🤩 Excited"].index(st.session_state.mood)
)
st.session_state.note = st.text_area("🖊️ Notes (optional)", st.session_state.note)

if st.button("➕ Add Entry"):
    st.session_state.moods.append({
        "date": str(st.session_state.date),
        "mood": st.session_state.mood,
        "note": st.session_state.note
    })
    st.success("✅ Mood entry added!")

    # Reset form
    st.session_state.date = datetime.date.today()
    st.session_state.mood = "😊 Happy"
    st.session_state.note = ""

    st.experimental_rerun()

# ----------------- Read Entries -----------------
st.subheader("📖 Your Mood Journal")
if not st.session_state.moods:
    st.info("No entries yet. Start tracking your mood today!")
else:
    for i, entry in enumerate(st.session_state.moods):
        with st.expander(f"{entry['date']} - {entry['mood']}"):
            st.write(entry["note"] if entry["note"] else "_No notes_")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("✏️ Edit", key=f"edit_{i}"):
                    new_mood = st.selectbox(
                        "Update mood",
                        ["😊 Happy", "😔 Sad", "😐 Neutral", "😡 Angry", "😴 Tired", "🤩 Excited"],
                        key=f"mood_{i}"
                    )
                    new_note = st.text_area("Update note", entry["note"], key=f"note_{i}")
                    if st.button("💾 Save", key=f"save_{i}"):
                        st.session_state.moods[i]["mood"] = new_mood
                        st.session_state.moods[i]["note"] = new_note
                        st.experimental_rerun()
            with col2:
                if st.button("❌ Delete", key=f"delete_{i}"):
                    st.session_state.moods.pop(i)
                    st.rerun()

# ----------------- AI Weekly Summary -----------------
st.subheader("🤖 Weekly Mood Summary")
if st.button("✨ Generate Summary"):
    if len(st.session_state.moods) == 0:
        st.warning("⚠️ Add some mood entries first!")
    else:
        moods = [m["mood"] for m in st.session_state.moods]
        notes = [m["note"] for m in st.session_state.moods if m["note"]]

        summary = f"This week you logged **{len(moods)}** moods. "
        summary += f"Most frequent mood: **{max(set(moods), key=moods.count)}**. "
        if notes:
            summary += f"One highlight from your notes: *{random.choice(notes)}*"

        st.success(summary)
