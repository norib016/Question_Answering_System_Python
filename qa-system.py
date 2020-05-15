import wikipedia
import sys
import os
import lxml
from nltk.chunk import tree2conlltags
import re
import nltk
from datetime import datetime
from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize

#Authors : Sree Nori

#Description:
#1) I built a Question Answering (QA) system using wikipedia toolkit which answers to Who, What, When and Where questions. 

#2) Ran the script in this format:
#C:\Users\bhanu\.spyder-py3> python qna.py mylogfile.txt
#This is a QA system by Sree Nori. It will try to answer questions that start with Who, What, When or Where. Enter exit to leave the program.

#How can I help you today?
#When was George Washington born? 
#George Washington was born on February 22, 1732.

#3) Algorithm:

#Step 1: Firstly, the user askes the system a question. The question is  Converted into title format and generate an NER tree for the question.
#Step 2: The system processes the question and matches it with regular expressions to retrieve the subject concerned with the question.
#Step 3: Depending on the type of the question, the system process it through the wikipedia library, using the summary function.
#Step 4: However, wikipedia uses why and how too. So we eliminate certain parts from the wiki result. The result should give us full length answers which are correct.
#Step 5: If the result is invalid from wikipedia, the system returns a standard reply.
#Step 6: We can exit the program when we type exit.

#Defining the main function for the program.








def main():
    try:
        log = open(sys.argv[1], "w+")
        print("Please enter a valid question, or type 'exit' to exit from the program:\n")
        counter = 1
        while True:
            s = input()
            e = s
            if s == "exit":
                print("\nThanks for using this program. Bye! :)\n")
                exit()
            log.write(str(counter) + "Q) " + s + "\n")
            #print(str(counter) + "Q) " + s + "\n")
            flag = False
            final = ""
            wiki = ""
            if s != "" and s is not None:
                s = s.title()
                n = token(s)
                #print('n is : ')
                #print(n)
                r = question(s)
                #print('r is : ')
                #print(r)
                if r!= "":
                    if ("Where" in s or "What" in s):
                        wiki = ans(r, log)
                        match = re.search(r'\d{4}', wiki)
                        if match is not None:
                            wiki = ""
                    if ('B-PERSON' or 'I-PERSON') in n[2]:
                        flag = True
                    elif ('I-PERSON' or 'B-PERSON') in n[2]:
                        flag = True
                    if "Who" in s and flag:
                        wiki = ans(r,log)
                    if ("When" in s or "Age" in s) and flag:
                        wiki = ans(r, log)
                        result = func(wiki)
                        if result != "":
                            if "Age" in s:
                                match = re.search(r'\d{4}', result)
                                if match is not None:
                                    result = datetime.now().year - int(match.group())
                            appends = reg(s, result)
                            if appends is not None:
                                final = s
                                #print("test")
                        else:
                            final = ""
                            #result = datetime.now().year - int(match.group())
                    else:
                        final = wiki
                else:
                    final = ""
                    #log.write(str(counter) + "A) Answer not found.\n\n")
            else:
                print("Please ask a valid question!")
            #print("test1\n")
            if final == "":
                log.write(str(counter) + "A) Answer not found.\n\n")
                print("I am sorry, I don't know the answer.\n")
            else:
                try:
                    log.write(str(counter) + "A) " + final + "\n\n")
                    #print(str(counter) + "A) " + final + "\n\n")
                    print(final + "\n")
                except Exception as GeneralException:
                    log.write(str(counter) + "A) Answer not found.\n\n")
                    print("I am sorry, I don't know the answer.\n")
            counter = counter + 1
            #print("test\n")
            print("Please ask another question or type 'exit' to exit from the program:\n")
    except Exception as GeneralException:
        print(GeneralException)
    finally:
        log.close()
        
def question(s):
    x = ""
    stats = [[r'Where (Is|Was) (.+)',["{0}"]],
             [r'Who (Is|Was) (.+)',["{0}"]],
             [r'What (Is|Was) (.+) Age',["{0}"]],
             [r'What (Is|Was) (.+)',["{0}"]],
             [r'When (Is|Was) (.+) Born',["{0}"]],
             #[r'When (Is|Was) (.+)',["{0}"]],
             [r'When (Is|Was) (.+) Birthday',["{0}"]]]
             #[r'When (Is|Was) (.+)',["{0}"]]]
    #print("test\n")
    for r, u in stats:
        m = re.match(r, s.rstrip('.!?'))
        if m:
            x = m.groups()[1]
            #x = m.groups(1)
            #print(x)
    return x

def token(u):
    tokens = word_tokenize(u)
    l = set(stopwords.words('english'))
    l.add('?')
    #l.add('!')
    string = []
    for i in tokens:
        if i not in l:
            string.append(i)
    #print("test\n")
    t = tree2conlltags(ne_chunk(pos_tag(word_tokenize(u))))
    return t        
        
        
def ans(query, log):
    try:
        #log.write(query + "\n")
        queryResult = wikipedia.summary(query, sentences=1)
        #queryResult = wikipedia.search(query, sentences=1)
        #queryResult.decode('ascii')
        #print("test\n")
    except Exception as GeneralException:
        queryResult = ""
    return queryResult

def func(s):
    m = ""
    stats = [[r'[\d]+\s(\w)+\s[\d]+',["{0}"]],
             [r'(?<=\().(\w+).(\w+,).(\w+)',["{0}"]]]
    for r, u in stats:
        #m1=re.searchall(r,s)
        #print(m1)
        m1 = re.search(r,s)
        if m1 is not None:
            m = match.group()
    return m

def reg(u, q):
    u = u.rstrip('.!?')
    ur = re.sub(r'When (Is|Was) (.+) Born', r'\2 Was Born On ', u)
    if ur != u:
        return ur + str(q) + '.'
    ur = re.sub(r'When (Is|Was) (.+) Birthday', r'\2 Birthday Is On ', u)
    if ur != u:
        ur = ur + q
        ur = re.sub(r'\d{4}', '', ur)
        return ur + '.'
    ur = re.sub(r'What (Is|Was) (.+) Age', r'\2 Age Is ', u)
    if ur != u:
        return ur + str(q) + '.'

main()