import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeatherMap API key
api_key = "be772309d9eddc1360f8b2e1c6760eea"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {"q": city, "appid": "be772309d9eddc1360f8b2e1c6760eea", "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"Temperature: {temperature}°C\nDescription: {weather_description}"
    except Exception as e:
        return f"Error: {e}"

def get_weather_for_city():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        result_label.config(text=weather_info)
    else:
        messagebox.showwarning("Input Error", "Please enter a city.")

# GUI setup
root = tk.Tk()
root.title("Weather Forecast App")

# City entry
city_label = tk.Label(root, text="Enter City:")
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

city_entry = tk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Get Weather button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_for_city)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
