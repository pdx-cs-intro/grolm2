#!/usr/bin/python3
# Grocery List Manager (version 2)
# Bart Massey 2021

import csv, sys
from os import path

# Keep a grocery list file in CSV format.
# Command-line commands:
#     * grolm2 add <count> <item>
#     * grolm2 clear
#     * grolm2 remove <item>
#     * grolm2 list

class Item:
    def __init__(self, count, item):
        self.count = count
        self.item = item

    def get_item(self):
        return self.item
    
    def display(self):
        print(f"{self.count}× {self.item}")
    
    def csv_row(self):
        return [self.count, self.item]

listfile = "groceries.csv"

class GroceryList:
    def __init__(self):
        self.groceries = []
        if path.isfile(listfile):
            f = open(listfile, "r")
            c = csv.reader(f)
            groceries = []
            for count, item in c:
                groceries.append(Item(count, item))
            self.groceries = groceries
            f.close()
    
    def add(self, count, item):
        self.groceries.append(Item(count, item))
    
    def display(self):
        for item in self.groceries:
            item.display()
    
    def clear(self):
        self.groceries = []
    
    def add(self, count, item):
        self.groceries.append(Item(count, item))

    def save(self):
        f = open(listfile, "w")
        c = csv.writer(f)
        for item in self.groceries:
            c.writerow(item.csv_row())
        f.close()

def usage():
    print("grolm2: usage: grolm2 <command>", file=sys.stderr)
    exit(1)

if len(sys.argv) < 2:
    usage()

grocery_list = GroceryList()

def check_arg_length(n):
    if len(sys.argv) < n + 2:
        usage()

cmd = sys.argv[1]
if cmd == "add":
    check_arg_length(2)
    try:
        count = int(sys.argv[2])
    except:
        usage()
    item = ' '.join(sys.argv[3:])
    grocery_list.add(count, item)
elif cmd == "list":
    check_arg_length(0)
    grocery_list.display()
elif cmd == "clear":
    check_arg_length(0)
    grocery_list.clear()

grocery_list.save()
