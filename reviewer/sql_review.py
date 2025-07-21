# Add SQL review to static analysis
from reviewer.sql_analysis import analyze_sql_format


def run_sql_review(filename, code):
    if filename.endswith('.sql'):
        return analyze_sql_format(code)
    return None
