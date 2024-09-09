from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from generate import generate_response  # Import the function to generate responses

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve the homepage (index.html)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint for generating responses from DialoGPT
@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, input_text: str = Form(...)):
    # Call the generate_response function from generate.py
    generated_responses = generate_response(input_text)
    
    # Return the page with the generated response
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "input_text": input_text, 
        "generated_responses": generated_responses
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
