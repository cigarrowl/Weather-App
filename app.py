from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

# Fetch API key from environment variables (fallback to yours for safety if needed)
# Safe version: only looks for the environment variable, no hardcoded key
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            city = city.strip()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                response = requests.get(url)
                data = response.json()
                
                if data.get("cod") == 200:
                    desc = data["weather"][0]["description"].lower()
                    emoji = "☀️" if "clear" in desc else "🌧️" if "rain" in desc else "☁️" if "cloud" in desc else "🌤️"
                    
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temp": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "wind": data["wind"]["speed"],
                        "description": data["weather"][0]["description"].capitalize(),
                        "emoji": emoji
                    }
                else:
                    error = "City not found. Please check the spelling."
            except Exception:
                error = "Could not connect to the weather service."
                
    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5001)