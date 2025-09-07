import streamlit as st
import datetime
import random

# Initialize session state
if "moods" not in st.session_state:
    st.session_state.moods = []
if "date" not in st.session_state:
    st.session_state.date = datetime.date.today()
if "mood" not in st.session_state:
    st.session_state.mood = "😊 Happy"
if "note" not in st.session_state:
    st.session_state.note = ""

st.title("🌙 Mood Journal App")

# --- Create Entry ---
st.subheader("Add Your Mood Entry")
st.session_state.date = st.date_input("Date", st.session_state.date)
st.session_state.mood = st.selectbox(
    "Your mood",
    ["😊 Happy", "😔 Sad", "😐 Neutral", "😡 Angry", "😴 Tired", "🤩 Excited"],
    index=["😊 Happy", "😔 Sad", "😐 Neutral", "😡 Angry", "😴 Tired", "🤩 Excited"].index(st.session_state.mood)
)
st.session_state.note = st.text_area("Notes (optional)", st.session_state.note)

if st.button("Add Entry"):
    st.session_state.moods.append({
        "date": str(st.session_state.date),
        "mood": st.session_state.mood,
        "note": st.session_state.note
    })
    st.success("Mood entry added!")

    # Reset form fields
    st.session_state.date = datetime.date.today()
    st.session_state.mood = "😊 Happy"
    st.session_state.note = ""

    # Rerun so fields clear instantly
    st.experimental_rerun()

# --- Read Entries ---
st.subheader("📅 Your Mood Journal")
if not st.session_state.moods:
    st.info("No entries yet. Add your first mood!")
else:
    for i, entry in enumerate(st.session_state.moods):
        with st.expander(f"{entry['date']} - {entry['mood']}"):
            st.write(entry["note"] if entry["note"] else "No notes")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("✏️ Edit", key=f"edit_{i}"):
                    new_mood = st.selectbox(
                        "Update mood",
                        ["😊 Happy", "😔 Sad", "😐 Neutral", "😡 Angry", "😴 Tired", "🤩 Excited"],
                        key=f"mood_{i}"
                    )
                    new_note = st.text_area("Update note", entry["note"], key=f"note_{i}")
                    if st.button("Save", key=f"save_{i}"):
                        st.session_state.moods[i]["mood"] = new_mood
                        st.session_state.moods[i]["note"] = new_note
                        st.experimental_rerun()
            with col2:
                if st.button("❌ Delete", key=f"delete_{i}"):
                    st.session_state.moods.pop(i)
                    st.experimental_rerun()

# --- AI Weekly Summary ---
st.subheader("🤖 Weekly Mood Summary")
if st.button("Generate Summary"):
    if len(st.session_state.moods) == 0:
        st.warning("Add some mood entries first!")
    else:
        moods = [m["mood"] for m in st.session_state.moods]
        notes = [m["note"] for m in st.session_state.moods if m["note"]]
        
        summary = f"This week you logged {len(moods)} moods. "
        summary += f"Most frequent mood: {max(set(moods), key=moods.count)}. "
        if notes:
            summary += f"You often mentioned things like: {random.choice(notes)}."
        
        st.success(summary)
