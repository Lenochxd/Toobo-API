import os
import json
from fastapi import FastAPI

from utils.get_meteo import get_tomorrow_date
from utils import ask_toobo

app = FastAPI()


@app.get("/API/toobo/get_weather_resume")
async def resume_weather(date: str = get_tomorrow_date()):
    date = date.replace("/", "-")

    file_path = f"data/{date}.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                pass
        os.remove(file_path)
        
    if date != get_tomorrow_date():
        return {"error": "Weather data for the requested date is not available"}
    resume = ask_toobo.resume_weather()
    ask_toobo.save_resume(resume, date)

    return {'text': resume}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
