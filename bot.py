import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot

# 🔴 PUT YOUR DETAILS HERE
BOT_TOKEN = "8923507494:AAGGjj5LjFV6NqIfBjRl67daB6oxypJZ0Do"
CHAT_ID = "8393320937"

URL = "https://corporate.ethiopianairlines.com/AboutEthiopian/careers/results"

bot = Bot(token=BOT_TOKEN)

last_seen = ""

def check_website():
    global last_seen

    try:
        response = requests.get(URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True).lower()

        # 🎯 Only look for Trainee Pilot
        if "trainee pilot" in text:

            if text != last_seen:
                last_seen = text

                bot.send_message(
                    chat_id=CHAT_ID,
                    text="🚨 TRAINEE PILOT UPDATE FOUND!\n\nCheck here:\n" + URL
                )

                print("Notification sent!")

    except Exception as e:
        print("Error:", e)


print("Bot is running...")

while True:
    check_website()
    time.sleep(300)  # checks every 5 minutes