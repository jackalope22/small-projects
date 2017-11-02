''' quiz_dictionary_style101.py
using a keyword:definitions_list dictionary for a flashcard-like quiz
tested with Python27 and Python33  by  vegaseat  08nov2013
'''
import random
# make string input work with Python2 or Python3
try: input = raw_input
except: pass
# a simple sample dictionary 'pick the right color'
# keyword:[def1, def2, def3, correct_def_ix]
# could use module pickle to dump/load this dictionary
mydict = {
#NOT
'Not False' : ['true', 'false', 0],
'Not True' : ['true', 'false', 1],
#OR
'True or False' : ['true', 'false', 0],
'True or True' : ['true', 'false',  0],
'False or True' : ['true', 'false', 0],
'False or False' : ['true', 'false', 1],
#AND
'True and False' : ['true', 'false', 1],
'True and True' : ['true', 'false', 0],
'False and True' : ['true', 'false', 1],
'False and False' : ['true', 'false', 1],
#NOT OR
'Not True or False' : ['true', 'false', 1],
'Not True or True' : ['true', 'false', 1],
'Not False or True' : ['true', 'false', 1],
'Not False or False' : ['true', 'false', 0],
#NOT AND
'Not True and False' : ['true', 'false', 0],
'Note True and True' : ['true', 'false', 1],
'Not False and True' : ['true', 'false', 0],
'Not False and False' : ['true', 'false', 0],
#!=
'1!=0' : ['true', 'false', 0],
'1!=1' : ['true', 'false', 1],
'0!=1' : ['true', 'false', 0],
'0!=0' : ['true', 'false', 1],
#==
'1==0' : ['true', 'false', 1],
'1==1' : ['true', 'false', 0], 
'0==1' : ['true', 'false', 1],
'0==0' : ['true', 'false', 0]
}
keyword_list = list(mydict.keys())
# shuffle the keywords in place
random.shuffle(keyword_list)
print('Would each statment be true or false:')
correct = 0
wrong = 0
for keyword in keyword_list:
    sf = '''\
{}
A) {}
B) {}
'''
    print(sf.format(keyword, mydict[keyword][0], mydict[keyword][1]))
    letter = input("Enter your choice with an (A B): ").upper()
    if letter == 'AB'[mydict[keyword][2]]:
        print('correct')
        correct += 1
    else:
        print('wrong')
        wrong += 1
    print('-'*30)
# final
sf = "Answers given --> {} correct and {} wrong"
print(sf.format(correct, wrong))