import abc
import datetime


class WriteFile:
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        with open(self.filename, 'a') as fh:
            fh.write(text + '\n')


class LogFile(WriteFile):
    def write(self, txt_line):
        date_str = datetime.datetime.now().strftime('%Y-%m.%d %H:%M')
        self.write_line('{0}    {1}'.format(date_str, txt_line))


class DelimFile(WriteFile):
    def __init__(self, filename, delimiter):
        super().__init__(filename)
        self.delimiter = delimiter

    def write(self, txt_list):
        line = self.delimiter.join(txt_list)
        self.write_line(line)
