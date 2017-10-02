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
def dec_to_bin(num, nbits=8):
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
   
   
def hamming_distance (rule_1,rule_2):
    if len(rule_1) == len(rule_2):
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

def write_to_file (primary, hamming, secondary, file_name):
        out = csv.writer(open(file_name,"a+"), delimiter=',')
        for i in range(len(primary)):
            row = []
            row.append(primary[i])
            row.append(hamming[i])
            row.append(secondary[i])
            out.writerow(row)
# tests write_to_file

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
    hamming_distance_list = []
    file = "hamming_distance_6.csv" # change this to alter the file name 
    # above are all of the variables needing to be populated
    #parameters are specified below
    NUM_CAs = 256
    RULE_TABLE_LENGTH = 8
    i= 1
    while i in range(NUM_CAs+1):
        ca_rules.append(i)
        i +=1
    #the above for loop populates the list CA_rules from (0-256)
    for j in range(len(ca_rules)):
        temp = dec_to_bin(ca_rules[j])
        ca_rule_tables.append(temp)
    #the above for loop populates the CA_rule_tables list 
    for k in range(len(ca_rules)):
        for l in range(len(ca_rules)):
            temp_1 = hamming_distance( ca_rule_tables[k], ca_rule_tables[l])
            if temp_1 >= 6:
                hamming_distance_list.append(temp_1)
                primary_list.append(ca_rule_tables[k])
                secondary_list.append(ca_rule_tables[l])
    write_to_file(primary_list, secondary_list, hamming_distance_list,file)

            
                
        
            

main()