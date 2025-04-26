from calendar import Calendar
from calendar import TextCalendar
from datetime import date





class Schedual:
    def __init__(self, year=2024, month=1, start=8, end=16):
        self.year = year
        self.month = month
        self.week_numbers = self.date_on_calendar(year, month)
        self.dates_in_month = self.dates_for_calendar()

        self.start = start
        self.end = end
        self.free_day = []
        self.work_hour = self.hour_interval(start, end)

        #[{key=hour: value=worker}]
        self.hour_worker = self.hours_and_workers()

        #[{dates:{hours: workers}}]
        self.shift =  self.date_hour_worker()
    @classmethod
    def get_year(cls):
        try:
            while True:
                year = int(input("input year: "))
                if (year > 0):
                    return year
                else:
                    print("Invalid year")
                    pass
        except ValueError:
            raise ValueError



    @classmethod
    def get_month(cls):
        try:
            while True:
                month = int(input("input month: "))
                if (month < 13 and month > 0):
                    return month
                else:
                    print("Invalid month")
                    pass
        except ValueError:
            print("Invalid month")
            pass

    @classmethod
    def get_start(self):
        while True:
            try:
                start = int(input("input start time: "))
                if (start < 24 and start >= 0):
                    return start
                else:
                    print("Invalid start time")
                    pass
            except ValueError:
                print("Invalid start time")
                pass

    @classmethod
    def get_end(self, start):
        while True:
            try:
                end = int(input("input end time: "))
                if (end > start and end < 25):
                    return end
                else:
                    print("Invalid end time")
                    pass
            except ValueError:
                print("Invalid end time")
                pass



    #return a list of tuple of (dates and week numbers)
    def date_on_calendar(self, year, month):
        calendar = Calendar()
        calendar_with_0 = calendar.monthdays2calendar(year, month)

        #delete day 0
        calendar_with_week_numbers = []
        for i in range(len(calendar_with_0)):
            for j in range(7):
                if calendar_with_0[i][j][0] != (0):
                        calendar_with_week_numbers.append(calendar_with_0[i][j])
        self.week_numbers = calendar_with_week_numbers
        return self.week_numbers

    #return a list of dates in month
    def dates_for_calendar(self):
        #a list of dates
        key_date = []
        for i in range(len(self.week_numbers)):
           key_date.append(self.week_numbers[i][0])
        self.dates_in_month = key_date
        return self.dates_in_month

    # return a list of hours interval
    def hour_interval(cls, start, end):
        working_hr = end - start
        w_hour = []
        for i in range(working_hr):
            w_hour.append(f"{start + i:02} - {start + i + 1:02}")
        colume = w_hour
        return colume

     #a list of {key=hour: value=worker}
    def hours_and_workers(self):
        hour_and_worker = []
        for i in range(len(self.work_hour)):
            hours_string = f"{self.start + i:02} - {self.start + i + 1:02}"
            hour_and_worker.append({hours_string: ""})
        self.hour_worker = hour_and_worker
        return self.hour_worker

    # a list of [{dates:{hours: workers}}]
    def date_hour_worker(self):
        shift = []
        for i in range(len(self.dates_in_month)):
            shift.append({self.dates_in_month[i]:self.hour_worker})
        self.shift = shift
        return shift

    def get_free_day(self):
        print("input days to set free day, after finish input type 0")
        while True:
            try:
                freeday = int(input("free day: "))
                if(freeday == 0):
                    break
                date(self.year, self.month, freeday)
                self.delete_day_from_calendar(freeday)
            except ValueError:
                print("Invaliad date")
                pass

    def set_regular_free(self):
        print("which week day you wanna rest? finish input 0")
        flag = True
        free = []
        while (flag):
            try:
                freeday = int(input("week? "))
                if (freeday < 8):
                    if(freeday == 0):
                        flag = False
                    if (freeday not in free):
                        for i in range(len(self.week_numbers)):
                            if(self.week_numbers[i][1] == freeday-1):
                                free.append(freeday)
                                self.delete_day_from_calendar(self.week_numbers[i][0])
                    else:
                        print("week already be set")
                else:
                    print("Invalid number")
            except ValueError:
                print("Invalid week number")
                pass



    #deleted the day from calendar because of free day
    def delete_day_from_calendar(self, freeday):
        if freeday not in self.free_day:
            self.free_day.append(freeday)
            try:
                #self.week_numbers.remove(freeday)
                self.dates_in_month.remove(freeday)
            except ValueError:
                pass
        else:
            print("free day already be set")

    def get_work_day(self):
        print("input days to set work day, after finish input type 0")
        while True:
            try:
                workday = int(input("work day: "))
                if(workday == 0):
                    break
                date(self.year, self.month, workday)
                self.add_day_from_calendar(workday)
            except ValueError:
                print("Invaliad date")
                pass


    #undo setting free day
    def add_day_from_calendar(self, workday):
        if workday not in self.dates_in_month:
            self.dates_in_month.append(workday)
            self.dates_in_month = sorted(self.dates_in_month)
        else:
            print("work day already be set")

    # def show_schedual(self):
    #     return write_calendar.read_schedual()


def main():
    schedual = get_information()
    print(schedual.week_numbers)
    schedual.set_regular_free()




def show_month(year, month):
    print("\n")
    tc = TextCalendar()
    tc.prmonth(year, month, w=0, l=0)
    print("\n")



def get_information():
        year = Schedual.get_year()
        month = Schedual.get_month()
        show_month(year, month)
        start = Schedual.get_start()
        end = Schedual.get_end(start)
        return Schedual(year, month, start, end)


if __name__ == "__main__":
    main()
