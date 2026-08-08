from data import question_data
from question_model import Question
from quiz_brain import Brain
import os, random


def clear():
    os.system("cls" if os.name == "nt" else "clear")

question_bank = []


for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)
    
random.shuffle(question_bank)
quiz_length = 0
max_length = len(question_bank)

clear() 
    
brain = Brain(question_bank)

brain.start(clear)

brain.result(clear)
