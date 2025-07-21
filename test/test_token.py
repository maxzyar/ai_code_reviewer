from github import Github
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("GITHUB_TOKEN")
g = Github(token)

for repo in g.get_user().get_repos():
    print(repo.full_name)
