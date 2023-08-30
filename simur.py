import streamlit as st

# Set page title and description
st.title("Cell and Refrigerator Comparison")
st.write("Explore the analogy between a cell and a refrigerator.")

# Create a dictionary to store cell parts and their refrigerator analogies
cell_parts = {
    "Cell Membrane": "Refrigerator Door",
    "Cytoplasm": "Interior of Refrigerator",
    "Mitochondria": "Power Source (Compressor)",
    "Endoplasmic Reticulum": "Shelves for Storage",
    "Golgi Apparatus": "Packaging and Shipping Area",
    "Nucleus": "Control Center",
    "Vacuoles": "Storage Compartments",
}

# Create a sidebar to select a cell part
selected_part = st.sidebar.selectbox("Select a Cell Part", list(cell_parts.keys()))

# Display the analogy
st.subheader(f"{selected_part} is like {cell_parts[selected_part]}")

# Explain the analogy
st.write("Just as a cell has various parts with specific functions, a refrigerator also has different components that work together to maintain its functionality. For example, the cell membrane is analogous to the refrigerator door, as it controls what enters and exits the cell, similar to how the door controls access to the refrigerator's interior.")
