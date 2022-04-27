import json
from random import shuffle
from os.path import isfile

QUESTIONS_FILE_NAME = '../questions.json'
question_num = 0


class GenericQuestion:
    def __init__(self, text, author, difficulty, answers, topic, asked = False, user_answer=''):
        self.text = text
        self.author = author
        self.difficulty = difficulty
        self.answers = answers
        self.topic = topic
        self.asked = asked
        self.user_answer = user_answer


class Question(GenericQuestion):

    def get_scores(self):
        return int(int(self.difficulty) * 10)

    def is_correct(self, answer):
        return True if answer.lower() in self.answers else False

    def build_question(self, question_num = False):
        self.question_num = question_num
        question_num += 1
        return f'вопрос: {question_num},  тема: {self.topic} сложность: {self.difficulty}\n{self.text}'

def load_questions():
  if isfile(QUESTIONS_FILE_NAME):
      with open(QUESTIONS_FILE_NAME, 'r', encoding='UTF-8') as file:
          questions_raw = json.load(file)
  else:
      print('такого вопроса не существует')
      exit()
  questions = []
  for question_raw in questions_raw:
      if 'text' in question_raw and 'difficulty' in question_raw and 'answers' in question_raw:
          text = question_raw['text']
          if not text.strip():
              continue
          author = question_raw['author'] if 'author' in question_raw else 'unknown'
          author = 'unknown' if not author.strip() else author
          difficulty = question_raw['difficulty']
          if not difficulty.strip():
              continue
          answers = []
          for answer in question_raw['answers']:
              if not answer.strip():
                  continue
              answers.append(answer.lower())
          if len(answers) < 1:
              continue
          topic = question_raw['topic'] if 'topic' in question_raw else 'general'
          topic = 'general' if not topic.strip() else topic
      else:
          continue
      questions.append(Question(text, author, difficulty, answers, topic))
  shuffle(questions)
  return questions

def get_statistic(questions):
    correct_answers = 0
    total_questions = 0
    for question in questions:
        if question.asked:
            total_questions +=1
            if question.user_answer.lower() in question.answers:
                correct_answers+=1
    return correct_answers, total_questions - correct_answers, total_questions

def main():
    questions = load_questions()
    user_scores = 0
    for question in questions:
        print(question.build_question())
        question.asked = True
        answer = input()
        question.user_answer = answer
        if question.is_correct(answer):
            scores = question.get_scores()
            user_scores+= scores
            print(f'Ответ верный, вы получаете {scores} очков')
        else:
            print(f' ответ неверный. На самом деле ответ -{question.answers[0]}')

    correct_answers, incorrect_answers, total_questions = get_statistic(questions)
    print('вот и все')
    print(f'вы набрали {user_scores} очков')
    print (f' правильных ответов {correct_answers} вопросов из {total_questions} неверных ответов - {incorrect_answers}')

if __name__ == '__main__':
    main()


