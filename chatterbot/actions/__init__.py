def get_date():
    from datetime import date
    return date.today().strftime("%d-%m-%y")


def get_day():
    from datetime import date
    return date.today().strftime("%A")

def get_location():
    return "Bangalore"


def get_time():
    import time
    return time.strftime("%H:%M:%S")


def get_temperature():
    return "24C"
