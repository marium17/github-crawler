import os
import requests
import time

GQL_URL = "https://api.github.com/graphql"
TOKEN = os.getenv("GITHUB_TOKEN")  # GitHub token from Actions

def query_github(after=None):
    q = """
    query ($after: String) {
      search(query: "stars:>1", type: REPOSITORY, first: 100, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes {
          ... on Repository {
            databaseId
            nameWithOwner
            stargazerCount
            updatedAt
          }
        }
      }
    }
    """
    payload = {"query": q, "variables": {"after": after}}
    r = requests.post(GQL_URL, json=payload, headers={"Authorization": f"bearer {TOKEN}"})
    if r.status_code != 200:
        print("Rate limit hit or error:", r.text)
        time.sleep(10)
        return query_github(after)
    return r.json()["data"]["search"]

def fetch_repositories(limit=1000):
    after = None
    all_repos = []
    while len(all_repos) < limit:
        data = query_github(after)
        all_repos.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        after = data["pageInfo"]["endCursor"]
        time.sleep(1)
    return all_repos

