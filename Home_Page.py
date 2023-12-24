import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2, = st.columns(2)


with col1:
    st.image('images/img.png', width=300)

with col2:
    st.title('Gleb Turanov')
    content = """Hi there! My name is Gleb. I'm proud to present you my portfolio.
    Born and located in Russian Federation, Saint-Petersburg. 
    Here I got Bachelor degree in Commercial Economics and was working in this direction.
    But since late few months I was studying Python coding and was very exited about learning new skill.
    Not just for work or living, but also for improving everyday  routine."""
    st.info(content)

content2 = """Below you can find some of the apps I have build during my study and experimenting. 
            Feel free to contact me! And have a great day!"""
st.info(content2)

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for i, row in df[0:9].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for i, row in df[9:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
