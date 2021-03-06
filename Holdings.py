class Holding(object):
    def __init__(self,name,date,shares,price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self,nshares):
         self.shares = self.shares - nshares


    def __repr__(self):
        return "Portfolio({!r}, {!r}, {!r}, {!r})".format(self.name,self.date,self.shares,self.price)

import  csv
def read_portfolio(filename):
    portfolio = []
    with open(filename,'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append(Holding(row[0],row[1],int(row[2]), float(row[3])))
    return portfolio