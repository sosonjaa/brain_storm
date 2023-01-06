file_data = open(r"chartIn.txt")
file_data_list = []


def remove(text):
    return text.replace(" ", "")




for line in file_data.read().splitlines():
    #new_lines = file_data_list.append(line)


    #no_spaces = list(remove(line))
    #file_data_list.append(no_spaces)


print(file_data_list)


# Python3 program to extract first and last
# element of each sublist in a list of lists
#

def extract_first(file_data_list):
    return [item[0] for item in file_data_list]


#print(extract_first(file_data_list))



# print(file_data_list[1][2]) # prints the second index of the first item in the list


file_data.close()