import streamlit as st

st.set_page_config(page_title="ComicCraft", page_icon="💥", layout="centered")

st.title("💥 ComicCraft")
st.subheader("AI Comic Generator")

story = st.text_area("Enter your story:", "A superhero cat saving the city!")

style = st.selectbox("Comic Style", ["Marvel Style", "Manga Style", "Cartoon Style"])

if st.button("Generate Comic"):
    st.success(f"Generating your comic in {style}!")
    st.write(f"**Story:** {story}")
    st.balloons()
    st.image("https://media.giphy.com/media/3o7aD2saalBwwIDFGo/giphy.gif", caption="Your Comic is Ready! (Demo)")

st.markdown("---")
st.caption("Built with ❤️ by Sitharaman")
