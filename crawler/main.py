from crawler.db import setup_schema, insert_repo, export_to_csv
from crawler.github_api import fetch_repositories

def crawl_repos():
    setup_schema()
    repos = fetch_repositories()

    for repo in repos:
        name = repo["nameWithOwner"]
        stars = repo["stargazerCount"]
        insert_repo(name, stars)

    export_to_csv()
    print("✅ Data saved to repos.db and exported to repos.csv")

if __name__ == "__main__":
    crawl_repos()

