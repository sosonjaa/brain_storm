#from pathlib import Path

#p = Path(__file__).with_name('file.txt')
#with p.open('r') as f:
#    print(f.read())

file_data_list = []

def open_file(filename):
    file_data = open(filename)
    for line in file_data.read().splitlines():  # splits the data into lines
        file_data_list.append(line.split())     # splits the lines into items

open_file(r"chartIn.txt")
print(file_data_list)

def extract_each(number):   # if the question comes up: is there a window seat available?
    return [item[number] for item in file_data_list]    # returns the value of each row for the given index (aisle)


window_seats = extract_each(1) + extract_each(6)  # [row A + row F]
middle_seats = extract_each(2) + extract_each(5)  # [row B + row E]
aisle_seats = extract_each(3) + extract_each(4)  # [row C + row D]


def reserved_seats_window():
    if "X" in window_seats:
        index_window = window_seats.index("X")
        return print(index_window)
    else:
        print("All seats are still available.\n")


file_data.close()


# soll alle Dateien einlesen können (chartIn 1-4)
# mit dictionaries?
