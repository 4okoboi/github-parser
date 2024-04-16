from pydantic import BaseModel
from datetime import date
from typing import List

class ShowRepo(BaseModel):
    repo: str
    owner: str
    # position_cur: int
    # position_prev: int
    stars: int
    watchers: int
    forks: int
    open_issues: int 
    language: str | None


class ShowRepoActivity(BaseModel):
    date: date
    commits: int
    authors: List[str]
    