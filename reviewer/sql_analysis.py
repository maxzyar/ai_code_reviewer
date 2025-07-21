# sql_analysis.py
# This module provides static analysis and formatting checks for SQL files.

import sqlparse

def analyze_sql_format(sql_code: str) -> dict:
    """
    Analyze SQL code for formatting and style issues.
    Returns a dictionary with analysis results.
    """
    formatted = sqlparse.format(sql_code, reindent=True, keyword_case='upper')
    issues = []
    if sql_code.strip() != formatted.strip():
        issues.append("SQL formatting does not match recommended style.")
    return {
        "issues": issues,
        "suggested_format": formatted
    }
