import aiohttp
import asyncio
from repos.schemas import ShowRepo

BASE_URL = "https://api.github.com"
ALLOWED_SORTS = ["stars", "forks", "help-wanted-issues", "updated"]

async def search_repos(
    q="stars:>1",
    per_page=100,
    sort="stars" # it can be one of: stars, forks, help-wanted-issues, updated
) -> list:
    if sort not in ALLOWED_SORTS: 
        raise Exception() # TODO: write exception for this error (sort not in ALLOWED_SORTS)
    url = f"https://api.github.com/search/repositories?sort={sort}&q={q}&per_page={per_page}"
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            if resp.status == 200:
                data = (await resp.json())['items']
                return data
            else:
                raise Exception() # TODO: write exception for this error (not 200 from api.github.com)
            
async def get_top100_by_stars_repos() -> ShowRepo:
    repos = await search_repos()
    return [ShowRepo(
        repo=repo["full_name"],
        owner=repo["owner"]["login"],
        stars=int(repo["stargazers_count"]),
        watchers=int(repo["watchers"]),
        forks=int(repo["forks"]),
        open_issues=int(repo["open_issues_count"]),
        language=repo["language"]
    ) for (index, repo) in enumerate(repos)]

async def main():
    data =  await get_top100_by_stars_repos()
    for i in data:
        print(data)
    
if __name__ == "__main__":
    asyncio.run(main())
    
