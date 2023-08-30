import streamlit as st

# Page Title and Header
st.title("Comparing a Refrigerator to Parts of a Plant Cell")
st.header("An Analogous Comparison")

# Introduction
st.markdown(
    "Just as different parts of a plant cell work together to ensure its proper functioning, "
    "a refrigerator also consists of various components that contribute to its operation. "
    "Let's explore the similarities between them!"
)

# Plant Cell Image
st.image("plant_cell.jpg", caption="Plant Cell", use_column_width=True)

# Refrigerator Image
st.image("refridgerator.jpg", caption="Refrigerator", use_column_width=True)

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
        "Vacuoles",]

    "Refrigerator": [
        "Door Seal",
        "Thermostat",
        "Compressor",
        "Cooling Coils",
        "Fan",
    ],
}

st.table(comparison_data)

# Conclusion
st.header("Conclusion")
st.markdown(
    "While a plant cell and a refrigerator serve completely different purposes, "
    "it's interesting to draw parallels between their components. Both examples highlight "
    "how individual parts contribute to the overall functioning of the system."
)
