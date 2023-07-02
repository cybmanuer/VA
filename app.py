import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import requests
import pyjokes
import json
import pywhatkit
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)
MASTER = "DANGER"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning Master")
    elif 12 <= hour < 18:
        speak("Good afternoon Master")
    else:
        speak("Good evening Master")
    speak('I am your Virtual Assistant. How can I help you today?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"YOU said: {query}\n")

        return query

    except sr.UnknownValueError:
        print('NO AUDIO HEARD......')
        return takeCommand()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    query = request.form['query']
    response = generate_response(query)
    return render_template('index.html', query=query, response=response)


def generate_response(query):
    if 'stop' in query.lower() or 'exit' in query.lower():
        speak("Ok, Master. I am leaving!")
        return "Assistant: Ok, Master. I am leaving!"

    if 'wikipedia' in query.lower() or 'search wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            return f"Wikipedia Summary: {results}"
        except wikipedia.exceptions.PageError:
            return "Sorry, I couldn't find any information on that topic."
        except wikipedia.exceptions.DisambiguationError:
            return "There are multiple results for that query. Please be more specific."

    elif 'open youtube' in query.lower():
        speak("Opening Youtube")
        url = "https://www.youtube.com"
        webbrowser.open(url)
        return "Assistant: Opening Youtube"

    # Add more cases for different commands and actions

    else:
        # Perform a default search on Google
        speak("Searching on Internet...")
        result = searchGoogle(query, num_sentences=4)
        if result:
            speak(result)
            return f"Search Result: {result}"
        else:
            return "No results found on Google."


def searchGoogle(query, num_sentences=10):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    search_result = soup.find("div", class_="BNeawe s3v9rd AP7Wnd").get_text()
    sentences = search_result.split(".")
    result = ". ".join(sentences[:num_sentences])
    return result


def VA():
    speak("STARTING...")
    wishMe()

    while True:
        query = takeCommand()
        response = generate_response(query)
        print("Assistant:", response)
        if 'stop' in query.lower() or 'exit' in query.lower():
            speak("Ok, Master. I am leaving!")
            break


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
    VA()
