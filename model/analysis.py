import csv
import matplotlib.pyplot as plt

def show_graphs(file_path):
    days, temps, hums = [], [], []
    
    try:
        with open(file_path, "r") as f:
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