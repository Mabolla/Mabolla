import os, requests, sys
TOKEN = os.environ.get("GITHUB_TOKEN")
HEADERS = {"Accept":"application/vnd.github+json"}
if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"
API = "https://api.github.com"

def paged_get(url, params=None):
    results=[]; page=1
    while True:
        r = requests.get(url, headers=HEADERS, params={**(params or {}), "per_page":100, "page":page})
        if r.status_code!=200:
            sys.exit(f"Error {r.status_code}")
        batch=r.json()
        if not isinstance(batch, list): return batch
        results.extend(batch)
        if len(batch)<100: break
        page+=1
    return results

def main(user):
    repos=paged_get(f"{API}/users/{user}/repos", {"type":"owner"})
    total_repos=len(repos)
    total_stars=sum(r["stargazers_count"] for r in repos)

    md=[f"## 📊 GitHub Stats for {user}", "", 
        f"- Public repos: **{total_repos}**", 
        f"- Total stars: **{total_stars}**", ""]

    md.append("| Repo | Stars |")
    md.append("|------|-------|")
    for r in repos:
        md.append(f"| [{r['name']}](https://github.com/{user}/{r['name']}) | {r['stargazers_count']} |")
    print("\n".join(md))

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: stats.py <github_username>")
        sys.exit(1)
    main(sys.argv[1])
