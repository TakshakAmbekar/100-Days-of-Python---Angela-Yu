class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
    def check_answer(self, guess):
        if guess == self.answer:
            return True
        return False