# Python default imports
import os, sys, time, platform
from datetime import datetime

# External libs import
import streamlit as st

# App modules import
from modules.streamlit_extras import PageBlueprint

# Page constants
title = "Settings"
description = "Adjust settings and see logs"
material_icon = "settings:"

# Page object
page = PageBlueprint(page_title = title,
    page_description = description,
    page_material_icon = material_icon,
    )

# Build page
page.build()