class QuizBrain:

    def __init__(self, question_bank):
        self.question = question_bank
        self.count = 0
        self.total = len(question_bank)
        self.running = True

    def get_question(self):
        score = 0
        while self.count <= self.total:
            question = self.question[self.count]
            choice = input(f"Q.{self.count}. {question.text} (True/False): " )
            if choice.lower() == question.answer.lower():
                self.count += 1
                score += 1
                print(f"Congratulations, you got it right.")
                print("\n")
            else:
                print(f"Better luck next time. Your total score is {score}/{self.total}")
                return
        print(f"Your total score is {score}/{self.total}")
