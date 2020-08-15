# This function will create a dictionary that displays which classes the students(numbers) share with each other

def OrgShedulesOptimized(arr):
    share_dict = {}
    for element in arr:
        for other_element in arr:
            if element[0] < other_element[0]:
                share_dict["{} & {}".format(element[0], other_element[0])] = []
    for element in arr:
        for other_element in arr:
            if element[0] < other_element[0] and element[1] == other_element[1]:
                share_dict["{} & {}".format(element[0], other_element[0])].append(element[1])
    for students in share_dict:
        print(students)
        print(share_dict[students])
    return(share_dict)

students = [
    ["1", "Economics"],
    ["2", "Philosophy"],
    ["3", "Physics"],
    ["1", "Physics"],
    ["4", "Social Studies"],
    ["2", "Economics"],
    ["3", "Philosophy"],
    ["4", "Philosophy"],
    ["1", "Philosophy"],
    ["2", "Linguistics"],
    ["4", "Linguistics"],
    ["5", "Art"]
]

OrgShedulesOptimized(students)