import csv

import argparse

import time



def read_file(filename):

    with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:

        csv_reader = csv.reader(csv_file)

        for row_number, row in enumerate(csv_reader, start=1):

            yield row_number, row #returning row number and the whole row contents

            

def printout(error_cells,color_counts):

    if error_cells:

        for row_num, col_num in error_cells:

            print(f"Found a broken cell in row {row_num} col {col_num}")

    for color, count in color_counts.items():

        if color!="this is a broken cell":

            print(f"Found: {count} {color} cells")    

    print(f"Found: {len(error_cells)} broken cells")       

    

start_time = time.time()#to measure execution time



parser = argparse.ArgumentParser()

parser.add_argument("filename")#path to the CSV file

parser.add_argument("-error",required=True, default=None)#error condition to check for

args = parser.parse_args()

    

color_counts = {} 

error_cells = []



print("Reading CSV file\n")



cells = ((row_number, col_number, cell)

         for row_number, row in read_file(args.filename)

         for col_number, cell in enumerate(row, start=1)) 



for row_num, col_num, cell in cells:

    if args.error and args.error in cell: #if there is an error arg and if error arg specified is in cell (found a broken cell)

        error_cells.append((row_num, col_num))

    color = cell.lower() if cell else "empty" #to ensure that if user changed in csv content (for example entering colors in opper case)

    color_counts[color] = color_counts.get(color, 0) + 1 #incrementing color count 



print("Done reading CSV file\n")



#printing out the results

printout(error_cells,color_counts)



end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time:.4f} seconds")

