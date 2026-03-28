import csv
import matplotlib.pyplot as plt

history_file = r"C:\Users\Asadc\Desktop\history.csv"

def get_past_data():
    temp_sum = 0
    hum_sum = 0
    total_days = 0

    try:
        with open(history_file, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                temp_sum += float(row[1])
                hum_sum += float(row[2])
                total_days += 1

        if total_days == 0:
            return 0, 0
        
        return temp_sum / total_days, hum_sum / total_days

    except:
        print("File not found. Starting fresh.")
        return 0, 0

def get_user_input():
    while True:
        try:
            t = float(input("Temp (C): "))
            h = float(input("Humidity (%): "))

            if -50 <= t <= 60 and 0 <= h <= 100:
                return t, h
            else:
                print("Please enter realistic values.")
        except:
            print("Please enter numbers only.")

def guess_weather(t, h):
    print("\nPredicting...")
    
    if t <= 0:
        if h > 60:
            return "Snow"
        else:
            return "Cold"
    elif h >= 80:
        return "Rain"
    elif t > 30 and h < 50:
        return "Sunny"
    elif t > 20:
        return "Cloudy"
    else:
        return "Normal weather"

def save_data(day, t, h, cond):
    with open(history_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([day, t, h, cond])
    print("Data saved.")

def show_graphs():
    days = []
    temps = []
    hums = []
    
    try:
        with open(history_file, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                days.append(int(row[0]))
                temps.append(float(row[1]))
                hums.append(float(row[2]))
    except:
        print("No data to plot yet.")
        return

    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(days, temps, marker="o", color="red")
    plt.title("Temp over time")
    plt.xlabel("Day")
    plt.ylabel("Temp (C)")
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.plot(days, hums, marker="s", color="blue")
    plt.title("Humidity over time")
    plt.xlabel("Day")
    plt.ylabel("Humidity (%)")
    plt.grid()

    plt.tight_layout()
    plt.show()

print("Weather Checker")

avg_t, avg_h = get_past_data()
print(f"Avg Temp: {avg_t:.1f} C, Avg Humidity: {avg_h:.1f}%")

current_t, current_h = get_user_input()

result = guess_weather(current_t, current_h)
print("Result:", result)

try:
    with open(history_file, "r") as f:
        day_number = sum(1 for _ in f)
except:
    day_number = 1

save_data(day_number, current_t, current_h, result)
show_graphs()