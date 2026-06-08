#!/usr/bin/python3
"""Module that provides a function to convert a CSV file to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write the result to data.json.

    Args:
        csv_filename (str): The path to the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f)
        return True
    except FileNotFoundError:
        return False
