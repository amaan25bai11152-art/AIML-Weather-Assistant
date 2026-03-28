import csv
import model_logic     
import analysis       

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

def save_data(day, t, h, cond):
    with open(history_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([day, t, h, cond])
    print("Data saved.")


# --- Main Application Starts Here ---
print("Weather Checker")

avg_t, avg_h = get_past_data()
print(f"Avg Temp: {avg_t:.1f} C, Avg Humidity: {avg_h:.1f}%")

current_t, current_h = get_user_input()

result = model_logic.guess_weather(current_t, current_h)
print("Result:", result)

try:
    with open(history_file, "r") as f:
        day_number = sum(1 for _ in f)
except:
    day_number = 1

save_data(day_number, current_t, current_h, result)

analysis.show_graphs(history_file)