# Use words.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
print("fh ", fh)
book = fh.read()
print("book ", book)
bookCAPITAL = book.upper()
bookCAPITALrstrip = bookCAPITAL.rstrip()
print(bookCAPITALrstrip)