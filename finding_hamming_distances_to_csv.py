## 
# Bailey Stillman
# Andrew Penland
# 8/31/17 
# This code will compile a list of all 3 neighbor Cellular Automata rules and their 
# Hamming sistance in relation to eachother.
# Python 3
##

## Imports
import math 
import random
import csv
import copy
## 


'''
dec_to_bin
This method converts a numerical input into a binary string of lenth nbits.

INPUTS: num, nbits

num, is the number you wish to convert to binary
nbits, is the length of the binary string you want outputted

RETURNS: bin

bin, The resulting binary number.

'''
def dec_to_bin(num, nbits):
   new_num = num
   bin = []
   for j in range(nbits):
      #create the appropriate power of 2 for the current step
      current_bin_mark = 2**(nbits-1-j)
      #check to see if you can subtract this power of 2; if so, then subtract it and append 1
      if (new_num >= current_bin_mark):
         bin.append(1)
         new_num = new_num - current_bin_mark
     #if you can't subtract, append 0
      else:
         bin.append(0)
   return bin
   

'''
hamming_distance
This method solves for the Hamming distance between two CA rule tables.

INPUTS: rule_1, rule_2

rule_1/rule_2, are the CA rule tables that you want to find the hamming distance of

RETURNS: hamming_num 

hamming_num, is the hamming distance between the two rules that were inputted. 


'''
   
   
def hamming_distance (rule_1,rule_2) :
    if len(rule_1) == len(rule_2) :
        # makes sure that the rule tables are of an equal length
        hamming_num = 0
        for i in range(len(rule_1)) :
            if rule_1[i] != rule_2[i] :
                hamming_num = hamming_num +1
                # counts the number of points where each the rules differ (hamming distance)
    return hamming_num
    #returns hamming distance
    
    
    
'''
write_to_file
This method records the information of each CA in a csv file.

INPUTS: primary_rule, hamming_distance , secondary_rule

primatry_rule_list, is the CA rule tables being examined.
hamming_distance_list, is the recorded hamming_distances between primary_rule_list and secondary_rule_list.
secondary_rule_list, are the rules that primary_rule_list is being compared to.


RETURNS: N/A
'''

def write_to_file (primary_rule_list, hamming_distance_list, secondary_rule_list):
    for i in range(len(primary_rule_list)):
        data = [primary_rule_list[i], hamming_distance_list[i], secondary_rule_list[i], "\n"]
        # The next two lines were found on stack exchance: https://stackoverflow.com/questions/2084069/create-a-csv-file-with-values-from-a-python-list
        # and have been modified to work with this code. (This is due to my limited knowledge of working with .csv files in python 3)
        out = csv.writer(open("hamming_distance_3_neighbor_83117.csv","w"), delimiter=',')
        out.writerow(data)
        #currently write to file is overwriting the first line of the .csv file. I am not sure how to specify that it goes to a new line.
# tests write_to_file
write_to_file([1,2,3],[1,2,3],[1,2,3])

'''
main
the main method will provide the rule numbers to each of the methods and ultimately initialize the code.

INPUTS:

RETURNS:

'''
def main ():
    # it is important that all of these lists be added too in order of CA.
    ca_rules = []
    ca_rule_tables = []
    primary_list = []
    secondary_list = [] 
    haming_distance_list = []
    # above are all of the variables needing to be populated
    #parameters are specified below
    NUM_CAs = 256
    RULE_TABLE_LENGTH = 8
    
    
    for i in len(range(NUM_CAs+1)):
        ca_rules.append(i)
    #the above for loop populates the list CA_rules form (0-256)
    
    for j in range(len(ca_rules)):
        temp = dec_to_bin(ca_rules(j), RULE_TABLE_LENGTH)
        ca_rule_tables.append(temp)
    #the above for loop populates the CA_rule_tables list 
    
    for k in range(len(CA_rules)):
        for l in range(len(CA_rules)):
            temp_1 = hamming_distance( ca_rule_tables[k], ca_rule_tables[l]
            primary_list.append(ca_rules[k])
            secondary_list.append(ca_rules[l])
            haming_distance_list.append(temp_1)
            
    write_to_file(primary_list,haming_distance_list,secondary_list)
            

