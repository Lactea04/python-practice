from time import sleep
with (open("kyong_gi_gwank_zu_weather_data.csv", "r") as f): #city_name, yyyy-mm-dd tt:tt,degree
    data = f.readlines() #city_name,yyyy-mm-dd tt:tt,degree(float)\n

    #elements
    Year = (2023, 2024)
    Months = list(range(1,13))
    Day = list(range(0,32))

    # flag
    def flag():
        flag_ = input("\nIf you want to quit the program,"
                      "\nplease input 'c', the others will continue the program:")
        return flag_

    # error_logs
    def error_wrong_date():
        print("\nThis data is not belong to the weather database."
              "\nPlease write other date in the correct form.")

    #work_program
    while True:
        #prompt
        print("\nWhat is the date you want to check the degree in Kyong-Gi-Do-Gwang-Zu?"
              "\nThe range is from 2023-08-30 00:00 to 2024-08-29 23:00.")
        sleep(1.5)
        choose_date = input("\nPlease write in the form yyyy-mm-dd tt:tt:")
        if choose_date[0:4] not in str(Year):
            error_wrong_date()
            sleep(1.5)
        elif int(choose_date[5:7]) > 13:
            error_wrong_date()
            sleep(1.5)
        elif int(choose_date[6:7]) < 10:
            if int(choose_date[6:7]) not in Months[:10]:
                error_wrong_date()
                sleep(1.5)
        elif choose_date[9:11] not in str(Day):
            error_wrong_date()
            sleep(1.5)
        elif choose_date[6:8] in ('02', '04', '06', '09', '11'):
            if choose_date[9:11] >= '31':
                error_wrong_date()
                sleep(1.5)



        #data_search_process
        for datum in data:
            if len(choose_date) == 16:
                if choose_date in datum:
                    datum = datum.split(',')
                    print(f"\nThe degree in Kyong-Gi-Do-Gwang-Zu at {choose_date} is {datum[2]}°C")
                else:
                    continue
            else:
                print("\nIt is wrong form, please write in correct form")
                sleep(1)
                break
            flag()
            if flag == 'c' or 'C':
                break

