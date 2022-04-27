import json
from random import shuffle
from os.path import isfile
from generic_question import GenericQuestion



QUESTIONS_FILE_NAME = 'questions.json' # Создадим подсчет


def load_questions(): #Функция производит Запись данных из json
    if isfile(QUESTIONS_FILE_NAME):
        with open(QUESTIONS_FILE_NAME, 'r', encoding='UTF-8') as file:
            questions_raw = json.load(file)
        return questions_raw
    else:
        print('такого вопроса не существует')
        exit()


def from_question_list(questions_raw): #обрабатывает вопросы
    questions = []
    for question_new in questions_raw:
        if 'text' in question_new and 'difficulty' in question_new and 'answers' in question_new:
            text = question_new['text']
            if not text.strip():
                continue
            author = question_new['author'] if 'author' in question_new else 'unknown'
            author = 'unknown' if not author.strip() else author
            difficulty = question_new['difficulty']
            if not difficulty.strip():
                continue
            answers = []
            for answer in question_new['answers']:
                if not answer.strip():
                    continue
                answers.append(answer.lower())
            if len(answers) < 1:
                continue
            topic = question_new['topic'] if 'topic' in question_new else 'general'
            topic = 'general' if not topic.strip() else topic
        else:
            continue
    question = question_list()
    question.set_text(questions_raw[question_new]['text'], True)
    question.set_author(questions_raw[question_new]['author'], True)
    question.set_difficulty(questions_raw[question_new]['difficulty'], True)
    question.set_answers(questions_raw[question_new]['answers'], True)
    question.set_topic(questions_raw[question_new]['topic'], True)
    questions.append(questions)
    random.shuffle(questions)
    return questions


def get_statistic(questions): #подсчет статистики
    correct_answers = 0
    total_questions = 0
    for question in questions:
        if question.asked:
            total_questions += 1
            if question.user_answer.lower() in question.answers:
                correct_answers += 1
    return correct_answers, total_questions - correct_answers, total_questions


def main(): #Основной код
    questions = from_question_list
    user_scores = 0
    for question in questions:
        print(question.build_question())
        question.asked = True
        answer = input()
        question.user_answer = answer
        if question.is_correct(answer):
            scores = question.get_scores()
            user_scores += scores
            print(f'Ответ верный, вы получаете {scores} очков')
        else:
            print(f' ответ неверный. На самом деле тответ -{question.answers[0]}')

    correct_answers, incorrect_answers, total_questions = get_statistic(questions)
    print('вот и все')
    print(f'вы набрали {user_scores} очков')
    print(f' правильных ответов {correct_answers} вопросов из {total_questions} неверных ответов - {incorrect_answers}')


if __name__ == '__main__':
    main()
