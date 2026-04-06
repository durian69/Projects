import streamlit as st

# packing = {
#     "Beach": ["Sunscreen", "Swimsuit", "Towel", "Flip Flops", "Sunglasses"],
#     "Mountains": ["Hiking Boots", "Jacket", "Water Bottle", "Trail Map", "Gloves"],
#     "City": ["Comfortable Shoes", "City Map", "Camera", "Umbrella", "Portable Charger"],
#     "Camping": ["Tent", "Sleeping Bag", "Flashlight", "Bug Spray", "Matches"]
# }

# locations = ["Beach", "Mountains", "City", "Camping"]

# if "selected" not in st.session_state:
#     st.session_state.selected = None

# st.title("Trip Packer")
# with st.sidebar:
#     st.header("Trip Settings")
#     st.session_state.selected = st.selectbox("Where are you going?", locations)



# st.header(f"Packing List for: {st.session_state.selected}")
# if st.session_state.selected:
#     selected = st.session_state.selected
#     data = packing[selected]
#     items = st.multiselect("Select items to pack", data)
#     if st.checkbox("Mark everything as packed"):
#         st.success("You're all packed!")
#     else:
#         packing = "Packing: "
#         for value in items:
#             packing += value
#             packing += ", "
#         st.write(packing)





# st.title("Pizza Builder")

# with st.container(border=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         size = st.selectbox("Size", ["Small", "Medium", "Large"])
#     with col2:
#         num = st.number_input("Quantity", min_value=1, max_value=10, value=1 )
#     topping = st.multiselect("Toppings", ["Pepperoni", "Mushrooms", "Olives", "Peppers", "Extra Cheese"])

# top = ""

# for value in topping:
#     top += value
#     top += ", "

# if st.button("Place Order"):
#     st.header("Order Summary")
#     st.markdown(f"**Size:** {size} x{num}")
#     st.markdown(f"**Toppings:** {top}")
#     if size == "Small":
#         cost = 8*num
#         st.markdown(f"**Total: ${cost}**")
#     if size == "Medium":
#         cost = 11*num
#         st.markdown(f"**Total: ${cost}**")
#     if size == "Large":
#         cost = 14*num
#         st.markdown(f"**Total: ${cost}**")
    
# if "selected" not in st.session_state:
#     st.session_state.selected = None

# history= {}

# grades = {
#     "A": [90, 100],
#     "B": [80, 89],
#     "C": [70, 79],
#     "D": [60, 69],
#     "F": [0, 59]
# }

# st.title("Grade Checker")
# st.session_state.grade = st.number_input("Enter your score (0-100)", min_value=0,max_value=100, value=0)

# num = st.session_state.grade

# if num >= 90:
#     level="A"
# if num >= 80 and num <= 90:
#     level="B"
# if num >=70 and num <= 79:
#     level="C"
# if num >=60 and num<=69:
#     level="D"
# if num <= 59:
#     level="F"
    
# st.session_state.history = []
# st.session_state.history.append(f"{num} -> {level}")

# top = ""

# for value in st.session_state.history:
#     top += value

# if st.button("Check Grade"):
#     st.success(f"Score: {num} -> Grade: {level}")
#     st.title("Grade History:")
#     st.write(top)

