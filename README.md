# ☁️ Real-Time Weather Report App

 

## Project Overview

This is a real-time desktop application built with **Python** and **Tkinter** to provide up-to-the-minute weather forecasts. It integrates directly with the **OpenWeatherMap API** to fetch data and display key metrics in a simple, user-friendly graphical interface (GUI).

This project was built during my Python Developer Internship at Vault of Codes.

## ✨ Features

* **Real-Time Data:** Fetches live weather information using a robust API call.
* **Key Metrics:** Displays the weather condition (e.g., "Clear"), temperature (in Celsius), and atmospheric pressure.
* **User-Friendly GUI:** Simple interface built with `Tkinter` and `ttk.Combobox` for easy state selection.

## 🛠️ Tech Stack

* **Language:** Python
* **GUI Library:** Tkinter
* **API:** OpenWeatherMap API
* **Data Handling:** `requests` (for HTTP calls), JSON parsing

## 🚀 Getting Started

Follow these steps to get the application up and running on your local machine.

### Prerequisites

You need Python 3.x installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Roohi2204/Real-Time-Weather-App.git](https://github.com/Roohi2204/Real-Time-Weather-App.git)
    cd Real-Time-Weather-App
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the main script** (assuming your file is named `weather_app.py` or similar):
    ```bash
    python <your_script_name>.py
    ```

2.  Select a state from the dropdown menu and click **"Done"** to view the live weather report.

## 🔑 Note on the API Key

The application currently uses a sample/placeholder API key . For security and best practice, if you plan to use this application long-term or share it with others, you should register for your own free API key from OpenWeatherMap and replace the key in the Python script.
