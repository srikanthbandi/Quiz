#PROJECT : Taking two text documents with random names and converting it into python dictionaries to conduct a quiz.

import os
import fnmatch
import random



# function to get all the .txt files in the directory.

def all_txt_files():
    path = os.getcwd() # to get the current working directory.
    folder = os.listdir( path )
    txtfiles = []
    for file in folder:
             if fnmatch.fnmatch(file,'*.txt'):
                 txtfiles.append(file)
             
    return txtfiles

# function to convert .txt into a dictionary.

def txt2dictionary(filename):
    sri = open(filename,"r")
    english2spanish ={}
    for line in sri:
        keyword,value = line.split(':')
        english2spanish[keyword.strip()] = value.strip()
    sri.close()
    #print english2spanish
    return english2spanish


# function to convert dictionary into .txt file.

def dictionary2txt(filename,dictionary):
    space= ""
    for keyword,value in dictionary.items():
        space+=keyword+":"+value+"\n"
    open(filename,"w").write(space)

if all_txt_files() != []:
    print "These are the files present in the directory"
    for i in range(len(all_txt_files())):
        txtfiles=all_txt_files()
        print str(i+1)+")"+txtfiles[i]
        


#user selection code.

selected_file = input("please select a file by typing the number next to it: ")

try:
    
    if (int(selected_file) <= len(all_txt_files())):
        selected_file = int(selected_file)
        
    else:
        selected_file = input("TRY AGAIN:NOT A VALID SELECTION:please select a file by typing the number next to it: ")

except ValueError:
        print("Sorry you have not entered a number:")
        sys.exit
        
    
       
   
txtfiles=all_txt_files()
quiz_dictionary = txt2dictionary(txtfiles[selected_file-1])

print "number of english words in the selected dictionary are  = "+ str(len(quiz_dictionary))

numberofwords_selected = int(input("please enter the number of words you want to take quiz on? "))
if numberofwords_selected >len(quiz_dictionary):
            print("you have entered a number greater than the limit,TRY AGAIN")
            numberofwords_selected = int(input("please enter the number of words you want to take quiz on? "))
        

question_dictionary = [] # an temporary dictionary is taken to conduct the quiz.
    
for key, value in quiz_dictionary.items():
        s = [key,value]
        question_dictionary.append(s)
    
questions = random.sample(question_dictionary,numberofwords_selected)
wrongones = {}

for i in range(numberofwords_selected): # code to conduct quiz
        print("What is '" + str(question_dictionary[i][0])+ "' in Spanish? ")
        ans = raw_input(str("enter answer:"))
        print ans
        if  ans == question_dictionary[i][1]:
            print "right answer!"
        else:
            print "wrong answer!!"
            wrongones[question_dictionary[i][0]] = question_dictionary[i][1]
if wrongones == {}:
    print "all correct"
else:
    print "please check the wrong answers in wrong.txt"
    dictionary2txt("wrong.txt",wrongones)
        
    


            
      
    


    


            
    



