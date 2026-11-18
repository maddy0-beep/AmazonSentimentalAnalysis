import streamlit as st 
import requests

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎬",
    layout ="centered"
)
st.title("Product Review Sentiment Analyzer")
st.write("Enter a product review and get instant snetiment prediction!")

review = st.text_area('Enter your product review here:', height=150)

if st.button('Analyze Sentiment'):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):

            response=requests.post(
                "http://127.0.0.1:5000/predict",
                json={"reviews": review}
            )
            result=response.json()
            
        sentiment = result['prediction']
        # confidence = result['confidence']
        if "positive" in sentiment or "negative" in sentiment:
            st.success(f"Sentiment : {sentiment}")
        else:
            st.error(f"Sentiment : {sentiment}")
       # st.metric(label="Confidence", value=confidence)

            
               
                               