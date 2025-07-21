### File: reviewer/summarizer.py

def summarize_reviews(reviews):
    for item in reviews:
        print(f"## File: {item['filename']}")
        print("\n### LLM Suggestions:\n")
        print(item['llm'])
        print("\n### Static Analysis:\n")
        print(item['static'])