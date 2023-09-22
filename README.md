
# GUI-exercise

A short description of the project.

## Setup
Optionnal if using GIT:

1. Install git and checkout the [git code repository]

Optionnal if python project:

2. Install [anaconda]/[miniconda] python version 3.6+
3. Change working directory the project root directory
4. Create the self contained conda environment. Open anaconda prompt and go to the project root directory and enter the command:

    `pip install -r requirements.txt`

5. .. Place your own project specific setup steps here e.g. copying data files ...


## Using the Python Conda environment

Once the Python Conda environment has been set up, you can

* Activate the environment using the following command in a terminal window:

    * Windows: `activate my_environment`
    * Linux, OS X: `source activate my_environment`
    * The __environment is activated per terminal session__, so you must activate it every time you open terminal.

* Deactivate the environment using the following command in a terminal window:

    * Windows: `deactivate my_environment`
    * Linux, OS X: `source deactivate my_environment`
               
* Delete the environment using the command (can't be undone):

    * `conda remove --name my_environment --all`

## Initial File Structure

```
├── config                   <- Config files 
│
├── data                     <- All the data
│
├── models                   <- Trained models
│
├── reports                  <- Visual exports (Tableau, Qlik, PowerBI, Images etc.)
│
├── scripts                  <- All scripts and code snippets
│
├── src                      <- Production ready code
│
├── tests                    <- Test cases
│  
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── requirements.txt         <- Essential python packages used in the project
│  
└── README.md                <- The top-level README for developers using this project.
```

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more 
than once then it should be placed into a common script / module under src and unit tests added. The same applies for 
any other non trivial code to ensure the correct functioning.

To run tests, install pytest and then from the repository root run
 
```
pytest
```

## Development Process
Contributions to this project are greatly appreciated and encouraged.

To contribute an update simply:

* Create a new branch / fork for your updates.
* Check that your code follows the PEP8 guidelines (line lengths up to 120 are ok) and other general conventions within this document.
* Ensure that as far as possible there are unit tests covering the functionality of any new code.
* Update the yml file for the python environment if new packages are installed
* Check that all existing unit tests still pass.
* Edit this document if needed to describe new files or other important information.
* Create a pull request.

## Contacts
* Author: Agilytic
* Agilytic team: Jeroen Lardot
* Client: Not defined

## References
* https://jerome_belp@bitbucket.org/jerome_belp/cookiecutter-agilytic.git - The master template for this project
* http://docs.python-guide.org/en/latest/writing/structure/
* https://drivendata.github.io/cookiecutter-data-science/

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
   [miniconda]: <https://docs.conda.io/en/latest/miniconda.html>
