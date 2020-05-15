This project implements a Question Answering (QA) system in Python called qa-system.py. 
The system will able to answer Who, What, When and Where questions (but not Why or How questions). 
It handles questions from any domain, and will provide answers in complete sentences that are specific to the questions asked. 
The system takes an approach similar to that of the AskMSR system, and simply reformulates the questions as a series of "answer patterns" that we then search for in Wikipedia, where it
finds an exact match to one of our patterns. 

For example, 
  suppose the question was "Where is Malosky Stadium?". 
  "Malosky Stadium is located in", "Malosky Stadium is found in" or even "The address of Malosky Stadium is". 
  
Multiple patterns are associated with each possible type of question (Who, What, When, and Where).

wikipedia.summary() is used to interact with Wikipedia.
The program runs interactively, and prompts the user for questions until the user says "exit".

Run "$ python qa-system.py mylogfile.txt" in the command line and this is how it interacts:
*** This is a QA system by YourName. It will try to answer questions
that start with Who, What, When or Where. Enter "exit" to leave the
program.
=?> When was George Washington born? (user)
=> George Washington was born on February 22, 1732. (system)
=?> What is a bicycle?
=> A bicycle has two wheels and is used for transportation.
=?> Where is Duluth, Minnesota?
=>I am sorry, I don't know the answer.
=?> exit
Thank you! Goodbye. ********

In addition to the program, a plain text file called qa-samples.txt is provided which includes 20
factual questions - five for each of the Who, What, When, and Where type. 
Example"
Question : When was George Washington born?
Correct Answer : George Washington was born on February 22, 1732.
System Answer : George Washington was born on February 22, 1732. (correct)
System Answer : George Washington was born ......(incorrect)
 
