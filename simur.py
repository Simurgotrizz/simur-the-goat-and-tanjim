import streamlit as st

# Page Title and Header
st.title("Comparing a House to Parts of a Plant Cell")
st.header("An Analogous Comparison") 

# Introduction
st.markdown(
    "Just as different parts of a plant cell work together to ensure its proper functioning, "
    "a house also consists of various components that contribute to its operation. "
    "Let's explore the similarities between them!"
)

# Plant Cell Image
st.image("plant_cell.jpg", caption="Plant Cell", use_column_width=True)

# Refrigerator Image
st.image("Parts-of-a-house.jpg", caption="house", use_column_width=True)

# Comparison Table
st.header("Comparison Table")

comparison_data = {
    "Plant Cell": [
        "Cell Wall", 
        "Chloroplast", 
        "Cytoplasm", 
        "Lysosome", 
        "Mitochondria",
        "Nucleus",
        "Endoplasmic Reticulum",
        "Golgi Body (a.k.a. Golgi Apparatus)*",
        "Ribosomes",
        "Vacuoles",
    ],

    "house": [
        "Walls of the house",
        "The kitchen",
        "Air in the house",
        "Garbage disposal or recycling container",
        "The fireplace and electricity",
        "The home owner",
        "Hallways and pipes in the house",
        "Backpack or luggage",
        "The oven, grill, or microwave of the house",
        "Refrigerator, closet, or pantry",
    ],
}

st.table(comparison_data)

# Conclusion
st.header("Conclusion")
st.markdown(
    "While a plant cell and a house serve completely different purposes, "
    "it's interesting to draw parallels between their components. Both examples highlight "
    "how individual parts contribute to the overall functioning of the system."
)
