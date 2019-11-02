
"""
# list


def overlap_lists(list_a, list_b):
    for item in list_b:
        if item not in list_a:
            list_a.append(item)
    return list_a  # remember the return


animals = ["pig", "panda"]
sports = ["redsox", "philly", "panda"]

# copy_list = animals.copy()

overlaping_list = overlap_lists(animals, sports)
print(overlaping_list)


# dictionary

phi = {}

phi = {
    "city" : "P",
    "sport": "baseball",
    "food": "cheese",
    "lucky_num" : 1
}

yankees = {
    "city" : "N",
    "sport": "baseball",
    "food": "apple",
    "lucky_num" : 0
}
# print(phi)

phi["lucky_num"] = 76


for key in yankees:
    value = yankees[key]
    print(f"{key} has the value of {value}")
    


teams = [phi, yankees]
for team in teams:
    for key in team:
        value = team[key]
        print(f"{key} has the value of {value}")
    print("---------------")
"""

state_rows = []
with open("state.sizes.csv") as states_file:
    for row in state_file.readlines():
        row_text = row.strip()
        state_rows.append(row_text)
