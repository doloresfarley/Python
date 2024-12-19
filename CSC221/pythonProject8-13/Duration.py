class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        minute_string = str(self.minutes)
        if self.minutes < 10:
            minute_string = f'0{minute_string}'
        return f'{self.hours} hrs {minute_string} mins'

my_time = Duration(6, 45)
print(my_time)