from tableExtend1 import  TextTableFormatter

class QuotedTextFormatter(TextTableFormatter):
    def row(self, rowdata):
        quoted =['"{}"'.format(d) for d in rowdata]
        super().row(quoted)

