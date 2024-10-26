import schedule
import smtplib
import requests
from bs4 import BeautifulSoup

def umbrellaReminder():
    city = "Ernakulam, Kerala"

    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.findd('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs={'class' : 'BNeawe tAd8D AP7Wnd'}).text

    sky = time_sky.split('/n')[1]

    if sky == "Rainy" or sky == "Rain And Snow" or sky == "showers" or sky == "Haze" or sky ==  "Cloudy":
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

        smtp_object.starttls()

        smtp_object.login("email id", "password")
        subject = "Umberlla Reminder"
        body = f"Take an umberlla, it may rain. Weather condition for today is {sky} and temparature is {temperature} in {city}."
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode( 
            'utf-8') 
        
        smtp_object.sendmail("FROM EMAIL", "TO EMAIL", msg)

        smtp_object.quit()
        print("Email Sent!")

schedule.every().day.at("06:00").do(umbrellaReminder)

while True:
    schedule.run_pending()
