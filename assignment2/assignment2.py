import csv
import traceback
import os
import custom_module
from datetime import datetime

#Task 2
def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r", newline = '') as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        
        data["rows"] = rows
        
        return data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}')

        print(f'Exception type: {type(e).__name__}')

        if str(e):
            print(f'Exception message: {str(e)}')

        print(f'Stack trace: {stack_trace}')

employees = read_employees()
print(employees)

#Task 3
def column_index(name):
    return employees["fields"].index(name)

employee_id_column = column_index("employee_id")

#Task 4
def first_name(row_num):
    return employees["rows"][row_num][column_index("first_name")]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))

    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

    return matches

#Task 7
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])

    return employees["rows"]

print(sort_by_last_name())

#Task 8
def employee_dict(row):
    keys = employees["fields"][1:]
    values = row[1:]

    return dict(zip(keys, values))

print(employee_dict(employees["rows"][1]))

#Task 9
def all_employees_dict():
    result = {}

    employee_id_column = 0
    
    for row in employees["rows"]:
        id = row[employee_id_column]
        result[id] = employee_dict(row)
    
    return result

print(all_employees_dict())

#Task 10
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("ooga booga")
print(custom_module.secret)

#Task 12
def read_csv_to_dict(path):
    data = {}
    rows = []

    with open(path, "r") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            if i == 0:
                data["fields"] = row
            else:
                rows.append(tuple(row))

    data["rows"] = rows

    return data

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1 | set2

minutes_set = create_minutes_set()
print(minutes_set)

#Task 14
def create_minutes_list():
    min_set_list = list(minutes_set)

    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), min_set_list))

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    minutes_list.sort(key = lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    with open("minutes.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list

print(write_sorted_list())