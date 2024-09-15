from datetime import datetime
import csv
def main():

    users= [
        {'name': 'amir', 'birthday': 1990},
        {'name': 'ahmad', 'birthday': 2005},
        {'name': 'asghar', 'birthday': 2000},
        {'name': 'mamad', 'birthday': 1995},
        {'name': 'hossein','birthday': 2020}
    ]

    currentYear= datetime.now().year
    
    ages= list(map(lambda user: {'name': user['name'], 'age': currentYear - user['birthday']}, users))

    adultUsers= list(filter(lambda user: user['age']>=18, ages))

    with open('ages.csv', 'w', newline='')as csvfile:
        fieldNames=['name', 'age']

        writer= csv.DictWriter(csvfile, fieldnames = fieldNames)

        writer.writeheader()
        for user in ages:
            writer.writerow({'name': user['name'], 'age': user['age']})
    with open('adultUsers.csv', 'w', newline='')as file:
        write=csv.DictWriter(file, fieldnames=fieldNames)

        write.writeheader()
        for user in adultUsers:
            write.writerow({'name': user['name'], 'age': user['age']})

    with open('ages.csv','r', newline='')as file1:
        reader= csv.reader(file1)
        print('ages')
        for row in reader:
            print(row)
    
    with open('adultUsers.csv','r',newline='')as file2:
        read= csv.reader(file2)
        print('adultUsers')
        for row in read:
            print(row)

main()