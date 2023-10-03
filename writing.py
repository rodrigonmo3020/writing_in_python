""" This is how you write CSV files on Python """

import os
import csv

output_path = os.path.join('.','new.csv')

with open(output_path, 'w') as my_file:
    my_writer = csv.writer(my_file) # NOTE... Maybe we should add the delimeter

    my_writer.writerow(['id','Name','SSN'])
    my_writer.writerow(['1','Jose','1234'])
    my_writer.writerow(['2','Ana','5678'])
    my_writer.writerow(['3','Andres','9012'])

