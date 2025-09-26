import requests

def get_weather(city):
    API_KEY = "1aca608aea5dc2a158b81d4ffcabc1b1"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return f"Weather info not found for '{city}'."
    else:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        return f"Weather in {city.title()}: {temp}°C | {condition}"

def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    return f'"{quote}" — {author}'

def get_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    data = response.json()
    return data["slip"]["advice"]

def main():
    print("\n🌞 Welcome to Daily Motivation App 🌞\n")  # 👈 Pehle ek line ka gap
    city = input("Enter your city name: ")
    print("\nFetching data... Please wait...\n")

    weather = get_weather(city)
    print("🌤️", weather)

    quote = get_quote()
    print("💬 Quote of the Day:", quote)

    advice = get_advice()
    print("💡 Advice:", advice)

    print("\n✨ Thank you for using Daily Motivation App! ✨\n")  # 👈 Aakhir me ek line ka gap

if __name__ == "__main__":
    main()
