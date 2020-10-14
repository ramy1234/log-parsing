

import re #this model to use the reguler expresion
from collections import Counter #this module used to count the ips
import csv


#the comming fun will open the file, search for the ips and return a list of the founded ips
def file_reader(filename):
    with open(filename) as file: #with used to handle the exciptions, to make the code cleaner and much more readable
        log=file.read()
        regex_string = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        list_of_ips = re.findall(regex_string, log)
        return list_of_ips


#the comming fun will return a dictionary of the existing ips and its counts
def ips_counter(list_of_ips):
    number_of_every_ip= Counter(list_of_ips)
    return number_of_every_ip


#the comming fun will take a dictionary of the existing ips and its counts the creat csv file and redirect the output to it, csv file opend by excel
def output_file(number_of_every_ip):
    with open('logs_result.csv', 'w') as output:
        writer= csv.writer(output)
        header=['ip', 'count']
        writer.writerow(header)
        for i in number_of_every_ip:
            writer.writerow((i, number_of_every_ip[i]))


        

if __name__ == "__main__":
    output_file(ips_counter(file_reader('fil.log')))
