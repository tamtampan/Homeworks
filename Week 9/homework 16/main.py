from starlette.responses import RedirectResponse
from init_app import app
import uvicorn


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
