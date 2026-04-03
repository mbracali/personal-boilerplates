# Python defaults
import os, sys, random
from datetime import datetime

# Data handeling imports
import tomllib

# Streamlit import
import streamlit as st

# PageBlueprint class to build pages
class PageBlueprint:
    def __init__(self,
        page_title: str = "Page",
        page_description: str = "Welcome user!",
        page_emoji_icon: str = "📃",
        page_material_icon: str = ":material/ad:",
        page_primary_color: str = "orange",
        page_secondary_color: str = "yellow",
        page_icon_preference: str = "material",
        page_custom_footer: str = "",
        ):
        """ Class constructor has a fallback for every attribute"""
        
        # Seting class attributes
        self.page_title = page_title
        self.page_description = page_description
        self.page_emoji_icon = page_emoji_icon
        self.page_material_icon = page_material_icon
        self.page_primary_color = page_primary_color
        self.page_secondary_color = page_secondary_color
        self.page_icon_preference = page_icon_preference
        self.page_custom_footer = page_custom_footer

        # Set the prefenced icon method for this page
        if page_icon_preference == "material":
            self.page_icon = f"{page_material_icon}:"
        else:
            self.page_icon = page_emoji_icon

        # Set the page footer text
        if page_custom_footer == "":
            self.footer_text = """
        <style> .footer {position: fixed; right: 16px;
            bottom: 0; width: calc(100% - 16px);
            background: transparent; color: white;
            text-align: right;font-size: 12px;}
        </style>
        <div class="footer"> <p>Made by Korza</p></div>
        """
        else:
            self.footer_text = """
        <style> .footer {position: fixed; right: 16px;
            bottom: 0; width: calc(100% - 16px);
            background: transparent; color: white;
            text-align: right;font-size: 12px;}
        </style>
        <div class="footer"> <p>"""+self.custom_footer+"""</p></div>
        """

        # Get all sections from src/.streamlit/pages_index.toml file
        with open("src/.streamlit/pages_index.toml", "rb") as f:
            data = tomllib.load(f)
            self.app_sections = data["section"]

        # Get all pages from src/.streamlit/pages_index.toml file
        with open("src/.streamlit/pages_index.toml", "rb") as f:
            data = tomllib.load(f)
            self.app_pages = data["page"]

        # List all pages in the app/pages folder
        self.pages_files = [f for f in os.listdir("src/pages") if f.endswith(".py")]


    def _set_page_configs(self):
        """ Set main streamlit page configs """

        # Using Streamlit oficial method to set page behavior
        st.set_page_config(
            layout="wide",
            initial_sidebar_state="expanded",
            page_title=self.page_title,
            page_icon=self.page_icon,
            )


    def _build_page_footer(self):
        """ This method create a custom HTML footer for the page"""

        # Return the custom html footer
        st.markdown(self.footer_text, unsafe_allow_html=True)


    def _build_page_sidebar(self):
        """ 
        Based on the app/.streamlit/pages_index.toml file, create a 
        full sidebar, taking in consideration all the sections and
        pages defined in the file.
        """

        # Instance the sidebar component
        with st.sidebar:

            # Company logo
            st.image("src/assets/images/korza_white_no_background.png", width='stretch')
            st.markdown("---")

            # For each section in the app sections
            for section_key, section in self.app_sections.items():

                # Create a expander for the section
                with st.expander(f":{section['color']}[{section['material_icon']}] - {section['title']}", expanded=section['expanded']):
                    
                    # For each page that should be in this section
                    for page_key, page in self.app_pages.items():

                        # Test page section
                        if page["section"].lower() == section["title"].lower():

                            # Create a page link
                            st.page_link(
                                f"pages/{page['file']}", 
                                label=f":{section['color']}[{page['material_icon']}] - {page["title"]}"
                                )


    def build(self):
        """ Build the full page """

        # Set page configs
        self._set_page_configs()

        # Build page sidebar
        self._build_page_sidebar()

        # Build page footer
        self._build_page_footer()















