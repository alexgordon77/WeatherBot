TOKEN='1788367235:AAHVYV8bL9RLC_jA_NixsVifhbQn7g_tywI'

URL='https://api.telegram.org/bot{token}/{method}'

UPDATE_METH='getUpdates'
SEND_METH='sendMessage'

MY_ID=584154638

UPDATE_ID_FILE_PATH='update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data=file.readline()
    if data:
        data=int(data)
    UPDATE_ID=data

WEATHER_TOKEN='f9a2a7462c700a778bd824c805e648f6'
WEATHER_URL='http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

