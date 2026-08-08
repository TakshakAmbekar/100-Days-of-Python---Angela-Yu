class Brain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        self.max_score = len(self.questions_list)
        
    
    def greet(self):
        print("Welcome to the Quiz Game!\n")
    
    def set_difficulty(self, clear):
        max_length = self.max_score
        while True:
            try:
                quiz_length = int(input(f"How many questions would you like? (max: {max_length})\n"))
                if 1 <= quiz_length <= max_length:
                    clear()
                    self.questions_list = self.questions_list[:quiz_length]
                    self.max_score = len(self.questions_list)
                    break
                else:
                    clear()
                    print(f"Please enter a valid number between 1 and {max_length}")
            except ValueError:
                clear()
                print(f"Please enter a valid number between 1 and {max_length}")

    def start(self, clear):
        self.greet()
        self.set_difficulty(clear)
        for _ in range(len(self.questions_list)):
            self.display_score(clear)
            self.ask()
        
    def ask(self):
        curr_question = self.questions_list[self.question_number]
        self.question_number += 1
        
        print(f"Q{self.question_number}. {curr_question.question}")
        while True:
            
            guess = input(f"Enter True/False: ").strip().title()
            if guess not in ('True', 'False'):
                continue
            if guess == curr_question.answer:
                self.score += 1
                return True
            return False
    
    def display_score(self, clear):
        clear()
        print(f"Current Score: {self.score}/{self.max_score}\n")
        
    def result(self, clear):
        total = len(self.questions_list)
        score = self.score
        
        clear() 
        
        print(f"You scored: {score}/{total}\n")
        if score < total / 2:
            print("You can do better...")
        elif score < 3 * total / 4:
            print("Keep it up!")
        elif score < 4 * total / 5:
            print("You did really well!!")
        else:
            print("You nailed it!!!")    