# Python defaults
import os, sys, random, pickle, shutil
from datetime import datetime

# Python external libs imports
import yaml

class page_blueprint:
    def __init__(self,
        page_name: str = "Playbook",
        page_emoji: str = "🤖",
        page_icon: str = "robot_2",
        page_desc: str = "Playbook page",
        custom_footer: str = "",
        custom_header: str = ""):
        """ Initialize the pages object """
        
        # Set class attributes
        self.page_name = page_name
        self.page_emoji = page_emoji
        self.page_icon = page_icon
        self.page_desc = page_desc
        self.custom_footer = custom_footer
        self.custom_header = custom_header


    def _set_page_configs(self):
        """ Set the page configs """

        # Set page configs
        st.set_page_config(
            page_title=self.page_name,
            page_icon=f":material/{self.page_icon}:",
            layout="wide",
            initial_sidebar_state="expanded",
        )


    def _set_header(self):
        """ Set the page header """

        # Set the header based on the user input
        if self.custom_header == "":
            self.custom_header = self.page_desc

        # Set default header
        head_var = f"# :blue[:material/{self.page_icon}:] {self.custom_header}"

        # Return to header
        return st.markdown(head_var)


    def _set_footer(self):
        """ Set the page footer """

        # Set the footer based on the user input
        if self.custom_footer == "":
            self.custom_footer = "Korza ML Playbook"

        # Create a string with the HTML content
        footer_html = """
        <style> .footer {position: fixed; right: 16px;
            bottom: 0; width: calc(100% - 16px);
            background: transparent; color: white;
            text-align: right;font-size: 12px;}
        </style>
        <div class="footer"> <p>"""+self.custom_footer+"""</p></div>
        """

        # Return the footer as a streamlit object for the page
        return st.markdown(footer_html, unsafe_allow_html=True)


    def _set_sidebar(self):
        """ Set the page sidebar """
        
        # Get all page files from the pages folder (only .py files)
        page_files = [f for f in os.listdir("pages") if f.endswith(".py")]

        # Sort the list of page files
        page_files.sort()

        print(page_files)

        # Return to sidebar
        return ""

    def start(self):
        """ Start the page """

        # Set page configs
        #self._set_page_configs()

        # Set page header
        #self._set_header()

        # Set page footer
        #self._set_footer()

        # Set page sidebar
        self._set_sidebar()


