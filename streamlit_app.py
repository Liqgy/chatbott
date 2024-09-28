import streamlit as st
import google.generativeai as genai

# App title
st.title("🐱 AI-powered Cat Knowledge Chatbot")

# Input for Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")

# Authenticate the API if the user provides a key
if gemini_api_key:
    try:
        # Configure the API with the provided key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")  # Use Gemini model for generating responses
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input for user message
user_input = st.text_input("Ask about a cat breed or type your message:")

# Add user input to chat history and display it
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    st.write(f"**You:** {user_input}")

    # Check if API Key is provided and model is set up
    if gemini_api_key and model:
        try:
            # Generate AI-based response
            prompt = (
                        f"ข้อมูลเบื้องต้นเกี่ยวกับแมวสายพันธุ์ '{user_input}' "
                        f"ให้คำแนะนำเกี่ยวกับวิธีการเลี้ยงดู "
                        f"รายละเอียดเกี่ยวกับ ประเภทของอาหาร ช่วงราคา "
                        f"ข้อควรระวังในการดูแล"
                    )
            response = model.generate_content(prompt)
            bot_response = response.text
            st.session_state.chat_history.append(("assistant", bot_response))
            st.write(f"**AI Bot:** {bot_response}")
            # st.text_input("Ask about a cat breed or type your message:")
        except Exception as e:
            st.error(f"An error occurred while generating AI response: {e}")
    
    else:
        # Check if user is asking about a specific breed
        breed_name = user_input.strip().capitalize()  # Capitalize for dictionary lookup
        #breed_info = get_cat_breed_info(breed_name)

        # if breed_info["description"] != "Sorry, I don't have information about that breed.":
        #     bot_response = (
        #         f"**Description:** {breed_info['description']} \n\n"
        #         f"**Care Tips:** {breed_info['care']} \n\n"
        #         f"**Personality Traits:** {breed_info['personality']}"
        #     )
        #     follow_up_question = generate_follow_up_question(breed_name)
        #     bot_response += f"\n\n**Follow-up Question:** {follow_up_question}"
        # else:
        #     bot_response = breed_info["description"]

        # # Append bot response to chat history and display
        # st.session_state.chat_history.append(("assistant", bot_response))
        # st.write(f"**Bot:** {bot_response}")