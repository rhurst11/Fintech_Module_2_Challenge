# Module 2 Challenge: Expanding My Loan Qualifier Application

This application allows a user to input CSV data of different loans along with some of their own finanical information, and subsequently view a series of loans that they qualify for. The user may also save the data of their qualifying loans as a CSV file. All of the user-application dialogue occurs within a Command Line Interface, and prompts the user to input information when necessary. 

---

## Technologies

This programs uses the following:

### Language: 
* Python

### Imported Libraries:
* csv
* sys
* questionary
* fire 
* pytest
* Path from pathlib

### Versions Used In Program:
Fire 0.4.0
Questionary 1.9.0
PyTest 6.2.4
Python 3.7.10
---

## Installation Guide

You will need to install the following software versions within your terminal interface: 

### Installation Steps In Order: 

* conda activate dev
* pip install fire
* pip install questionary
* pip install pytest

---

## Usage

Navigate to Workspace_Plus_test/loan_modules/app.py  to begin program

Will be prompted to enter series of financial info via command line interface. When prompted for Path, use absolute path

Will be given option to save a csv file of your qualifying loans if the number of qualifying loans is > 0

If program is fed a valid path for the output file, will be able to view the new csv of qualifying loans accordingly


---

## Contributors

Raymond Hurst - rhurst1125@berkeley.edu
---

## License

MIT license