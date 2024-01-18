import streamlit as st

class ProblemSolverViewSt:
    def __init__(self, question_manager, problem_solver):
        st.title("Waterpump troubleshooting")
        st.sidebar.header("Recommended action")
        st.sidebar.write("The recommended action could not yet be determined.")

        self.question_manager = question_manager
        self.problem_solver = problem_solver
        self.current_question = None
        self.selected_answer = None
        self.current_question_index = 0
        #print("first q loading") works but twice??
        self.load_question()

    def load_question(self):
        self.current_question_index += 1

        # no more question left, display outcome
        if len(self.question_manager.query_list) == 0:
            st.sidebar.empty()
            st.sidebar.write(self.problem_solver.rule_model.outcome)
            return

        # set and display current question
        self.current_question = self.question_manager.query_list[0]
        #st.write(self.current_question.show_text())

        # display options
        #for i, option in enumerate(self.current_question.answers):
        #    button_key = f"{self.current_question_index}_{i}"
        #    if st.button(option):
        #        self.on_option_click(i)

        selected_option = st.radio(self.current_question.show_text(), self.current_question.answers, index=None)
        # possibly disable button after selection
        if selected_option is not None:
            selected_index = self.current_question.answers.index(selected_option)
            self.on_option_click(selected_index)

    def on_option_click(self, selected_option):
        print(f"Selected option: {selected_option}")
        self.next_question(selected_option)

    def next_question(self, selected_index):
        #print("selected index: ", selected_index)
        self.question_manager.unquery()
        self.problem_solver.change_status(self.current_question.entity, self.current_question.attribute, self.current_question.outcomes[selected_index])

        self.selected_answer = None

        self.problem_solver.solve_problem()
        st.empty()
        self.load_question()