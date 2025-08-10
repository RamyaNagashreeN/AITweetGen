#backend code to use Google Gemini model for generating tweets
import os

os.environ['GOOGLE_API_KEY']  = st.secrets['GOOGLE_API_KEY']

#Using Google Models (Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

tweet_template = PromptTemplate(
    input_variables=["topic", "number_of_tweets"],
    template="Generate {number_of_tweets} tweets on the topic: {topic}"
)


# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

tweet_chain=tweet_template | gemini_model



# Example of using the Gemini model
#response = gemini_model.invoke("Give me 3 tweets on World War 1")

# Display the output
#print(response.content)





#frontend code
import streamlit as st

# Custom theme configuration
st.set_page_config(
    page_title="AI Tweet Generator",
    page_icon="🐦",
)

# Custom CSS styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #1DA1F2;
        color: white;
    }
    .stTextInput>div>div>input {
        border-color: #1DA1F2;
    }
    .stNumberInput>div>div>input {
        border-color: #1DA1F2;
    }
    </style>
""", unsafe_allow_html=True)


st.title("AI Tweet Generator 🐦")

st.markdown("""
    <h2 style='color: #1DA1F2;'>Generate Tweets on Any Topic</h2>
    """, unsafe_allow_html=True)

#st.header("Generate Tweets on Any Topic")

#st.subheader("Enter a topic below:")    

topic = st.text_input("Topic")

number_of_tweets = st.number_input("Number of Tweets", min_value=1, max_value=10, value=1, step=1)

# if st.button("Generate Tweets"):
#     st.write("Tweets will be generated here...")
#     tweets=tweet_chain.invoke({"topic": topic, "number_of_tweets": number_of_tweets})
#     st.write(tweets.content)

if st.button("Generate Tweets"):
    with st.container():
        st.write("Tweets will be generated here...")
        tweets = tweet_chain.invoke({"topic": topic, "number_of_tweets": number_of_tweets})
        #st.markdown(f"<div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px;'>{tweets.content}</div>", 
                  # unsafe_allow_html=True)










