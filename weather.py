
from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox
import time

def get_data():
    city = city_name.get()
    try:
        # Making the API request
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=42629823726130805846f3cbf952b277").json()
        
        # Displaying the weather data
        weather_result.config(text=data['weather'][0]["main"])
        weather_des_result.config(text=data["weather"][0]["description"])
        
        # Convert from Kelvin to Celsius
        temp_celsius = data["main"]["temp"] - 273.15
        weather_temp_result.config(text=str(round(temp_celsius, 2)) + " °C")
        
        weather_temp_min_result.config(text=str(data["wind"]["speed"]) + " km/h")
        weather_temp_max_result.config(text=str(data["main"]["humidity"]) + " %")
        
        # Check for rain and display a normal or high alert
        if(city=="Rajasthan"):
             if "rain" in data:
                 rain_volume = data['rain'].get('1h', 0)  # Rain volume in the last 1 hour
                 if rain_volume > 10:  # Adjust threshold as needed (10mm as example)
                     messagebox.showwarning("High Rain Alert", "Heavy rain detected! Volume: " + str(rain_volume) + " mm in the last hour.\nConsider closing schools and colleges.")
                 else:
                     messagebox.showinfo("Weather Alert", "It's raining lightly. Volume: " + str(rain_volume) + " mm in the last hour.")
    
    except KeyError:
        # Handle the case where the city is not found or data is missing
        weather_result.config(text="Data not found")
        weather_des_result.config(text="Data not found")
        weather_temp_result.config(text="Data not found")
        weather_temp_min_result.config(text="Data not found")
        weather_temp_max_result.config(text="Data not found")

def continuous_update(interval=900000):  # 900,000 milliseconds = 15 minutes
    get_data()
    root.after(interval, continuous_update)

root = Tk()
root.geometry("700x600+0+0")
root.resizable(False, False)
root.configure(bg='#d9e4f5')

# Title label
title_app = Label(root, text="Weather App", font=('times new roman', 30, 'bold'), bg='#283593', fg='white', relief=SUNKEN, borderwidth=3)
title_app.pack(pady=20)

# Combobox for selecting city
city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
citybox = ttk.Combobox(root, font=('times new roman', 20), value=list_name, textvariable=city_name)
citybox.place(x=200, y=100, height=40, width=300)
city_name.set('Rajasthan')  # Set default value to 'Rajasthan'

# Weather Climate field
weather_text = Label(root, text="Weather Climate:", font=('times new roman', 18), bg='#d9e4f5')
weather_text.place(x=80, y=180, height=40, width=200)
weather_result = Label(root, text="", font=('times new roman', 18), bg='#00a2ff', fg='white', relief=SOLID, borderwidth=2)
weather_result.place(x=300, y=180, height=40, width=250)

# Weather Description field
weather_description = Label(root, text="Description:", font=('times new roman', 18), bg='#d9e4f5')
weather_description.place(x=80, y=240, height=40, width=200)
weather_des_result = Label(root, text="", font=('times new roman', 18), bg='#00a2ff', fg='white', relief=SOLID, borderwidth=2)
weather_des_result.place(x=300, y=240, height=40, width=250)

# Temperature field
weather_temp = Label(root, text="Temperature:", font=('times new roman', 18), bg='#d9e4f5')
weather_temp.place(x=80, y=300, height=40, width=200)
weather_temp_result = Label(root, text="", font=('times new roman', 18), bg='#00a2ff', fg='white', relief=SOLID, borderwidth=2)
weather_temp_result.place(x=300, y=300, height=40, width=250)

# Wind Speed field
weather_temp_min = Label(root, text="Wind Speed:", font=('times new roman', 18), bg='#d9e4f5')
weather_temp_min.place(x=80, y=360, height=40, width=200)
weather_temp_min_result = Label(root, text="", font=('times new roman', 18), bg='#00a2ff', fg='white', relief=SOLID, borderwidth=2)
weather_temp_min_result.place(x=300, y=360, height=40, width=250)

# Humidity field
weather_temp_max = Label(root, text="Humidity:", font=('times new roman', 18), bg='#d9e4f5')
weather_temp_max.place(x=80, y=420, height=40, width=200)
weather_temp_max_result = Label(root, text="", font=('times new roman', 18), bg='#00a2ff', fg='white', relief=SOLID, borderwidth=2)
weather_temp_max_result.place(x=300, y=420, height=40, width=250)

# Button to fetch weather data
btn = Button(root, text="Click Me", font=('times new roman', 20, 'bold'), bg='#283593', fg='white', relief=RAISED, borderwidth=3, command=get_data)
btn.place(x=270, y=500, height=50, width=150)

# Start continuous monitoring
continuous_update()

root.mainloop()
