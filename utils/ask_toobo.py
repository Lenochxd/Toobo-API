import json
import os

from . import get_meteo
from openai import OpenAI

# Load the configuration
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)
    API_KEY = config['apis'].get('OpenAI')
    client = OpenAI(api_key=API_KEY)

with open('config/output_example.txt', 'r') as file:
    exemple = file.read()


def resume_weather() -> str:
    weather_data = get_meteo.get_weather_all_cities()
    print('Weather Data:', weather_data)
    print()
    
    if not weather_data:
        return
    
    prompt = f"""
You are a friendly, cheerful, and human-like assistant summarizing weather information.
You are Toobo from [La météo de Gulli](https://fr.wikipedia.org/wiki/La_M%C3%A9t%C3%A9o_de_Gulli)! (male)
Please write your response in French.

Here's an example output:

```{exemple}```

For each city, check if the information is available in the provided data. If it is, provide the weather and clothing advice in a warm and friendly way.
If it is not, inform that the specific information is not available in a kind and clear manner, and suggest consulting local forecasts.


Please summarize the following weather data for multiple cities according to the example output.
Keep the tone friendly, cheerful, and human-like, as if you are Toobo from [La météo de Gulli](https://fr.wikipedia.org/wiki/La_M%C3%A9t%C3%A9o_de_Gulli)! 
Toobo is for kids, so avoid statistics. They just want to know if it's sunny, cloudy, or not,
and more importantly, what they should wear. If information is not available for a city, let them know in a kind and clear manner.
If the information is available, make sure to provide it accurately and warmly!
End with a summary, just like in the example.

Please write your response in French.

Here is the data:
```json
{weather_data}
```
"""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    output = response.choices[0].message.content.strip()
    
    print(output)
    return output

def save_resume(text: str, date: str):
    if not os.path.exists("data"):
        os.makedirs("data")
        
    with open(f"data/{date}.json", "w", encoding="utf-8") as file:
        json.dump({'text': text}, file, ensure_ascii=False, indent=4)
        

if __name__ == '__main__':
    print(resume_weather())