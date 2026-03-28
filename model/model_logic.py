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