# AIML Weather Assistant 🌤️

Welcome to my AI Weather Assistant project! 

For this project, I built a smart Python program that predicts the weather based on temperature and humidity. Instead of relying on complex machine learning math (like a trained `.pkl` file), I designed a **Rule-Based Expert System**. This means the "brain" of my AI makes decisions using strict, logical rules that I wrote myself!

It doesn't just guess the weather, though—it also acts as a data logger. Every time you use it, it saves your inputs, learns the historical averages, and draws charts to show how the weather is changing over time.

## ✨ What Makes It Cool
* **Custom AI Logic:** Uses a clean, rule-based decision tree (`model_logic.py`) to figure out if it's Sunny, Cloudy, Rainy, Snowy, or Cold.
* **It Remembers:** It automatically saves every weather check into a local CSV dataset (`history.csv`), building its own history over time.
* **Live Visuals:** Uses the `matplotlib` library to pop open easy-to-read graphs showing temperature and humidity trends.
* **Smart Averages:** Before making a new prediction, it actually reads all the past data to calculate the historical average.

## 📁 How My Code is Organized
I broke the project down into modular files to keep the code clean:
* `app.py` — The main script. Run this to start the program! It talks to the user and connects all the other files together.
* `model_logic.py` — The "brain" of the operation. It holds all the rules for predicting the weather (this perfectly replaces the need for a machine learning `.pkl` file).
* `analysis.py` — The graphing tool. It reads the dataset and draws the charts.
* `dataset/history.csv` — The specific folder and file where all the previous weather data is securely saved.

## 🚀 How It Works Behind the Scenes
When you run the program, it does a full cycle:
1. **Reads** the past data to find average trends.
2. **Asks** you for today's temperature and humidity.
3. **Predicts** the current weather condition using the rule-based logic.
4. **Stores** your new numbers to the bottom of the dataset.
5. **Draws** a graph showing the newly updated history.

## 💻 How to Run It Yourself
To try it out on your own machine, you just need Python and Matplotlib installed.

1. Install Matplotlib in your terminal:
   `pip install matplotlib`
2. Make sure all the files and the `dataset` folder are saved together.
3. Run the main app:
   `python app.py`

Thanks for checking out my project!
