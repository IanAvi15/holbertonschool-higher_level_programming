#!/usr/bin/python3
"""Simple templating program that generates invitation files."""
import os


def generate_invitations(template, attendees):
    """Generate invitation files from a template and list of attendees."""
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if len(template) == 0:
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        result = template
        for key in ("name", "event_title", "event_date", "event_location"):
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            result = result.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, "w") as f:
            f.write(result)