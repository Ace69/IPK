# -*- coding: utf-8 -*-
import socket
import json
import sys

# ***************************** Check argument count *********************************
arg_count = len(sys.argv)
if not (arg_count == 3):
    sys.exit("ERROR: Invalid arguments count \nCorrect arguments must be in shape 'api_key=<API key> city=<city name>'\n")

# ***************************** Check first argument *********************************
arg_key = sys.argv[1]
arg_key = arg_key.split("=")[0]+"="
if not (arg_key == "api_key="):
    sys.exit("ERROR: An error occured during parsing input \nBefore your key must be 'api_key='\n")

# ****************************** Check second argument ******************************
arg_city = sys.argv[2]
arg_city = arg_city.split("=")[0]+"="
if not (arg_city == "city="):
    sys.exit("ERROR: An error occured during parsing input \nBefore city name must be 'city='\n")

# **************Function that removes everything before certain character*****************
def afterStr(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1:
        return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value):
        return ""
    return value[adjusted_pos_a:]
# ***************************Socket creating *****************************************
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ****************Define all the substrings of request string*************************
server = "api.openweathermap.org"
port = 80
key = afterStr(sys.argv[1], "=")
url = "/data/2.5/weather"
city_name = afterStr(sys.argv[2], "=")
units = "metric"
param = url + "?q=" +city_name + "&units=" + units + "&appid=" + key

# *****************************Finally connected string request ***********************
request = "GET " + param + " HTTP/1.1\r\n" + "Host: " + server + "\r\n" + "Connection: close\r\n\r\n"
# ******************************Connect to the server ******************************
try:
    server_ip  = socket.gethostbyname(server)
except:
    sys.exit("Server is not available \nCheck your internet connection or 'api.openweathermap.org'\n")

s.connect((server_ip, port))
s.send(request.encode())
result = s.recv(4096)

# **************************** Check error code that came from server ****************
code_check = result.split("\n")[0]
code_error = code_check

code_check = code_check.find("200")
if (code_check == -1):
    sys.exit(" ERROR: %s \nCorrect them and try again\n" % code_error)


#******************** Cutting the string, so there be only JSON part************************
gg = afterStr(result,"\n")
gg = json.loads(gg)

#******************** Getting certain information from JSON ***************************
name = gg['name']
weather = gg['weather'][0]['description']
temp = gg['main']['temp']
humidity = gg['main']['humidity']
pres = gg['main']['pressure']
winds = gg['wind']['speed']
try:
    windd = gg ['wind']['deg']
except:
    windd = "n/a"

while (len(result) > 0):
        print(name)
        print(weather)
        print('temp: {} °C' .format(temp))
        print('humidity: {} %' .format(humidity))
        print('pressure: {} hPa' .format(pres))
        print('wind-speed: {} hm/h'.format(winds))
        print('wind-deg: {}' .format(windd))
        result = s.recv(4096);
