import streamlit as st
import streamlit.components.v1 as components

def set_page_config() :
    st.set_page_config(
        page_title="CP Ordering",
        layout='wide',
        initial_sidebar_state="expanded"
    )

def main() :
    set_page_config()

    with open("src/components/draggable_component.html") as f:
        components.html(f.read(), height=600)


if __name__ == "__main__" :
    main()