import functions as fn

# MAIN CODE FILE


file_sz = 15000 # writing file size
tupples_lst = []  # tupple buffer
data = "data.csv" # data file name
to_write = ["ordered", "heap_file"] 

fn.readnstore(data,tupples_lst) # read the data, put it in the <tupples_lst>

tupples_num = len(tupples_lst) # how many tupples in the list

fn.write_unsorted(tupples_lst,to_write[1],file_sz,tupples_num) # write to the file in initial order

""" Sort the tupples_lst """

col = []

for tupple in tupples_lst :
    col.append(tupple.columns[0])

col.sort()
sorted_tupples = []

for line in col :
    for tupple in tupples_lst :
        if line == tupple.columns[0]:
            sorted_tupples.append(tupple)
            break

""" End sorting the tupples list"""

fn.write_unsorted(sorted_tupples,to_write[0],file_sz,tupples_num) # write to a file ordered by the first column

col.clear()              # empty the col
sorted_tupples.clear()   # -||-
tupples_lst.clear()      # -||-
print("\n|\n|\n|First exercise \n|\n|\n\n")
print ("\n___________________________________________________________\n")
print("\nPrinting from the ordered file :\n")
print ("\n___________________________________________________________\n\n")
fn.first_ex(col, to_write[0]) # first exercise for the ordered file
print ("\n___________________________________________________________\n")
print ("\nPrinting from the heap file :\n")
print ("\n___________________________________________________________\n\n")
fn.first_ex(col, to_write[1]) # for the unordered file

print("\n|\n|\n|Second exercise \n|\n|\n\n")
print ("\n___________________________________________________________\n")
print("\nPrinting from the ordered file :\n")
print ("\n___________________________________________________________\n\n")
fn.secnd_ex(col, to_write[0]) # second ex for the ordered file
print ("\n___________________________________________________________\n")
print ("\nPrinting from the heap file :\n")
print ("\n___________________________________________________________\n\n")
fn.secnd_ex(col, to_write[1]) # on the heap file

print("\n|\n|\n|Third exercise \n|\n|\n\n")
print ("\n___________________________________________________________\n")
print("\nPrinting from the ordered file :\n")
print ("\n___________________________________________________________\n\n")
fn.third_ex(col, to_write[0]) # third on the ordered
print ("\n___________________________________________________________\n")
print ("\nPrinting from the heap file :\n")
print ("\n___________________________________________________________\n\n")
fn.third_ex(col, to_write[1]) # on on the heap

print("\n|\n|\n|Fourth exercise\n|\n|\n\n")
fn.fourth_ex(col, to_write[0], to_write[1]) # fourt exercise for both files
