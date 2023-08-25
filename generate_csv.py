# this code is to generate colors randomly in the specified csv file
import csv

import random



# List of available colors

colors = ["red", "blue", "green", "yellow","black","white","this is a broken cell"]



def generate_random_color():

    return random.choice(colors)



def generate_csv_with_colors(filename, num_rows, num_columns):

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:

        csv_writer = csv.writer(csv_file)

        for _ in range(num_rows):

            row = [generate_random_color() for _ in range(num_columns)]

            csv_writer.writerow(row)

filename = "input.csv"

num_rows = 1000  

num_columns = 5 



generate_csv_with_colors(filename, num_rows, num_columns)

print(f"CSV file '{filename}' generated with {num_rows} rows and {num_columns} columns.")
