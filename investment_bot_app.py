import streamlit as st
import openai
import pandas as pd

openai.api_key = "placeholder"

# Example mock data (replace with actual DataFrame)
def load_data():
    data = {
        "Date": ["2025-01-10", "2025-01-11", "2025-01-12"],
        "Crash_Prediction": [0, 1, 0],
        "Crash_Probability": [0.01, 0.92, 0.03],
        "Investment_Action": ["Growth Investments", "Safe Assets", "Growth Investments"],
        "Portfolio_Value": [10000, 9000, 11000],
        "Buy_and_Hold": [10000, 8000, 10500],
    }
    return pd.DataFrame(data)

data = load_data()

# Function to generate GPT responses using the new API
def ask_gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # Use the appropriate model, e.g., "text-davinci-003"
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

st.title("GPT-Powered Investment Chatbot")
st.write("Ask me about market predictions, investment strategies, or historical performance!")

# User input
user_input = st.text_input("Type your question below:")

# Bot response logic
if user_input:
    if "market prediction" in user_input.lower():
        latest_prediction = data.iloc[-1]
        if latest_prediction["Crash_Prediction"] == 1:
            gpt_prompt = "Explain what a market crash is and why it might happen."
            gpt_response = ask_gpt(gpt_prompt)
            st.write(f"The market is likely to crash with a probability of {latest_prediction['Crash_Probability']:.2%}.")
            st.write(f"GPT Explanation: {gpt_response}")
        else:
            st.write(f"The market is stable with a probability of {latest_prediction['Crash_Probability']:.2%}.")
    
    elif "investment action" in user_input.lower():
        latest_action = data.iloc[-1]["Investment_Action"]
        gpt_prompt = f"What are some advantages of {latest_action.lower()} in current market conditions?"
        gpt_response = ask_gpt(gpt_prompt)
        st.write(f"Recommended Action: {latest_action}")
        st.write(f"GPT Insight: {gpt_response}")
    
    elif "performance" in user_input.lower():
        st.write(f"Strategy Final Portfolio Value: ${data['Portfolio_Value'].iloc[-1]:,.2f}")
        st.write(f"Buy-and-Hold Final Portfolio Value: ${data['Buy_and_Hold'].iloc[-1]:,.2f}")
        st.line_chart(data[["Portfolio_Value", "Buy_and_Hold"]])
    else:
        gpt_prompt = f"Answer this user query: {user_input}"
        gpt_response = ask_gpt(gpt_prompt)
        st.write(f"GPT Response: {gpt_response}")

