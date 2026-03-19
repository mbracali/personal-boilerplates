# Project Boilerplate

A comprehensive boilerplate template for new projects. This structure provides a well-organized foundation with different folders designed to encapsulate a wide range of project needs. Some default libraries and configurations are included to help you get started quickly.

## 📁 Folder Structure

### `/app`
Intend to store all the log files

### `/app`
All core functions and libraries for the application should be placed here.

**Subdirectories:**
- `core/` - Core functions of the app
- `libs/` - Full libraries that can be used to help and extend app functionality
- `pages/` - Visual components (created primarily for Streamlit packages, but customizable as needed)
- `utils/` - Utility modules and functions for the app

### `/assets`
Store images, sounds, and other static assets here.

### `/config`
YAML configuration files should be stored here. The structure is focused on development and production environments, but you can customize it to fit your needs.

**Default configurations:**
- `base.yaml` - Base application configuration
- `dev.yaml` - Development environment settings
- `prd.yaml` - Production environment settings

### `/data`
Folder for storing project data files.

### `/notebooks`
Used to store Jupyter notebooks. Useful for tests and ad-hoc analysis.

### `/scripts`
Intended to store system scripts (`.sh`, `.bash`, or even `.bat` for Windows).

## 🚀 Getting Started

1. Customize the configuration files in `/config` to match your project needs
2. Add your application code in `/app`
3. Place your assets in `/assets`
4. Use `/notebooks` for exploratory work and testing
5. Add deployment and system scripts to `/scripts`

---

*This is a boilerplate template - customize it to fit your specific project requirements.*
