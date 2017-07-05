#what if the Parent class initialized some value. How to deal with it for child classes

import  sys
def print_tables(objects, colnames, formatter):
    #emits some table header
    formatter.headings(colnames)

    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


class TableFormatter(object):
    # design specs
    def __init__(self, outfile=None):
        if outfile == None:
            self.outfile = sys.stdout
        self.outfile = outfile
    def headings(self, headers):
        raise NotImplementedError
    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def __init__(self,outfile=None, width=10):
        super().__init__(outfile)
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print()
    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(item,self.width), end=' ', file=self.outfile)
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):

        print(",".join(headers), file=self.outfile)
    def row(self, rowdata):

        print(",".join(rowdata), file=self.outfile)


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end = ' ')
        print('</tr>')
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}</td>'.format(d), end = ' ')
        print('</tr>')