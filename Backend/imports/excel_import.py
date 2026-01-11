# imports/excel_import.py
"""
Handles Excel file parsing and database insertion.
Keeps file I/O logic isolated from views.
"""

import openpyxl
from scoring.models import Score
from matches.models import Match

def import_scores_from_excel(file):
    """
    Reads an Excel file and creates Score records.

    Expected columns:
    participant_name | match_id | points | house
    """

    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active

    created = 0
    errors = []

    # Skip header row
    for row in sheet.iter_rows(min_row=2, values_only=True):
        try:
            participant_name, match_id, points, house = row

            match = Match.objects.get(id=match_id)

            Score.objects.update_or_create(
                match=match,
                participant_name=participant_name,
                defaults={'points': points}
            )

            created += 1

        except Exception as e:
            errors.append(str(e))

    return {
        "created": created,
        "errors": errors
    }
