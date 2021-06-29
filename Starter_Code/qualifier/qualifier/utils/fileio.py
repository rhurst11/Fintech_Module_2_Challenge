# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


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

#   csv lib already imported

qualifying_data = []

def save_csv(qualifying_data):
    """
    Here I am writing to a new csv file as I did in the end of module 1
    I set the output path for the newly written csv file
    I set up a csv writer
    I set up a for loop to iterate through the qualifying_data provided

    IMPORANT: qualifying_data will need to be redefined
    """
    csvpath = Path("qualifying_data.csv")
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in qualifying_data:
            csvwriter.writerow(header)
            csvwriter.writerow(row.values())