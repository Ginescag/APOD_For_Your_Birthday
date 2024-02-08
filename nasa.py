<<<<<<< HEAD
import requests
import json
from PIL import Image
import webbrowser

def get_raw(api_key):
    raw_response = requests.get(api_key)
    return raw_response

def get_data(api_key):
    raw_response = requests.get(api_key).text
    response = json.loads(raw_response)
    return response

def get_date(response):
    date = response['date']
    return date


def get_explaination(response):
    explaination = response['explanation']
    return explaination


def get_hdurl(response):
    hdurl = response['hdurl']
    return hdurl

def main():
    val = input("Enter your birthday date (YYYY-MM-DD format): ")
    val = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + val
    rawR = get_raw(val)
    if rawR.status_code == 200:
        R = get_data(val)
        url =get_hdurl(R)
        webbrowser.open(url)
        print(get_explaination(R) + " HAPPY BIRTHDAY!\n")
    else:
        print("YOU ARE TOO OLD!!\n")

    input("\nPRESS ANY KEY TO EXIT: ")

=======
import requests
import json
from PIL import Image
import webbrowser

def get_raw(api_key):
    raw_response = requests.get(api_key)
    return raw_response

def get_data(api_key):
    raw_response = requests.get(api_key).text
    response = json.loads(raw_response)
    return response

def get_date(response):
    date = response['date']
    return date


def get_explaination(response):
    explaination = response['explanation']
    return explaination


def get_hdurl(response):
    hdurl = response['hdurl']
    return hdurl

def main():
    val = input("Enter your birthday date (YYYY-MM-DD format): ")
    val = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + val
    rawR = get_raw(val)
    if rawR.status_code == 200:
        R = get_data(val)
        url =get_hdurl(R)
        webbrowser.open(url)
        print(get_explaination(R) + " HAPPY BIRTHDAY!\n")
    else:
        print("YOU ARE TOO OLD!!\n")

    input("\nPRESS ANY KEY TO EXIT: ")

>>>>>>> 792e4374ac2b3d85a3b6836b170bdfae2fbc2869
main()