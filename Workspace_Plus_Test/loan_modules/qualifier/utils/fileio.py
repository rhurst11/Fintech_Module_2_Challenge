# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):

    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(user_save_path_ouput, qualifying_loans):

    """Writes to a csv file

    Args: 
    user_save_path_ouput: the desired output path for the new csv content
    qualifying_loans: the data to be written into the csv file

    """

    #qual_loanscsv_output_path = questionary.text("Please the desired path for your new saved csvfile").ask()\
    header = ["Lender", "Loan Amount,Max", "LTV,Max", "DTI,Min", "Credit Score", "Interest Rate"]
    #currently written to intake output path from save_qualifying_loans() in app.py
    with open (user_save_path_ouput, 'w', newline='') as user_qual_loans_csvfile:
        user_qual_loans_csvwriter = csv.writer(user_qual_loans_csvfile)
        user_qual_loans_csvwriter.writerow(header)
        for row in qualifying_loans:
            user_qual_loans_csvwriter.writerow(row)