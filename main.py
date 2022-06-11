from tkinter import *
from configparser import ConfigParser
import requests

# ++++++++++ VARIABLES ++++++++++
# https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key} - http request
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# ++++++++++ INIT ++++++++++
# -window
app = Tk()
app.title("Weather")
app.geometry('350x200')
app.configure(bg='#001429')
# -config
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


# ++++++++++ FUNCTIONS ++++++++++
def get_weather(city):
    result = requests.get(url.format(city, api_key))  # places variables into url {} and {}
    if result:
        json = result.json()
        print(json)
        city = json['name']
        country = json['sys']['country']
        temp_k = json['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = (temp_k - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        full = (city, country, temp_c, temp_f, icon, weather)
        return full
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        loc_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        # image['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]


# ++++++++++ TKINTER ITEMS +++++++++++
# -city entry
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
# -search button
search_btn = Button(app, text='Search weather', width=12, command=search)
# -data labels
loc_lbl = Label(app, text='', font=('bold', 20),  bg='#001429', fg='white')
temp_lbl = Label(app, text='', font=('bold', 20),  bg='#001429', fg='white')
weather_lbl = Label(app, text='', font=('bold', 20), bg='#001429', fg='white')
# -images
image = Label(app, bitmap='', bg='#001429', fg='white')


# ++++++++++ TKINTER ITEM PACKING ++++++++++
city_entry.pack()
search_btn.pack()
loc_lbl.pack()
temp_lbl.pack()
weather_lbl.pack()
image.pack()


# ++++++++++ MAIN CODE ++++++++++
# ++++ Run in Console ++++
#print(get_weather('Austin'))

# ++++ Run GUI ++++
app.mainloop()
