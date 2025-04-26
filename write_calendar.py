
import csv
from tabulate import tabulate


def write_schedual(dates, w_hour):
    dates.insert(0,"time")
    with open("time_worker_file.csv", mode='w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames = dates)
        writer.writeheader()
        #print the work hour as colume
        for i in range(len(w_hour)):
            hour = w_hour[i]
            writer.writerow({dates[0]:hour})

#read the file and print it as table
def read_schedual():
    new = []
    with open("time_worker_file.csv", mode="r") as schedual_file:
        reader = csv.reader(schedual_file)
        for row in reader:
            new.append(row)

    table = tabulate(new[1:], headers = new[0],  tablefmt="mixed_grid")
    with open('table.txt', 'w') as f:
        f.write(table)
        return table



def main():
    write_schedual()
    read_schedual()



if __name__ == "__main__":
    main()

