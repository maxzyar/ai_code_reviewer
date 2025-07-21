### File: reviewer/llm_reviewer.py

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)


def review_with_llm(filename, code):
    prompt = f"""
You are a senior engineer. Review the following Python file `{filename}`.
Look for:
- Bugs
- Performance issues
- Best practices
Return your feedback in Markdown format.

```
{code}
```
"""
    response = llm([HumanMessage(content=prompt)])
    return response.content