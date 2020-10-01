class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Who Invented Python \n(a) Guido van Rossum\n(b)Dennis Ritchie",
     "Which Year Python Was Realesed ?\n(a) 1991\n(b)1996",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "a"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)