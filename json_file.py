import json

emps = []

def read_data():
    global emps
    global data
    data = json.load(open('data.json', ))
    emps = data['emp_details']


def find_avg_age():
    avg_age = sum([i["age"] for i in emps]) / len(emps)
    return avg_age

def find_average_age_for_dept(dept):
    emps1 = []
    for i in emps:
        if i['department'] == dept:
            emps1.append(i)
    # print(emps1)
    avg_age = sum([s["age"] for s in emps1]) / len(emps1)
    return avg_age


def main():

    read_data();
    print("Average emp age is", find_avg_age())
    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))

if __name__ == "__main__":
    main()




















