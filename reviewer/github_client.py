### File: reviewer/github_client.py

from github import Github
import re


def get_changed_code(pr_url: str, token: str):
    g = Github(token)
    match = re.match(r"https://github.com/(.*?)/(.*?)/pull/(\d+)", pr_url)
    owner, repo_name, pr_number = match.groups()
    repo = g.get_repo(f"{owner}/{repo_name}")
    pr = repo.get_pull(int(pr_number))

    changed_files = pr.get_files()
    code = {}
    for file in changed_files:
        if file.filename.endswith(".py"):
            contents = repo.get_contents(file.filename)
            code[file.filename] = contents.decoded_content.decode("utf-8")

    return code
