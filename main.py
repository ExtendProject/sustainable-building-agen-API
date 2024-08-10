from fastapi import FastAPI, File, UploadFile, Form
from typing import List, Dict
from pydantic import BaseModel
import google.generativeai as genai
import os
from PIL import Image
import json
import io
from fastapi.middleware.cors import CORSMiddleware
from prompts.prompts import MainPrompt
from config.config import GEMINI_API_KEY

# Configure the GenAI client
genai.configure(api_key=GEMINI_API_KEY)

# Define the FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the allowed origins here
    # allow_origins=["https://gipc-gamma.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request model using Pydantic
class UserDetails(BaseModel):
    user_name: str
    budget: int
    location: str
    current_weather_condition: str

# Define the response schema
class ResponsSchema(BaseModel):
    materials_objects_tools: str
    observed_in_images: str
    sustainable_alternative: str
    found_alternatives_from_market: str
    const_efficient: str
    notes: str
    budget_allocation: str
    recommendations: str

class MainResponse(BaseModel):
    user_name: str
    budget: int
    final_remarks: str
    remaining_amount_form_budget: int
    total_estimated_spendings: int
    results: List[ResponsSchema]

# Define the model configuration
model = genai.GenerativeModel('gemini-1.5-flash', generation_config={
    "response_mime_type": "application/json",
    "response_schema": MainResponse
})

# Load product data from a JSON file
with open('./building_construction_products.json') as f:
    product_data = json.load(f)
    

# Endpoint to process user details and images
@app.post("/analyze")
async def analyze_construction(
    user_name: str = Form(...),
    budget: int = Form(...),
    location: str = Form(...),
    current_weather_condition: str = Form(...),
    images: List[UploadFile] = File(...)
):
    # Process the uploaded images
    pil_images = []
    for image in images:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))
        pil_images.append(pil_image)
        

    # Prepare the prompt for the model
    prompt = MainPrompt(user_name,budget,location,current_weather_condition,product_data)
    
    # Call the Generative AI model
    response = model.generate_content([prompt, *pil_images])
    # Parse the JSON response
    json_response = json.loads(response.text)

    return json_response

