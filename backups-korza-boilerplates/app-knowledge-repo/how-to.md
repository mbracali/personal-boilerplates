
# Knowledge repo instructions and structure

Here you should find all the documents created for each project and customer.
Have in mind that this is still manual, it depends on users to update, there is no automated data comming from nowhere.

## How to add a new customer

* Clone this repo;
* Create a new branch;
    * We recomend the gitflow standard: `feature/customer-<customer-name>`
* On your terminal, run the command: `make customer <customer-name>`;
* This will create a new folder inside 'customers' with the customer name and a README.md file;
    * The created file is a template, you need to fill the info of the customer;
* Remember to remove template tags, otherwize the document will not be included in applications that can read this repo;
* After all changes, push your changes to the repo and create your PR when you are done;


## How to add a new project

* Clone this repo;
* Create a new branch;
    * We recomend the gitflow standard: `feature/project-<project-name>`
* On your terminal, run the command: `make project <project-name>`;
* This will create some folders and some files inside the repo;
    * All the files are templates, make sure to fill with project info;
    * See a representation of the project structure folder at the end of this section;
* Remember to remove template tags, otherwize the document will not be included in applications that can read this repo;
* After all changes, push your changes to the repo and create your PR when you are done;

Folder structure of a project:
``` Plaintext
project-xyz/
├── README.md                 # Main README of the project, the starting point for any user
├── executive-report.md       # Executive report of the project, ideal for reporting to the executive/sales team
└── project-details/          # Folder with all the project details
    ├── phase-1.md            # Details about the phase 1 of the project
    ├── phase-2.md            # Details about the phase 2 of the project
    ├── ...                   # If your project have more phases, copy the templates
    ├── progress-report.md    # Report with the progress of the project, expect more details than the executive report
    └── deep-dive/            # Folder dedicated to store artifacts and other documents, focused on deepdives
        ├── index.md          # Index with all the artifacts collected during the project (and some explanation)
        ├── databases/        # Folder with all the databases collected during the project
        ├── emails/           # Folder with all the emails collected during the project
        ├── imgs/             # Folder with all the images collected during the project
        ├── notebooks/        # Folder with all the notebooks collected during the project
        ├── other/            # Folder with all the other artifacts collected during the project
        └── querys/           # Folder with all the querys collected during the project
```

## FAQ:

* No questions so far!