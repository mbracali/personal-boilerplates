# Variables - APP
APP_NAME      := app-knowledge-repo
APP_VERSION   := 0.1.0

# Variables - locations
ROOT_DIR      := $(CURDIR)
TEMPLATES_DIR := $(ROOT_DIR)/.templates

# Variables - dates
DATE          := $(shell date +"%Y-%m-%d")

# Params - capture
PARAM         := $(word 2, $(MAKECMDGOALS))

# Fix the customer name for the doc | Replace - or _ to space
CUST_NAME     := $(shell echo "$(PARAM)" | tr '_-' ' ' | tr '[:upper:]' '[:lower:]')

# Magic Eval: Prevents Make from treating the parameter as a target
$(eval $(PARAM):;@:)

# Create a new customer inside the knowledge repo
customer:
# Create customer folder
	@echo "> Creating folder at ./customers/$(PARAM)"
	@mkdir -p $(CURDIR)/customers/$(PARAM)
# Copying template
	@echo "> Copying profile template"
	@cp -r $(TEMPLATES_DIR)/0-customers-general-root-README.md $(CURDIR)/customers/$(PARAM)/README.md
# Replacing variables
	@echo "> Filling profile template"
	@sed -i '' 's/{!CUSTOMER_NAME}/$(CUST_NAME)/g' $(CURDIR)/customers/$(PARAM)/README.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/customers/$(PARAM)/README.md 
	@echo "> Customer documentation initialized successfully"

# Create a new project inside the knowledge repo
project:
# Test if the initial parameter is valid
	@if [ -z "$(PARAM)" ]; then \
		echo "*** Error: No name for the project was provided."; \
		echo "*** Try: make project <name>"; \
		echo "*** "; \
		echo "*** "; \
		exit 1; \
	fi
# If there is already a folder with the same name, warn the user and exit
	@if [ -d "$(CURDIR)/projects/$(PARAM)" ]; then \
		echo "*** Error: A project with the name '$(PARAM)' already exists."; \
		echo "*** "; \
		echo "*** "; \
		exit 1; \
	fi
# Create project folders
	@echo "> Creating folders at ./projects/$(PARAM)/..."
	@mkdir -p $(CURDIR)/projects/$(PARAM)
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/emails
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/imgs
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/notebooks
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/databases
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/querys
	@mkdir -p $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/other
# Copying templates
	@echo "> Copying templates"
	@cp -r $(TEMPLATES_DIR)/0-projects-general-root-README.md $(CURDIR)/projects/$(PARAM)/README.md
	@cp -r $(TEMPLATES_DIR)/1-projects-general-report-executive.md $(CURDIR)/projects/$(PARAM)/executive-report.md
	@cp -r $(TEMPLATES_DIR)/2-projects-general-report-progress.md $(CURDIR)/projects/$(PARAM)/project-details/progress-report.md
	@cp -r $(TEMPLATES_DIR)/3-projects-detail-phase-n.md $(CURDIR)/projects/$(PARAM)/project-details/phase-1.md
	@cp -r $(TEMPLATES_DIR)/3-projects-detail-phase-n.md $(CURDIR)/projects/$(PARAM)/project-details/phase-2.md
	@cp -r $(TEMPLATES_DIR)/4-projects-deepdive-index.md $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/index.md
# Replacing placeholders
	@echo "> Filling templates"
	@sed -i '' 's/{!PROJECT_NAME}/$(PARAM)/g' $(CURDIR)/projects/$(PARAM)/README.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/projects/$(PARAM)/README.md
	@sed -i '' 's/{!PROJECT_NAME}/$(PARAM)/g' $(CURDIR)/projects/$(PARAM)/executive-report.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/projects/$(PARAM)/executive-report.md
	@sed -i '' 's/{!PROJECT_NAME}/$(PARAM)/g' $(CURDIR)/projects/$(PARAM)/project-details/progress-report.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/projects/$(PARAM)/project-details/progress-report.md
	@sed -i '' 's/{!PROJECT_NAME}/$(PARAM)/g' $(CURDIR)/projects/$(PARAM)/project-details/phase-1.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/projects/$(PARAM)/project-details/phase-1.md
	@sed -i '' 's/{!PHASE_NUMBER}/1/g' $(CURDIR)/projects/$(PARAM)/project-details/phase-1.md
	@sed -i '' 's/{!PROJECT_NAME}/$(PARAM)/g' $(CURDIR)/projects/$(PARAM)/project-details/phase-2.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/projects/$(PARAM)/project-details/phase-2.md
	@sed -i '' 's/{!PHASE_NUMBER}/2/g' $(CURDIR)/projects/$(PARAM)/project-details/phase-2.md
	@sed -i '' 's/{!PROJECT_NAME}/$(PARAM)/g' $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/index.md
	@sed -i '' 's/{!DOC_DATE}/$(DATE)/g' $(CURDIR)/projects/$(PARAM)/project-details/deep-dive/index.md
	@echo "> Project documentation initialized successfully"

help:
	@echo

# This catches any target name (%) that wasn't matched above
%:
	@echo "Error: '$(MAKECMDGOALS)' is not a valid command."
	@echo "Try running 'make help' to see what you can do."