from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from reviewer.github_client import get_changed_code
from reviewer.llm_reviewer import review_with_llm
from reviewer.static_analysis import run_static_analysis
from reviewer.sql_review import run_sql_review
from reviewer.summarizer import summarize_reviews
from reviewer.notifications.slack import send_to_slack
from main import post_comment_to_pr

load_dotenv()

app = FastAPI(title="AI Code Reviewer API")

class PRReviewRequest(BaseModel):
    pr_url: str

class PRReviewResponse(BaseModel):
    summary: str
    all_reviews: list

@app.post("/review", response_model=PRReviewResponse)
def review_pull_request(request: PRReviewRequest):
    token = os.getenv("GITHUB_TOKEN")
    code_files = get_changed_code(request.pr_url, token)
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
    summary = summarize_reviews(all_reviews)
    send_to_slack(f"📣 Code Review Summary:\n\n{summary}")
    
    # Post review as a comment to the PR
    review_lines = []
    for review in all_reviews:
        filename = review["filename"]
        llm_section = "**🧠 LLM Review:**\n" + ("\n".join(review["llm"]) if isinstance(review["llm"], list) else str(review["llm"])) if review["llm"] else "_No LLM feedback._"
        static_section = "**🔍 Static Analysis:**\n" + ("\n".join(review["static"]) if isinstance(review["static"], list) else str(review["static"])) if review["static"] else "_No static analysis feedback._"
        sql_section = "**🛢️ SQL Review:**\n" + ("\n".join(review["sql"]) if isinstance(review["sql"], list) else str(review["sql"])) if review["sql"] else "_No SQL review feedback._"
        section = f"""### `{filename}`\n\n{llm_section}\n\n{static_section}\n\n{sql_section}\n"""
        review_lines.append(section)
    full_review = "## 🤖 Automated Code Review\n\n" + "\n\n---\n\n".join(review_lines)
    post_comment_to_pr(request.pr_url, full_review)
    
    return PRReviewResponse(summary=summary, all_reviews=all_reviews)
