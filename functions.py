from csv import DictReader
from tupples import Tupple

"""Functions file"""

def readnstore(data,lst):

    """
    Function that reads the raw data from the csv file and stores
    it in a list of <object : Tupple>
    """

    with open(data, "r") as raw_data :
        csv_reader = DictReader(raw_data)
        for row in csv_reader :
            #each item in the list is a tupple
            lst.append(Tupple([row["col1"],row["col2"],row["col3"],row["col4"]]))
            lst[-1].set_options()



def write_unsorted(lst,filename,file_size,tupples_num):

    """
    Function to write the data structured in the file
    fl_header_ptr: where to write the file header
    tpl_header_ptr: where to write the tupple header, end of free space
    tpl_length: size of the tupple data in bytes
    """

    fl_header_ptr = 0
    tpl_header_ptr = file_size
    with open(filename, "wb") as file:
        file.write(bytearray(file_size)) #allocate the memory for the file by writing *file_size* 0 bytes
        file.seek(fl_header_ptr)
        file.write(str(tupples_num).encode("ascii")) # first part of the header, number of tupples to write
        fl_header_ptr += 12 # leaving 6 bytes to put the end of free space
        for item in lst :
            file.seek(fl_header_ptr)
            tpl_length = item.data_pointer
            file.write(str(tpl_header_ptr-tpl_length).encode("ascii")) # writing the pointer to the tupple
            fl_header_ptr += 6 #increasing the value of the pointer for the next pointer to the tupple
            tpl_header_ptr -= tpl_length # updating the writing point for the next tupple
            file.seek(tpl_header_ptr) # go to the end of the last writen tupple pointer
            file.write(item.header.encode("ascii"))
            file.seek(1,1) # skip one byte
            for column in item.columns :
                file.write(column.encode("ascii"))
            file.seek(6)
            file.write(str(tpl_header_ptr-1).encode("ascii")) # update the end of free space pointer
            file.write(bytearray(6-len(str(tpl_header_ptr))))


def first_ex(lst, file) :

    """
    Function to get all the tupples with more than two words in the second
    column
    point : pointer to file header
    key : pointer to tupple header
    col_ptr : pointer to the data
    col_len : data size in bytes
    col_data : initial data
    """

    point = 12
    with open(file, "rb") as rd :
        for i in range(int(rd.read(3))) :
            rd.seek(point)
            key = int(rd.read(6).decode("ascii").replace('\x00','')) # initialize the key
            rd.seek(key + 6) # go to the second column pointer
            col2_ptr = key + int(rd.read(2).decode("ascii"))
            col2_len = int(rd.read(3).decode("ascii")[1:])
            rd.seek(col2_ptr) # go to the data
            col2_data = rd.read(col2_len).decode("ascii")
            if len(col2_data.split()) > 2 : # do the maths
                lst.append(get_tupple(key,rd)) # get the tupple
            point += 6 # go to the next tupple pointer
    for tupple in lst : # print out the results
        print(tupple)
    print("\n" + "Total tupples : " + str(len(lst)) + "\n")
    lst.clear()

# the next three exercises will be ligthly commented due to the simmilarity with the last function

def secnd_ex(lst,file):

    """
    Function to get all the tupples with two negative numbers in the second
    column.
    point : file point to write the pointer to the tupple
    key : pointer to the tupple
    col_data : initial data of the column
    """

    point = 12
    with open(file,"rb") as rd :
        for i in range(int(rd.read(3))) :
            rd.seek(point)
            key = int(rd.read(6).decode("ascii").replace('\x00',''))
            col3_data = get_tupple(key,rd).split(" |||| ")[2]
            if col3_data.count("-") == 2 :
                lst.append(get_tupple(key,rd))
            point += 6
    for tupple in lst :
        print (tupple)
    print("\n" + "Total tupples : " + str(len(lst)) + "\n")
    lst.clear()


def third_ex(lst,file) :

    """
    Function to get all the tupples containing <<P.O Box>> in the third
    column
    """

    point = 12
    with open(file,"rb") as rd :
        for i in range(int(rd.read(3))) :
            rd.seek(point)
            key = int(rd.read(6).decode("ascii").replace('\x00',''))
            col3_data = get_tupple(key,rd).split(" |||| ")[3]
            if "P.O. Box" in col3_data :
                lst.append(get_tupple(key,rd))
            point += 6
    for tupple in lst :
        print (tupple)
    print("\n" + "Total tupples : " + str(len(lst)) + "\n")
    lst.clear()


def fourth_ex(lst,ordered, unordered) :

    """
    Function to get all the tupples in the increasing order,
    ordered by first column
    """
    print ("\n___________________________________________________________\n")
    print("\nPrinting from the ordered file :\n")
    print ("\n___________________________________________________________\n\n")
    point = 12
    with open(ordered, "rb") as rd :
        for i in range(int(rd.read(3))) :
            rd.seek(point)
            key = int(rd.read(6).decode("ascii").replace('\x00',''))
            print(get_tupple(key,rd))
            point +=6

    point = 12
    print ("\n___________________________________________________________\n")
    print ("\nPrinting from the heap file :\n")
    print ("\n___________________________________________________________\n\n")
    with open(unordered, "rb") as rd :
        for i in range(int(rd.read(3))) :
            rd.seek(point)
            key = int(rd.read(6).decode("ascii").replace('\x00',''))
            lst.append(get_tupple(key,rd).split(" |||| ")) # get all the tupples
            point += 6
        ls = sorted(lst, key = lambda x : x[0]) # sort the tupples in increasing order by the first column
    for i in ls :
        temp = ""
        for l in i :
            temp += l + " |||| "

        print(temp.rstrip(" |||| "))
    ls.clear()
    lst.clear()


def get_tupple(key,rd) :
    """
    Function to get the data from a tupple :
    key : point of the tupple start in the file
    rd : file
    """
    rd.seek(key) # go to the tupple
    col1_ptr = key + int(rd.read(2).decode("ascii")) # get the first pointer
    col1_len = int(rd.read(3).decode("ascii")[1:]) # get the data lenth
    rd.seek(col1_ptr) # go to the data
    col1_data = rd.read(col1_len).decode("ascii") # get the data
    rd.seek(key + 6) # same thing for all the columns
    col2_ptr = key + int(rd.read(2).decode("ascii"))
    col2_len = int(rd.read(3).decode("ascii")[1:])
    rd.seek(col2_ptr)
    col2_data = rd.read(col2_len).decode("ascii")
    rd.seek(key + 12)
    col3_ptr = key + int(rd.read(2).decode("ascii"))
    col3_len = int(rd.read(3).decode("ascii")[1:])
    rd.seek(col3_ptr)
    col3_data = rd.read(col3_len).decode("ascii")
    rd.seek(key + 18)
    col4_ptr = key + int(rd.read(2).decode("ascii"))
    col4_len = int(rd.read(3).decode("ascii")[1:])
    rd.seek(col4_ptr)
    col4_data = rd.read(col4_len).decode("ascii")
    return col1_data + " |||| " + col2_data + " |||| " + col3_data + " |||| " + col4_data # return the tupple data as a string,
                                                                                          # columns divided by " |||| "
