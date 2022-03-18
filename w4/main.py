import random
# What self development I should be working today
user = input("Hello Beautiful! How do you feel today? \n")
feelings = ['Happy', 'Sad', 'Angry', 'Over life', 'Joyful', 'Depressed', 'Moody']
weather = ['Rainy', 'Sunny', 'Cloudy', 'Storm', 'Snowing']
self_development = ['Read a book', 'treat yourself to coffee', 'Meditate', 'Watch a movie', 'Workout for 30mnin']
loving_words = ['You are amazing', 'Keep up the work', 'You rock', 'Be kind to yourself', 'Love yourself', 'Embrace change', 'Trust the process']
treat_yourself = ['Starbucks', 'Dutch Bros', 'Teazers', 'Kuppa Joy']
home_activ = ['Play board game', 'plan your future', 'Watch a show', 'reach for the sky']
for day_feeling in feelings:
    if day_feeling == "Happy":
        happy_feels = random.choice(loving_words)
        print(f"The day is going to be great! " f"{happy_feels}")
    elif day_feeling == "Sad":
        sadfeels = random.choice(treat_yourself)
        print(f"You deserve a little treat to cheer you up! " f"{sadfeels}")
    elif day_feeling == "Angry":
        vibes = random.choice(loving_words)
        print(f"Take a deep breath it will be fine. Don't spend more than five minutes mad. " f"{vibes}!")
self = input("What is the forcast for today?\n")
for forcast in weather:
    if forcast == "Storm":
        day = random.choice(home_activ)
        print(f"Here are some options for your day; " f"{day}")
    elif forcast == "Sunny":
        sunshine = random.choice(self_development)
        print(f"Have an awesome day " f"{sunshine}")
