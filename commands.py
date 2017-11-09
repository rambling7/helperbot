import requests
import config

def d_help():
  return 'ща помогу'
  
def d_advice():
  return 'вот мой совет: гы'
  
def d_weather():
  res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'id': '703448', 'units': 'metric', 'lang': 'ru', 'APPID': config.WEATHER_API_KEY})
  data = res.json()
  weather = str(data['weather'][0]['description'])
  temp = str(data['main']['temp'])
  res_str = 'сегодня {w}, средняя температура {t}'.format(w=weather, t=temp)

  return res_str

comm_arr = {
'помоги':   d_help,
'совет':    d_advice,
'погода':   d_weather
}
