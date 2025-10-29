from tkinter import *
from tkinter import ttk
import requests

def data_get():
    # 1. Get the city name from the Combobox
    city = city_name.get()
    
    # 2. Fetch data from OpenWeatherMap API
    # Note: API key is embedded here. The city is passed via the 'q' parameter.
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
    + city + "&appid=cd428c80e2bb37333a664f4b919b77af").json()
    
    # 3. Update output labels
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    
    # Convert temperature from Kelvin (API default) to Celsius (Kelvin - 273.15)
    tem_label1.config(text=int(data["main"]["temp"] - 273.15))
    
    per_label1.config(text=data["main"]["pressure"])

# --- Main Window Setup ---
win = Tk()
win.title("Weather Report")
win.config(bg="sky blue")

# This line has been commented out to prevent crashing due to hardcoded absolute path.
# image = PhotoImage("C:\\Users\\roohi\\Downloads\\61nuuPxUvaL.png")

win.geometry("500x570")

# Title Label
labelname = Label(win, text="WEATHER FORECAST", fg="blue", bg="yellow", 
                  font=("Time New Roman", 30, "bold"))
labelname.place(x=25, y=50, height=50, width=450)

# City Selection (Combobox)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat",
             "Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala",
             "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
             "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
             "Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh",
             "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
             "National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, text="WEATHER APP", values=list_name, 
                   font=("Time New Roman", 15, "bold"), textvariable=city_name)
com.place(x=30, y=120, height=50, width=450)

# --- Output Labels Setup ---

# Weather Climate
w_label = Label(win, text="Weather Climate", font=("Time New Roman", 17))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
w_label1.place(x=250, y=260, height=50, width=210)

# Weather Description
wb_label = Label(win, text="Weather Description", font=("Time New Roman", 17))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
wb_label1.place(x=250, y=330, height=50, width=210)

# Temperature
tem_label = Label(win, text="Temperature", font=("Time New Roman", 17))
tem_label.place(x=25, y=400, height=50, width=210)
tem_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
tem_label1.place(x=250, y=400, height=50, width=210)

# Pressure
per_label = Label(win, text="Pressure", font=("Time New Roman", 17))
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
per_label1.place(x=250, y=470, height=50, width=210)

# Done Button
done_button = Button(win, text="Done", font=("Time New Roman", 25, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()