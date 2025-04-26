from tabulate import tabulate
import schedual
import write_calendar

def main():
    s = schedual.get_information()
    cmp_function(s)


def show_function():
    print("\n")
    table = [{"index": 1, "function": "set regular rest number of weeks"},
             {"index": 2, "function": "set holidays"},
             {"index": 3, "function": "add work days"},
             {"index": 4, "function": "view work days"},
             {"index": 5, "function": "finish"}]
    print(tabulate(table, headers="keys", tablefmt="github"))
    print("\n")
    return 1

def check_option(option):
    try:
        option = int(option)
        if (option > 0 and option < 6):
            return option
        else:
            print("Invalid Option")
    except ValueError:
        print("Invalid Option")
        raise ValueError



def cmp_function(s):
    while True:
        show_function()
        option = check_option(input("what do you want to do?"))
        match option:
            case 1:
                s.set_regular_free()
                print(s.dates_in_month)
            case 2:
                s.get_free_day()
            case 3:
                s.get_work_day()
            case 4:
                print(s.dates_in_month)
                print("\n")
            case 5:
                print("setting finish")
                print_schedual(s)
                return 2



def print_schedual(s):
    write_calendar.write_schedual(s.dates_in_month, s.work_hour)
    return 3


if __name__ == "__main__":
    main()
