import streamlit as st
import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Enter your email here')
    user_message = st.text_area('Your message')
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
    """
    submit_button = st.form_submit_button('Submit')
    if submit_button:
        send_email.send_emails(message)
        st.info('Email was sent. Thank you')



