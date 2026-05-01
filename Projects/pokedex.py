import streamlit as st
from openai import OpenAI
import json

client = OpenAI(api_key=st.secrets["KEY"])

if "selected" not in st.session_state:
    st.session_state.selected = "Generate Entry"

if "pokedex" not in st.session_state:
    st.session_state.pokedex = []

pokedex = st.session_state.pokedex
message = ["Generate Entry", "View Entries"]

def id_exists(pokedex_list, pokemon_id):
    for entry in pokedex_list:
        if pokemon_id in entry:
            return True
    return False

def print_entry(entry_dict, name):
    with st.container(border=True):
        st.title(f"ID Number: {name}")
        col1, col2 = st.columns(2) 
        name = str(name).zfill(3)
        thing = entry_dict[name]
        for i in thing:
            if "Stats" == i:
                with col2:
                    st.header(i)
                    for j in thing["Stats"]:
                        with col2:
                            st.write("   ", j, ":", thing["Stats"][j])
            elif "Details" == i:
                with col2:
                    st.header(i)
                    for k in thing["Details"]:
                        if k == 'Abilities':
                            with col2:
                                st.header("    Abilities")
                                for s in thing["Details"]["Abilities"]:
                                    with col2:
                                        st.write("      ", s)
                        else:
                            with col2:
                                st.write("   ", k, ":", thing["Details"][k])
            else:
                with col1:
                    st.header(i)
                    st.write(f"{thing[i]}")

def merge_pokedex(pokedex_list):
    merged = {}
    for entry in pokedex_list:
        merged.update(entry)
    return merged

def order_id(entry_dict):
    ids = []
    for number in entry_dict:
        ids.append(int(number))
    n = len(ids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ids[j] > ids[j + 1]:
                ids[j], ids[j + 1] = ids[j + 1], ids[j]
    for k in ids:
        print_entry(entry_dict, str(k).zfill(3))

st.sidebar.title("Options")
st.title("Pokedéx")
st.write("Welcome to the Pokédex! Choose an option on the sidebar to either generate a Pokémon entry, or view existing Pokédex entries.")

for page in message:
    if st.sidebar.button(page, icon=":material/star:", use_container_width=True):
        st.session_state.selected = page
selected = st.session_state.selected

if selected == "Generate Entry":
    with st.container(border=True):
        col1, col2 = st.columns(2) 
        with col1:
            st.session_state.name = st.text_input("Pokémon Name")
            name = st.session_state.name
        with col2:
            st.session_state.id = st.number_input("ID Number", min_value=1, max_value=999, value=1 )
            id = st.session_state.id
    if st.button("Generate Entry"):
        realid = str(id).zfill(3)
        if id_exists(st.session_state.pokedex, realid):
            st.error(f"Pokédex ID {realid} already exists. Choose a different ID.")
        elif name == "":
            st.error("Fill out all required fields.")
        else:
            template = {'realid':{
                "Name": "",
                "Description": "",
                "Type": "",
                "Stats": {"HP" : "", "Attack": "", "Defense": "", "Speed": ""},
                "Details": {"Gender": "", "Category": "", 'Abilities': ["", "", ""]},
                "Weakness": "",
                "Evolution": ""}
                }

            system_prompt = f"""You are a Pokedex entry generator. Generate an entry about {name}. Follow this format: {template}. For the values of "Attack", "HP", "Defense", and "Speed", generate a number between 0 to 15 in relation to the Pokemon. For the pokemon's ID number, use {realid}. Do NOT put '''json or ''' in your output. Make sure to enclose all the variables with double quotes."""

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": system_prompt}
                ]
            )
            st.session_state.entry = json.loads(response.choices[0].message.content)
            entry = st.session_state.entry
            pokedex.append(entry)
            st.success("Successfully generated!")
            print_entry(entry, realid)

else:
    if pokedex == []:
        st.write("No generated entries yet!")
    else:
        merged = merge_pokedex(pokedex)
        order_id(merged)

# My application is a Pokedex. You can choose to generate entries about an existing Pokemon. In order to generate one, you have to insert the wanted Pokemon's name and the ID number. The ID number is required to not be in the Pokedex already and no more than 3 characters long. The name is required to be filled out, which expects the name of the pokemon. After generating a few entries, the user can view all the generated options, and the entries are arranged from ID number, smallest to biggest.