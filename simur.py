import streamlit as st

def main():
    st.title("Plant Cell vs. Refrigerator Comparison")
    st.write("Explore the similarities and differences between a plant cell and a refrigerator!")

    # Load images
    plant_cell_image = "plant_cell.jpg"
    refridgerator_image = "refrigerator.jpg"

    st.image(plant_cell_image, caption="Plant Cell", use_column_width=True)
    st.image(refrigerator_image, caption="Refrigerator", use_column_width=True)

    st.header("Comparison:")
    st.subheader("1. Structure")
    st.write("A plant cell has a defined structure with various organelles, similar to the compartments and shelves in a refrigerator.")

    st.subheader("2. Energy Source")
    st.write("Plant cells generate energy through photosynthesis using chloroplasts. A refrigerator requires electricity to power its cooling system.")

    st.subheader("3. Storage")
    st.write("Both entities have storage capabilities: a plant cell stores nutrients and water, while a refrigerator stores food and beverages.")

    st.subheader("4. Regulation")
    st.write("Plant cells regulate water and nutrients using the cell membrane and vacuole, while a refrigerator regulates temperature and humidity.")

    st.subheader("5. Maintenance")
    st.write("Regular maintenance of a refrigerator ensures efficient cooling, just as a plant cell requires proper care for its health.")

if __name__ == "__main__":
    main()
