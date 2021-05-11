import pyowm
import numpy as np
from scipy import stats

def fridge_temp():
    '''
    Función que retorna una distribución normal entre 8 y 12, con media 10 y desviación estándar 2, correspondiente a la temperatura de la nevera.
    '''
    return stats.truncnorm.rvs((8-10)/2,(12-10)/2,loc=10,scale=2,size=None)

def fridge_ice():
    '''
    Función que retorna una distribución uniforme entre 0 y 10, correspondiente a la capacidad de generar hielo de la nevera.
    '''
    return np.random.uniform(low=0, high=10, size=None)

def pot_temp():
    '''
    Función que retorna una distribución uniforme entre 0 y 150, correspondiente a la temperatura de la olla en grados centígrados.
    '''
    return np.random.uniform(low=0, high=150, size=None)

def living_room_capacity():
    '''
    Función que retorna una distribución uniforme entre 0 y 10, correspondiente a la cantidad de personas reunidas en la sala.
    '''
    return round(np.random.uniform(low=0, high=10, size=None))

def ccs_temp():
    '''
    Función que retorna la temperatura actual de Caracas. Usa la librería "pyowm" para consumir datos de la API "OpenWeatherMap".
    '''
    owm = pyowm.OWM('0c449c2320a101aad901918bef6138c0')
    ccs = owm.weather_manager().weather_at_place('Caracas, VE')
    weather = ccs.weather
    return weather.temperature('celsius')['temp']

def tank_empty(water=100):
    '''
    Función que retorna la cantidad de agua restante en el tanque, después de restarle el valor resultante de una distribución normal entre 0 y 100, con media 10% y desviación estándar 5% de su capacidad total.
    '''
    norm = stats.truncnorm.rvs((0-10)/5,(100-10)/5,loc=10,scale=5,size=None) # loc=10 por ser 10 el 10% de 100, scale=5 por ser 5 el 5% de 100
    if norm > water:
        return 0
    return (water-norm)

def tank_fill(water=100):
    '''
    Función que retorna la cantidad de agua actual en el tanque, después de sumarle el valor resultante una distribución normal entre 0 y 100, con media 20% y desviación estándar 5% de su capacidad total.
    '''
    norm = stats.truncnorm.rvs((0-10)/5,(100-10)/5,loc=10,scale=5,size=None) # loc=20 por ser 20 el 20% de 100, scale=5 por ser 5 el 5% de 100
    if norm + water > 100:
        return 100
    return (water+norm)
