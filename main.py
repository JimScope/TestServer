from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import BackgroundTasks
import time

app = FastAPI()

html_content = """
<html>
<head>
<script>
function changeColor(color) {
    document.body.style.backgroundColor = color;
}
</script>
</head>
<body>
<h1>FastAPI Color Change</h1>
</body>
</html>
"""


def change_color(color, data):
    html = f"<html><head><script>changeColor('{color}');</script></head><body>{ data }</h1></body></html>"
    return HTMLResponse(content=html, status_code=200)


def reset_color(background_color):
    time.sleep(5)  # Sleep for 5 seconds before resetting the color
    change_color(background_color, {})


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/test_endpoint")
async def test_endpoint(data: dict, background_tasks: BackgroundTasks):
    try:
        background_color = "#FFFFFF"  # White is the default background color

        # Change color and schedule reset in the background
        background_tasks.add_task(reset_color, background_color)

        return change_color("#FF0000", data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
