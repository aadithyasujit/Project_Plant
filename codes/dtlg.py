def datalog(temp, hum, light, soil):
    worksheet = None

    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    print('Temperature: {0:0.2f} C'.format(temp))
    print('Humidity:    {0:0.2f} %'.format(hum))
    print('Humidity:    {0:0.2f} %'.format(light))
    print('Humidity:    {0:0.2f} %'.format(soil))
    date_str = json.dumps(datetime.datetime.now().strftime("%Y-%m-%d"))
    time_str = json.dumps(datetime.datetime.now().strftime("%H:%M:%S"))
    print(date_str)
    print(time_str)
    # Append the data in the spreadsheet, including a timestamp
#    try:
#    worksheet.append_row((datetime.datetime.now(), temp, humidity))
#    worksheet.append_row((temp, humidity))
    worksheet.append_row((date_str, time_str, temp, hum, light, soil))

    worksheet = None
    
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
