from fastapi import APIRouter
from typing import List
from repos.schemas import ShowRepo, ShowRepoActivity
from repos.services import get_top100_by_stars_repos

repos_router = APIRouter()

@repos_router.get("/top100", response_model=List[ShowRepo])
async def get_top100_repos(
    # sort: str
) -> List[ShowRepo]:
    return await get_top100_by_stars_repos()


@repos_router.get("/{owner}/{repo}/activity")
async def get_repo_activity(
    owner: str,
    repo: str
):
    return {
        "owner": owner, 
        "repo": repo
    }


