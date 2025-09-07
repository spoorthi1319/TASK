import streamlit as st

# -------------------------------
# FAQ knowledge base (keywords → answer)
# -------------------------------
faqs = {
    ("program", "course", "about", "what programs", "offer"): 
        "Iron Lady offers leadership programs designed to empower professionals with skills in confidence, decision-making, and strategic leadership.",
    ("duration", "time", "how long", "weeks", "program duration"): 
        "The leadership program usually runs for 12 weeks with live sessions and assignments.",
    ("mode", "online", "offline", "class type", "is it online", "is it offline"): 
        "The program is conducted online with interactive live classes, group activities, and case studies.",
    ("certificate", "certification", "completion proof", "are certificates provided"): 
        "Yes, participants receive a recognized certificate of completion after successfully finishing the program.",
    ("mentors", "teachers", "trainers", "faculty", "who are the mentors", "coaches"): 
        "Our mentors are industry experts, leaders, and certified trainers with years of experience.",
    ("fees", "price", "cost", "payment"): 
        "Fee details can be requested directly from the Iron Lady admissions team.",
    ("register", "admission", "enroll", "apply"): 
        "You can register through the Iron Lady official website or contact the admissions team for assistance.",
    ("internship", "job training"): 
        "Currently, the program does not include an internship, but it focuses on leadership skills that enhance career growth.",
    ("good", "bad", "worth", "valuable"): 
        "The program has received positive feedback from participants who found it highly valuable for personal and professional growth.",
    ("placement", "get placed", "job", "career", "opportunity"): 
        "While the program is not a direct placement service, it equips you with strong leadership skills that improve career opportunities.",
    ("thankyou","Thank you","thanks"): 
        "Welcome! Thank you for visiting our site. For further queries, contact our team.",
    ("Bye","bye"): "Bye."
}


# -------------------------------
# Function to get FAQ answer
# -------------------------------
def get_answer(user_input):
    for keywords, reply in faqs.items():
        for keyword in keywords:
            if keyword in user_input.lower():
                return reply
    return "Sorry, I don’t have an answer for that. Please contact Iron Lady support."

# -------------------------------
# Streamlit Web App with chat history
# -------------------------------
st.set_page_config(page_title="Iron Lady Chatbot", page_icon="🤖")

st.title("Iron Lady Leadership Chatbot")
st.write("Ask me about program details, duration, mode, certificate, mentors, fees, registration, internship, placement, and more.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(("You", user_input))

    # Bot logic
    if user_input.lower() in ["hi", "hello", "hey"]:
        bot_reply = "Welcome to Iron Lady Leadership Program, How can I help you?"
    elif user_input.lower() == "help":
        bot_reply = "You can ask me about program details, duration, mode, certificate, mentors, fees, registration, internship, and placements."
    else:
        bot_reply = get_answer(user_input)

    # Add bot reply
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)
