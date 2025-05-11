import base64
from openai import OpenAI
client = OpenAI()

img = client.images.generate(
    model="dall-e-3",
    prompt="pixel art of a 2d game cat character. black and gray cat. no background",
    n=1,
    size="1024x1024"
)

image_url = img.data[0].url
print(image_url)

# download
import requests
data = requests.get(image_url).content
with open('test.jpg', 'wb') as handler:
    handler.write(data)