class Employee:
    def __init__(self, first, last, salary):
        self.infor = dict()
        self.infor['first'] = first
        self.infor['last'] = last
        self.infor['salary'] = salary + 5000

    def give_raise(self):
        self.infor['salary'] += 450
        return self.infor

    def show_infor(self):
        return self.infor
