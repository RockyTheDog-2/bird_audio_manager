import streamlit as st

st.set_page_config(
    page_title="Credits",
    page_icon="📃",
    layout="wide",
)

st.title("St. Louis Wildlife Project")
st.write(
    "Credits"
)

# EDIT THE TEXT BELOW ANYTIME YOU WANT TO UPDATE YOUR CREDITS PAGE.

left_box, right_box = st.columns(2, gap="large")

with left_box:
    with st.container(border=True):
        st.subheader("Where the project came from:")
        st.write(
            "This project was originally made for a robotics competition in the MICDS team. However, only two people in the team worked on it. We worked with a St. Louis "
            "Wildlife Project researcher to make this possible."
        )

with right_box:
    with st.container(border=True):
        st.subheader("The team:")
        st.write(
            "-Dhruv Bherthepudi"
        )

        st.write(
            "-Matthew Elliott"
        )
