import csv

import argparse

import time



def open_file(filename):

    csv_file=open(filename, mode="r")

    csv_reader=csv_file.read()

    csv_reader.replace("\n",",")

    arr=csv_reader.split(",")

    return arr

    

def read_file(arr):

    max_cols=3

    col=0

    row=0

    for cell in arr:

        yield cell,row,col

        col+=1	

        if(col==max_cols):

            col=0

            row+=1

    yield None, 0, 0

        

def printout(error_cells,color_counts):

    for (row, col) in error_cells:

        print(f"Found a broken cell in Row: {row}, Column: {col}")

    print(f"Found: {color_counts.get('red')} red cells")    

    print(f"Found: {color_counts.get('blue')} blue cells")  

    print(f"Found: {color_counts.get('green')} green cells")    

    print(f"Found: {color_counts.get('yellow')} yellow cells")  

    print(f"Found: {color_counts.get('black')} black cells")    

    print(f"Found: {color_counts.get('white')} white cells")   

    print(f"Found: {len(error_cells)} broken cells") 

    

    

start_time = time.time()#to measure execution time

parser = argparse.ArgumentParser()

parser.add_argument("filename")#path to the CSV file

parser.add_argument("-error",required=True, default=None)#error condition to check for

args = parser.parse_args()

color_counts = {} 

error_cells = []



print("Reading CSV file")

arr = open_file(args.filename)



gen = read_file(arr)



while True:

    cell,row,col=next(gen)

    if cell is None: break

    

        error_cells.append((row, col))

        continue

        

    color = cell.lower() 

    color_counts[color] = color_counts.get(color, 0) + 1 #incrementing color count

    

#printing out the results

printout(error_cells,color_counts)

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time:.4f} seconds")

