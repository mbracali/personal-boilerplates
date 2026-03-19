# Python default imports
import os, sys, time, platform
from datetime import datetime

# External libs import
import streamlit as st

# App modules import
from modules.streamlit_extras import PageBlueprint

# Page constants
title = "Home"
description = "Home page of the boilerplate app"
material_icon = "home:"

# Page object
page = PageBlueprint(page_title = title,
    page_description = description,
    page_material_icon = material_icon,
    )

# Build page
page.build()