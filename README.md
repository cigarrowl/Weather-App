# Weather-App
# 🌍 Aura Weather App

A sleek, lightweight web application built with **Python**, **Flask**, and modern **CSS3** that provides real-time weather information and conditions for cities worldwide using the OpenWeatherMap API.

---

## ✨ Features

- 🌡️ **Real-Time Weather Data:** Get accurate live temperature, "Feels Like" temperature, humidity, and wind speed.
- 🎨 **Modern & Responsive UI:** Clean card layout styled with custom CSS, soft shadows, and smooth hover effects.
- 🌤️ **Dynamic Condition Emojis:** Automatically displays matching weather emojis based on the current weather (☀️ Clear, 🌧️ Rain, ☁️ Clouds, etc.).
- ⚠️ **Built-in Error Handling:** Graceful error popups and alerts for invalid city names or network issues.
- 🚀 **Vercel Ready:** Pre-configured for seamless deployment to Vercel with a free domain.

---

## 📂 Project Structure

```text
weather-app/
│
├── app.py              # Flask server backend & API handler
├── requirements.txt    # Python dependency package list
├── vercel.json         # Vercel deployment configuration
│
├── templates/
│   └── index.html      # HTML structure & Jinja2 templates
│
└── static/
    └── style.css       # Custom CSS styling & responsive layout