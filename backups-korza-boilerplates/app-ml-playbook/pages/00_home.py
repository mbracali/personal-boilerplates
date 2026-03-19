# Python default imports
import os, sys, time, platform
from datetime import datetime

# External libs import
import streamlit as st

# Local imports
from libs.playbook_objects import page_blueprint

# Page constants
PAGE_NAME = "Home"
PAGE_DESC = "home"
PAGE_EMOJI = ""
PAGE_ICON = "home"


page = page_blueprint(
    page_name=PAGE_NAME,
    page_emoji=PAGE_EMOJI,
    page_icon=PAGE_ICON,
    page_desc=PAGE_DESC
)

page.start()
