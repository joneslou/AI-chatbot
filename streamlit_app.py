import streamlit as st

# --- Page Title and Description ---
st.title("💬 Multi-Model Chatbot")
st.write(
    "This chatbot supports multiple language models: DeepSeek and Qwen. "
    "Select your preferred model, enter the relevant API key, and start chatting!"
)

# --- Model Selection ---
model_options = [
    "DeepSeek",   # You can rename or add more models as needed
    "Qwen"
]
selected_model = st.selectbox("Choose Model", model_options)

# --- API Key Input ---
if selected_model == "DeepSeek":
    api_key = st.text_input("DeepSeek API Key", type="password")
elif selected_model == "Qwen":
    api_key = st.text_input("Qwen API Key", type="password")
else:
    api_key = None

if not api_key:
    st.info(f"Please enter your {selected_model} API key to continue.", icon="🗝️")
    st.stop()

# --- Session State for Chat Messages ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Call the appropriate model API ---
    if selected_model == "DeepSeek":
        # TODO: Replace the following with actual DeepSeek API call
        # Example (pseudo-code):
        # response = deepseek_chat(api_key, st.session_state.messages)
        response = "DeepSeek response: (implement DeepSeek API call here)"
    elif selected_model == "Qwen":
        # TODO: Replace the following with actual Qwen API call
        # Example (pseudo-code):
        # response = qwen_chat(api_key, st.session_state.messages)
        response = "Qwen response: (implement Qwen API call here)"
    else:
        response = "Model not supported."

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
