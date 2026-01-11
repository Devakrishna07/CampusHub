# core/constants.py
"""
Contains application-wide constants.
Used across multiple apps to avoid magic strings.
"""

USER_ROLES = (
    ('ADMIN', 'Admin'),
    ('JUDGE', 'Judge'),
    ('COORDINATOR', 'Coordinator'),
    ('HOUSE_CAPTAIN', 'House Captain'),
    ('EVALUATOR', 'Evaluator'),
    ('EDITOR', 'Editor'),
    ('VOLUNTEER', 'Volunteer'),
)

ROUND_TYPES = (
    ('PRELIM', 'Preliminary'),
    ('QUARTER', 'Quarter Final'),
    ('SEMI', 'Semi Final'),
    ('FINAL', 'Final'),
)
