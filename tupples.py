"""A class to handle the tupple structure"""


class Tupple:
    def __init__(self, columns = []):

        """columns : the data stored in each csv column
           header : the offset and length of the data in each column
           header size : part of the header
           data pointer : helping variable to make the header"""

        self.columns = columns
        self.header = ""
        self.header_size = 0
        self.data_pointer = 0


    def set_options(self):

        """method for setting the header_size, data_pointer, header"""

        self.header_size = 6*len(self.columns) # every header cell is 6 bytes
        self.data_pointer = self.header_size + 1 # after the header cells there is a null byte
        for column in self.columns : # make the header
            self.header += str(self.data_pointer) + "," + str(len(column.encode("ascii")))
            if len(str(len(column.encode("ascii")))) == 2 :
                self.header += " "
            else :
                self.header += "  "
            self.data_pointer += len(column.encode("ascii"))
