# Streamlit entrypoint file
# This file is the entry point for the Streamlit app.
# It fixes the Python path so all pages can import from src/modules
# without needing any path manipulation inside individual page files.

import streamlit as st
import sys, os

# Add the src/ directory to the Python path transparently
# so that "from modules.xxx import ..." works in every page file
sys.path.insert(0, os.path.dirname(__file__))

# Redirect to the home page
st.switch_page("pages/00_home.py")