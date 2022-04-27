from random import shuffle
from os.path import isfile


question_num = 0


class GenericQuestion:
    def __init__(self):
        self.text = ""
        self.author = ""
        self.difficulty = ""
        self.answers = ""
        self.topic = ""
        self.asked = None
        self.user_answer = None


class Question(GenericQuestion):
    def _set_text(self, text):
        self.text = text
    def _set_author(self, author):
        self.author = author
    def _set_difficulty(self, difficulty):
        self.difficulty = difficulty
    def _set_answers(self, answers):
        self.answers = answers
    def _set_topic(self, topic):
        self.topic = topic
    def _set_asked(self, asked):
        self.asked = asked
    def _set_user_answer(self, user_answer):
        self.user_answer = user_answer




    def get_scores(self):
        return int(int(self.difficulty) * 10) #Подсчет очков

    def is_correct(self, answer):
        return True if answer.lower() in self.answers else False   # корректность ответа

    def build_question(self, question_number = False): # возврат строоки с вопросом
        self.question_number = question_number
        question_number += 1
        return f'вопрос: {question_number},  тема: {self.topic} сложность: {self.difficulty}\n{self.text}'