class Date(object):
    def __init__(self, year , month , day ):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, s): # essentially we are defining new ways to construct objs
        parts = s.split("-")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @classmethod
    def today(cls):
        import  time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)



class Mydate(Date):
    def yeo(self):
        print("Hello Yeo!!")

# function is detached from the class. It is related to the class
# this is known problem, We might  need diff ways to create object


def date_from_string(s):
    parts = s.split("-")
    return Date(int(parts[0]), int(parts[1]), int(parts[2]))
