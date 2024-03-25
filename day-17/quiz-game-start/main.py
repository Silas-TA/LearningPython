from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# for look to iterate over questions in data
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0])
quiz = QuizBrain(question_bank)
quiz.get_question()