import json

class Question:
    def __init__(self, question_text, answers, entity, attribute):
        self.question_text = question_text
        self.answers = answers
        self.entity = entity
        self.attribute = attribute

class QuestionManager:
    def __init__(self):
        self.questions = []
        self.query_list = []
        self.load_questions()

    def load_questions(self):
        json_file_path = 'knowledge/questions.json'
        with open(json_file_path, 'r') as file:
            questions_data = json.load(file)
        for i in range(len(questions_data)):
            q = questions_data[str(i)]
            self.add_question(q['question'], q['answers'], q['entity'], q['attribute'])

    def add_question(self, question_text, answers, entity, attribute):
        answers_as_list = []
        for i in range(len(answers)):
            answers_as_list.append(answers[str(i)])

        question = Question(question_text, answers_as_list, entity, attribute)
        self.questions.append(question)
    
    def query(self, entity, attribute):
        for q in self.questions:
            if (q.entity == entity) and (q.attribute == attribute):
                self.query_list.append(q)
                return
            
    def unquery(self):
        self.query_list.pop(0)
