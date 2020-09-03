import pyowm
owm = pyowm.OWM("143a7943ca22b3c0b2ed1be93ad6ab23")
observation = owm.weather_at_place('Ankara,TR')
w = observation.get_weather()
w.get_wind()
w.get_humidity()
