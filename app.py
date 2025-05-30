import streamlit as st

# Page config
st.set_page_config(page_title="🎓 Admission Predictor", layout="centered")

# Title and header
st.title("🎓 Admission Predictor")
st.markdown("Enter your 10th standard subject marks (out of 100) to get stream recommendations for 11th & 12th.")

# Input marks
st.subheader("📋 Enter Your Marks:")
math = st.number_input("Mathematics", 0, 100)
science = st.number_input("Science", 0, 100)
english = st.number_input("English", 0, 100)
social = st.number_input("Social Studies", 0, 100)
language = st.number_input("Second Language (Hindi/Marathi etc.)", 0, 100)

# Predict button
if st.button("🔍 Predict Stream"):
    marks = [math, science, english, social, language]
    avg = sum(marks) / len(marks)

    if avg >= 80 and math >= 75 and science >= 75:
        stream = "Science"
        suggestion = "You have strong analytical and reasoning ability. Science could be a great fit for you!"
    elif avg >= 65 and math >= 60 and english >= 60:
        stream = "Commerce"
        suggestion = "Commerce can be a good option if you're interested in business, economics, or accounting."
    else:
        stream = "Arts"
        suggestion = "Arts stream can open paths in humanities, literature, and social sciences."

    st.success(f"✅ Recommended Stream: **{stream}**")
    st.info(suggestion)

# Footer
st.markdown("---")
st.markdown("""
📱 **App made by:** Amit Dhaygude  
📧 **Email:** [amitdhaygude22@gmail.com](mailto:amitdhaygude22@gmail.com)
""")
