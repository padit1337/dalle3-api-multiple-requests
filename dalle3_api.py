import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with your API key
client = OpenAI(api_key=api_key)

# Number of times to generate an image
i = 10

for iteration in range(i):
    # Generate an image
    response = client.images.generate(
      model="dall-e-3",
      prompt="photorealistic whole, uncut, watermelon in a watermelon field",
      size="1024x1024",
      quality="standard",
      n=1, #this parameter can not be changed, as of April 2024. That is why i included the for loop. 
    )

    # Extract image URL from the response
    image_url = response.data[0].url

    # Use requests to download the image
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the image to a file with a unique name
        filename = f"dalle3_image{iteration}.png"
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Image successfully downloaded and saved as '{filename}'")
    else:
        print("Failed to download the image.")
