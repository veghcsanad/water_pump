import streamlit as st

class ProblemSolverViewSt:
    def __init__(self, question_manager, problem_solver):
        st.title("Waterpump troubleshooting")
        st.sidebar.header("Recommended action")
        st.sidebar.write("The recommended action could not yet be determined.")

        self.question_manager = question_manager
        self.problem_solver = problem_solver
        self.question = None
        self.selected_answer = None
        self.current_question_index = 0

        self.load_question()

    def load_question(self):
        self.current_question_index += 1
        if len(self.question_manager.query_list) == 0:
            st.sidebar.empty
            st.sidebar.write(self.problem_solver.rule_model.outcome)
            return

        self.question = self.question_manager.query_list[0]
        st.write(self.question)
        for i, option in enumerate(self.question.answers, start=1):
            st.button(option, key=f"{self.current_question_index}_{i}")

        for i, _ in enumerate(self.question.answers, start=1):
            if st.button(f"{self.current_question_index}_{i}"):
                selected_option = self.question.answers[i-1]
                self.next_question(selected_option)

    def next_question(self, selected_index):
        self.question_manager.unquery()
        self.problem_solver.change_status(self.question.entity, self.question.attribute, self.question.outcomes[selected_index])

        self.selected_answer = None

        self.problem_solver.solve_problem()
        st.empty()
        self.load_question()