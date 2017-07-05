def print_tables(objects, colnames, formatter):
    #emits some table header
    formatter.headings(colnames)

    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


class TableFormatter(object):
    # design specs
    def headings(self, headers):
        raise NotImplementedError
    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()
    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):

        print(",".join(headers))
    def row(self, rowdata):

        print(",".join(rowdata))


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