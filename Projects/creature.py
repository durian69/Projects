import streamlit as st

st.title("Mythical Creature Builder")
st.header("Design your own legendary being")


with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Creature Name")
        world = st.text_input("World of Origin")
    with col2:
        type = st.selectbox("Creature Type", ["Dragon", "Spirit", "Robot", "Alien", "Unknown"])
        person = st.radio("Personality Type", ["Agressive", "Calm", "Mysterious", "Chaotic"])
        life = st.number_input("Lifespan (years)", 
                               min_value=1,
                               max_value=10000)
    powers = st.multiselect("Select Special Abilities", ["Fire Control", "Mind Reading", "Teleportation", "Invisibility", "Super Strength"])
    back = st.text_area("Write a short backstory")
    weak = st.checkbox("Include a weakness")
    if weak == True:
        weakness = st.text_input("What is the creature weak to?")
    gen = st.button("Generate Profile")

if gen == True:
    if name == "" or world == "" or type == "" or person == "" or life == "" or powers == "" or back == "":
        st.error("Please fill out all required fields.")
        if weak == True:
            if weakness == "":
                st.error("Please fill out all required fields.")
    else:
        st.success("Creature Profile Generated!")
        st.header("Creature Summary")
        st.write("**Name:**", name)
        st.write("**Origin:**", world)
        st.write("**Type:**", type)
        st.write("**Personality:**", person)
        st.write("**Lifespan:**", life, "years")
        st.write("**Abilities:**")
        for i in powers:
            st.markdown(f"""
                        - {i}
                        """)
        st.write("**Backstory:**", back)
        if weak == True:
            st.warning(f"Weakness: {weakness}")
        st.button("Reset Builder")