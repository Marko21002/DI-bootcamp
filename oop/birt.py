from datetime import datetime


def birthd(year, month, day):
    birthdate = datetime(year, month, day)
    now = datetime.now()
    age = now.year - birthdate.year - \
        ((now.month, now.day) < (birthdate.month, birthdate.day))
    print("Вы прожили {} лет".format(age))
    delta = now - birthdate
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Вы прожили {} дней, {} часов, {} минут и {} секунд".format(
        days, hours, minutes, seconds))


birthd(2002, 7, 21)
