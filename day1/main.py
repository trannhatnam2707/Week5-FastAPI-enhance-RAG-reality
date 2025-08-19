import httpx
from fastapi import FastAPI

from Middleware import log_request_time


app = FastAPI()

#đăng ký middleware

app.middleware("http")(log_request_time)

#route tra cứu thời tiết 
@app.get("/weather/{city}")
async def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"  # API miễn phí (không cần key)

    #gọi API ngoài với async HTTP client
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()

    #trích xuất dữ liệu cơ bản
    current_temp = data["current_condition"][0]["temp_C"]   
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    return {
        "city": city,
        "temperature": f"{current_temp}°C",
        "description": desc
    }