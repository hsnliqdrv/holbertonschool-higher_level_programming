#!/usr/bin/python3
"""
A simple templating program that generates personalized invitations.
"""

import os


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees."""

    # Validate input types
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Handle empty template or list
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, person in enumerate(attendees, start=1):
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key)
            if value is None:
                value = "N/A"
            filled_template = filled_template.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
