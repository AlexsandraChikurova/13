from tkinter import *
import requests

# Функция для получения погоды
def get_weather():
    city = cityField.get()
    key = 'b33421202e1f749c5c39adf9abd3c8ab'  # Замените 'ВАШ КЛЮЧ' на ваш API ключ от OpenWeatherMap
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}°C'

# Настройки главного окна
root = Tk()
root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('300x250')
root.resizable(width=False, height=False)

# Создание фреймов
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создание текстового поля для ввода города
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

# Создание кнопки для получения погоды
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

# Создание текстовой надписи для отображения погоды
info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

# Запуск основного цикла
root.mainloop()
