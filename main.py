### File: main.py

from reviewer.github_client import get_changed_code
from reviewer.llm_reviewer import review_with_llm
from reviewer.static_analysis import run_static_analysis
from reviewer.summarizer import summarize_reviews
from reviewer.notifications.slack import send_to_slack
from reviewer.sql_review import run_sql_review
import os


def main(pr_url):
    token = os.getenv("GITHUB_TOKEN")
    code_files = get_changed_code(pr_url, token)

    all_reviews = []
    for filename, code in code_files.items():
        llm_comments = review_with_llm(filename, code)
        static_comments = run_static_analysis(filename, code)
        sql_comments = run_sql_review(filename, code)
        all_reviews.append({
            "filename": filename,
            "llm": llm_comments,
            "static": static_comments,
            "sql": sql_comments
        })

    # Message content
    summary = summarize_reviews(all_reviews)

    # Slack
    send_to_slack(f"📣 Code Review Summary:\n\n{summary}")

    print("===REVIEW_START===")
    print(all_reviews)  # Your markdown-style review string
    print("===REVIEW_END===")



if __name__ == "__main__":
    import sys
    pr_url = sys.argv[1]
    main(pr_url)
