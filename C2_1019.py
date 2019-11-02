
# 20191019


# adding machine
add = 0
for i in range (101):
    add += i
print(f"sum is: {add}")


# open file
long_state = 0
with open("state_names.txt") as state_names_file:  # file object

    for row in state_names_file.readlines():
        # print(row)  # to solve the empty row problem in the output, use the following code
        state_name = row.strip()
        # print(state_name)
        # longest names in state
        if len(state_name) > long_state:
            long_state = len(state_name)
            long_state_name = state_name
    print(long_state_name)  # North and south carolina has the same length

# strip - removing space...
name = "Bob Space             "
print(len(name))
cleaned_name = name.strip()
print(cleaned_name)
print(len(cleaned_name))


# patch strings
output_string = "Hi my name is " + name
print(output_string)


size = 5
name = "Alice"
state_file = open("state_names.txt")


# strings

big = "elephant"
animals = ["lion", "tiger", big]
# print(f"length is {len(animals)}")
# print(animals[2])
# print(animals[-1])
animals.append("pigs")
animals.append("pigs")
# print(animals[-1])

for animal in animals:  # animal is newly created and could only be used in this loop
    print(animal)


for this_file in file:
    name_list = []
    with open(this_file) as single_file_process:
        for row in single_file_process.readlines():
            name_list.append(row.strip())
    print(name_list)


# writing list from file
file = ["state_names.txt"]


def find_longest_name(name_list):
    record = 0
    for name in name_list.readlines():
       temp = len(name)
       if temp > record:
            longest_row = name
            record = temp
    print(longest_row)
    print(record)


for this_file in file:
    with open(this_file) as file_to_process:
        find_longest_name(file_to_process)


def merge_lists(list_a, list_b):
    # pass meaning do nothing the moment, but don't want python to fail
    merge_list = []
    for item in list_a:
        if item in list_b:
            merge_list.append(item)
    return merge_list  # remember the return


animals = ["pig", "panda"]
sports = ["redsox", "philly", "panda"]

merged_list = merge_lists(animals, sports)
print(merged_list)

