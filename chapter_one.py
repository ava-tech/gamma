def greeting(week_day):

    print(week_day.upper())
    if week_day.upper() not in ['SATURDAY', 'SUNDAY']:
        print("Working Day")
    else:
        print("Enjoy your Weekend !!!")
        if week_day.upper() == 'SATURDAY':
            print("Wake up late")
        if week_day.upper() == 'SUNDAY':
            print("Go for movies")

if __name__ == '__main__':
    greeting('sunday')
    greeting('Monday')
