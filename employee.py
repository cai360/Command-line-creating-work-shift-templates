import schedual

s = schedual.Schedual()

class Employee:
    def __init__(self, name, ID):
        self.workhour = 0
        self.money = 0
        self.name = name
        self.ID = ID

    def __str__(self):
        return f"name:{self.name}, ID:{self.ID}"

    #getter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        #add something to make sure they pass a name
        self._name = name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def workhour(self):
        return self._workhour

    @workhour.setter
    def workhour(self, hour):
        ...

    @property
    def paid(self):
        return self._money

    @paid.setter
    def paid(self, hour):
        # self._money = hour * hour_paid
        ...

    def get_empty_schedual(self):
        print(s.show_schedual())

    def choose_shift(self):
        ...

def main():
    employee = get_employee()
    print(employee)
    employee.get_empty_schedual()

def get_employee():
    name = input("name: ")
    ID = input("ID: ")
    return Employee(name, ID)


if __name__ == "__main__":
    main()
