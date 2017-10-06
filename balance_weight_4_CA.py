##
# Bailey Stillman
# 10/5/17
# Examine Ballanced 3 neighbor CAs that map to 5 neighbors
##
import CA

'''
balanced_three_n_CA

finds all of the three neighbor CAs that have a balanced rule table

RETURNS The integer value for the rule table

'''

def balanced_three_n_CA ():
    rule_nums = []
    num_CA = 256
    for i in range(0,256):
        rule_table = CA.dec_to_bin(i)
        if sum(rule_table) == len(rule_table)/2:
            rule_nums.append(i)
    return rule_nums
    
'''
get_ca_weight_4 

finds all of the three neighbor CAs that have a rule table with weight 4

RETURNS: the rules that have a rule table weight of 4

'''
def get_ca_weight_4 ():
    rule_nums = [] 
    num_CA = 256
    for i in range(0,256):
        rule_table = CA.dec_to_bin(i)
        if sum(rule_table) <= len(rule_table)/2-1:
            rule_nums.append(i)
    return  rule_nums;
print(get_ca_weight_4())


'''
full_3_ca_set

composes the lists for CAs of rule table weight 4 or less and those with a 
balanced rule table into a list.

RETURNS: the list of 4 or less and balanced rule tables

'''

def full_3_ca_set ():
    all_nums = balanced_three_n_CA() + get_ca_weight_4()
    all_nums.sort()
    for i in range(len(all_nums)):
        if all_nums[i] == all_nums[i-1]:
            all_nums[i].remove(i)
    return all_nums
    
    
    