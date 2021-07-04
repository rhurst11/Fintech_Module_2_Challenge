# Import pathlib
from pathlib import Path

#Import PyTest

import pytest

#Import fileio
from loan_modules.qualifier.utils import fileio

#Workspace_Plus_Test/loan_modules/qualifier/utils/fileio.py

# # # Import Calculators
from loan_modules.qualifier.utils import calculators

# # # Import Filters
from loan_modules.qualifier.filters import credit_score
from loan_modules.qualifier.filters import debt_to_income
from loan_modules.qualifier.filters import loan_to_value
from loan_modules.qualifier.filters import max_loan_size


# Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

# def test_filters():
#     bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
#     current_credit_score = 750
#     debt = 1500
#     income = 4000
#     loan = 210000
#     home_value = 250000

#     monthly_debt_ratio = 0.375

#     loan_to_value_ratio  = 0.84

# Test the new save_csv code!
def test_save_csv_local():
    user_save_path_ouput = fileio.save_csv(Path(' .your_pytest_loans'), qualifying_loans = ["Test", "Testing", "Tested"])
# have confirmed save_csv is writing


# 'loan_modules/data/output/qualifying_loans.csv'
def test_save_csv_extra():
    user_save_path_ouput = fileio.save_csv(Path('../loan_modules/data/output/qualifying_loans.csv'), qualifying_loans = ["Test", "Testing", "Tested"])