def greeting(week_day):
    if week_day.upper not in ['SATURDAY', 'SUNDAY']:
        print("Working Day")
    else:
        print("Enjoy your Weekend !!!")


if __name__ == '__main__':
    greeting('Monday')
