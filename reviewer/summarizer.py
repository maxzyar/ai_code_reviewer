### File: reviewer/summarizer.py

def summarize_reviews(reviews):
    summary = ""
    for item in reviews:
        summary += f"## File: {item['filename']}\n"
        summary += "\n### LLM Suggestions:\n"
        summary += item['llm']
        summary += "\n### Static Analysis:\n"
        summary += item['static']

    return summary