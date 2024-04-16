from fastapi import FastAPI, APIRouter


from repos.routers import repos_router

app = FastAPI(
    title="github-parser"
    )


main_router = APIRouter(prefix="/api")

main_router.include_router(repos_router, prefix="/repos", tags=["REPOS"])


app.include_router(main_router)
