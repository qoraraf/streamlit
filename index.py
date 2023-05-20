import streamlit as st
from PIL import Image


st.title("Envision Your Style, embrace Your Identity")


def display_sidebar():
    image = Image.open("logo.jpg")
    st.sidebar.image(image, width=150)
    st.sidebar.title("Select your styles")
    material = st.sidebar.selectbox("Material",["Cotton", "Plyster", "Fiber", "Denim", "Satin", "Nylon", "Silk","Wood"])
    occasion = st.sidebar.selectbox("Occasion", ["evening wear","daily wear", "formal wear", "informal wear", "durable wear", "wedding dress"])
    season = st.sidebar.selectbox("Season",["winter","spring", "Summer", "Fall"])
    male_female = st.sidebar.selectbox("Male/Female", ["Male", "Female"])
    kid_Adult = st.sidebar.selectbox("Kid/Adult", ["Kid", "Adult"])
    size = st.sidebar.selectbox("Size", ["Small","Medium","Large", "Xlarge"])
    color = st.sidebar.selectbox("Select your colors", ["Red", "Green", "Blue","white", "black","yellow"])
    culture = st.sidebar.selectbox("Culture",["African","Middle east", "Western","Asian", "Berber", "Egyption"])
    item = st.sidebar.selectbox("Item", ["Abaya","Thoab","Dress", "T-shirt", "Pant", "coat"])
    Era = st.sidebar.selectbox("Era",["70's","80's" , "90's" , "20's", "2050"])
    personal_touch = st.sidebar.text_area("Add your personal touch")
    
    # Generate a detailed prompt

    prompt = f"""
    Generate an novel pattern with listed items. The pattern wiil be used on the fabric to create Saudi abaya
    - 4k image, 
    - {color}
    - {personal_touch}

    """

    # Display the prompt at the end of the sidebar
    st.sidebar.markdown(prompt)
    return material, male_female, size, occasion, season, culture, item, kid_Adult, Era,color, personal_touch


def display_main_frame(images, selected_thumbnail):
    cols = st.columns(5)

    for i, img in enumerate(images):
        with cols[i]:
            if st.button(f"image {i + 1}"):
                selected_thumbnail = i

    st.image(images[selected_thumbnail], width=700)

    # Add your image editing buttons and tools here

    return selected_thumbnail


images = [Image.open(f"image{i + 1}.jpg") for i in range(5)]
selected_thumbnail = 0


st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    material, male_female, size, occasion, season, culture, item, kid_Adult,Era, personal_touch, color= display_sidebar()
    selected_thumbnail = display_main_frame(images, selected_thumbnail)
