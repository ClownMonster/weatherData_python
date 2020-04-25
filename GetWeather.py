import requests

''' 
This import  is to get my api key, u have to get your own api key from https://www.openweathermap.org/
'''

from apikey import api_key # comment this line to add your api key

# api_key = 'your api key'   

#  uncomment the above  line and add your key



# prints the weather report
def dataPrint():
    global data_in_json
    print('co-ordinates : ')
    print('\tLatitute : ',data_in_json['coord']['lat'])
    print('\tLongitude : ',data_in_json['coord']['lon'])
    print('')
    print('wather : ',data_in_json['weather'])
    print('')
    print('Temperature Details: ')
    print('\tCurrent Temperature : ',data_in_json['main']['temp'])
    print('\tMinimun Temperature : ',data_in_json['main']['temp_min'])
    print('\tMaximum Temperature : ',data_in_json['main']['temp_max'])
    print('')
    print('Pressure : ',data_in_json['main']['pressure'])
    print('Humidity : ',data_in_json['main']['humidity'])
    print(f"Wind speed : {data_in_json['wind']['speed']} and degree : {data_in_json['wind']['deg']}")
    print('Sunrise : ',data_in_json['sys']['sunrise'])
    print('Sunset : ',data_in_json['sys']['sunset'])
    print('Timezone : ',data_in_json['timezone'])
    return



city = input('Enter the city Name: ')

try:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        #print(response.text) # gets the data in  text format, u can change it to json format with response.json()
        data_in_json = response.json()
        #print(data_in_json)
        dataPrint()

    else:
        raise Exception('Server Not found check your api key or city name')


except Exception as e:
    print(e)


