import streamlit as st

def main():
    st.title("Plant Cell vs. Refrigerator Comparison")
    st.write("Explore the similarities and differences between a plant cell and a refrigerator!")

    # Load images
    plant_cell_image = "plant_cell.jpg"
    refrigerator_image = "refridgerator.jpg"

    st.image(plant_cell_image, caption="Plant Cell", use_column_width=True)
    st.image(refrigerator_image, caption="Refrigerator", use_column_width=True)


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
st.image("plant_cell.png", caption="Plant Cell", use_column_width=True)

# Refrigerator Image
st.image("refrigerator.png", caption="Refrigerator", use_column_width=True)

# Comparison Table
st.header("Comparison Table")

comparison_data = {
    "Plant Cell": [
        "Cell Membrane",
        "Nucleus",
        "Mitochondria",
        "Endoplasmic Reticulum",
        "Golgi Apparatus",
    ],
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
if __name__ == "__main__":
    main()
