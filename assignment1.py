"""
The program is for loading,adding and completing songs
Name:ZhuKunBo
Date:December 7th,2018
Link to my project on GitHub:https://github.com/jc490479/CP1404-SP532018-STARTER-A1

Function load_songs():
import csv
csv_reader=csv.reader(open("songs.csv"))
for row in csv_reader
list.append(row)
for index,element in enumerate(list)
if element[3] is y, then
elemnet[3] = "*"
Otherwise
element[3] = " "
Display " L - list songs
          A - add new song
          C - complete a song
          Q - quit"
get a choice from user
if choice is L, then
for i, item in enumerate(list):
Display""{:2}".format(i), "{:2}{:<30s}{:<20s}{:>20s}".format
                    (item[3], item[0], item[1], int(item[2]))"

Function complete_song():
while True:
  try:
     complete = int(input("Enter the number of a song to mark as learned:"))
  except ValueError:
     Display "invalid input,enter a valid number"
  else:
      break
while complete < 0:
    Display"number must >= 0"
    omplete = int(input("Enter the number of a song to mark as learned:"))

if list[complete][3] == " ", then
    Display""you have already learned {}".format(list[complete][0])"
else:
    list[complete][3] = " "
    Display""{} by {} learned".format(list[complete][0], list[complete][1]))"

"""


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
                print("{:2}".format(i), "{:2}{:<30s}{:<20s}{:>20d}".format
                    (item[3], item[0], item[1], int(item[2])))
            menu = show_menu()
            choice = input("Enter a option:").upper()
        elif choice == "A":
            choice = add_song()
            menu = show_menu()
            choice = input("Enter a option:").upper()
        elif choice == "C":
            choice = complete_song()
            menu = show_menu()
            choice = input("Enter a option:").upper()
        else:
            print("Invalid choice,please input a valid choice")
            menu = show_menu()
            choice = input("Enter a option:").upper()

    if choice == "Q":
        print("songs save to songs.csv,have a nice day:")


def show_menu():
    """Print a menu"""
    print("Menu:")
    print("L","-","List songs")
    print("A","-", "Add new song")
    print("C","-","Complete a song")
    print("Q","-","Quit")

def add_song():
    """Add the song(title,writer,year) in the menu"""
    adds = []
    title = input("Enter the song's title,input can not be blank:")

    while title == "":
        title = input("Input can not be blank,please input title a valid format:")
    adds.append(title)
    writer = input("Enter the song's writer：")
    while writer =="":
     writer = input("Input can not be blank,please input writer a valid format:")
    adds.append(writer)
    while True:
        try:
            year = int(input("enter the year:"))
        except ValueError:
            print("Invalid input,enter a valid number")
        else:
            break

    while year <= 0:
        print("number must >= 0")
        year = input("Enter the year")
    adds.append(year)
    require = "*"
    adds.append(require)
    list.append(adds)

def complete_song():
    """Complete the song's learning"""
    while True:
        try:
            complete = int(input("Enter the number of a song to mark as learned:"))
        except ValueError:
            print("Invalid input,enter a valid number")
        else:
            break
    while complete < 0:
        print("number must >= 0")
        complete = int(input("Enter the number of a song to mark as learned:"))

    if list[complete][3] == " ":
        print("you have already learned {}".format(list[complete][0]))
    else:
        list[complete][3] = " "
        print("{} by {} learned".format(list[complete][0], list[complete][1]))

main()