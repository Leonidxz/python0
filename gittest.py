class Calendar():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def date(self):
        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if self.year > 2025:
            print("False")
        else:
            if self.month <= 0 or self.month > 12:
                print("False")
            else:
                if self.day in range(1, months[self.month] + 1):
                    print("True")
                elif self.month == 2 and ((self.year % 4 == 0) and not (self.year % 100 == 0)) or (
                        self.year % 400 == 0):
                    if self.day in range(1, months[self.month] + 2):
                        print("True")
                    else:
                        print("False")
                else:
                    print("False")


class Clock(Calendar):
    def __init__(self, time, day, month, year):
        self.time = time
        self.day = day
        self.month = month
        self.year = year

    def time_hm(self):
        h = self.time // 60 % 24
        m = self.time % 60
        print(h, m)

# time = int(input("t"))
# day = int(input("d"))
# month = int(input("m"))
# year = int(input("y"))
#
# Rolex = Clock(time, day, month, year)
# Rolex.time_hm()
# Rolex.date()

# Дано число n. С начала суток прошло n минут. Определите,
# сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа:
# количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.

class Car():
    def sound():
        print('beep')

    def long_sound():
        print('beep-beep')


Car.sound()
Car.long_sound()

# Напишите класс Car, который при вызове метода sound печатает слово "beep",
# а при вызове метода long_sound печатает “beep-beep”.

# todo lala

