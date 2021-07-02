# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary


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

# creating initial save_csv() function

def save_csv(qualifying_loans):
    qual_loanscsv_output_path = questionary.text("Please the desired path for your new saved csvfile").ask()
    with open (qual_loanscsv_output_path, 'w', newline='') as user_qual_loans_csvfile:
        user_qual_loans_csvwriter = csv.writer(user_qual_loans_csvfile)
        for row in qualifying_loans:
            csv.writer(row)