

import csv

list = []
csv_reader = csv.reader(open("songs.csv"))
for row in csv_reader:
    list.append(row)


for index, element in enumerate(list):
    if element[3] == "y":
       element[3] = "*"
    else:
       element[3] = ""


def main():
    print("Welcome to songs to learn--ZhuKunBo")
    menu = show_menu()
    print("Please choose a option")
    choice = input("Enter a option:").upper()
    while choice != "Q":
        if choice == "L":
            for i, item in enumerate(list):
                print("{:2}".format(i), "{:2}{:<30s}{:<20s}{:>20s}".format
                (item[3], item[0], item[1], item[2]))
            menu = show_menu()
            choice = input("Enter a option:").upper()
        elif choice == "A":
            choice = add_song()
            menu = show_menu()
            choice = input("Enter a option:").upper()

def show_menu():
    print("Menu:")
    print("L","-","List songs")
    print("A","-", "Add new song")
    print("C","-","Complete a song")
    print("Q","-","Quit")

def add_song():
    adds = []
    title = input("Enter the song's title,input can not be blank:")
    adds.append(title)
    writer = input("Enter the song's writer,input can not be blank:")
    adds.append(writer)
    year = input("Enter the year,number must >= 0:")
    adds.append(year)
    require = "*"
    adds.append(require)
    list.append(adds)



main()