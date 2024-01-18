import streamlit as st
from streamlit_js_eval import streamlit_js_eval


class ProblemSolverViewSt:
    def __init__(self, question_manager, problem_solver):

        self.col1, self.col2 = st.columns([2, 1])
        self.col1.title(":blue[Troubleshoot Your Water Pump] :gear: :droplet:")
        self.col2.markdown("<h3 style='text-align: center;'>"
                           "<b>"
                           "Here's what to do!"
                           "</b>"
                           "</h3>",
                           unsafe_allow_html=True)
        self.col2.write("Use this as a guide if your :blue[water pump is not working] as expected! "
                        "Answer a few questions and you'll get some :blue[advice] right here :point_down:")
        self.recs_container = self.col2.container(border=True)
        self.recs_container.markdown("<p style='font-size:20px; color:#2970E7;'><b>Solution:</b></p>", unsafe_allow_html=True)

        self.col2.write("You want to :blue[change your answer to a previous question]? "
                        "No problem! You can easily do so, just select a different answer. "
                        "You can also :blue[start from scratch] by pressing the button below!")
        if self.col2.button("Reset"):
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
        self.default_recommendation_container = self.recs_container.empty()
        self.default_recommendation_container.markdown("<h5 style='color: #938B84;'>"
                                                       "The recommended action could not yet be determined..."
                                                       "</h5>",
                                                       unsafe_allow_html=True)

        self.question_manager = question_manager
        self.problem_solver = problem_solver
        self.current_question = None
        self.selected_answer = None
        self.current_question_index = 0

        self.load_question()

    def load_question(self):
        self.current_question_index += 1

        # no more question left, display outcome
        if len(self.question_manager.query_list) == 0:
            st.toast("Recommendation generated.")
            self.default_recommendation_container.empty()
            self.recs_container.write(f" ##### :bulb: :ok_hand: :orange[{self.problem_solver.rule_model.outcome}]")

            return

        # set and display current question
        self.current_question = self.question_manager.query_list[0]
        self.col1.markdown(f"### {self.current_question.show_text()}")

        selected_option = self.col1.radio(
            "Select an option:",
            self.current_question.answers,
            key=self.current_question_index,
            index=None,
            format_func=lambda option: f"**{option}**"
        )

        if selected_option is not None:
            selected_index = self.current_question.answers.index(selected_option)
            self.next_question(selected_index)

    def next_question(self, selected_index):
        self.question_manager.unquery()
        self.problem_solver.change_status(self.current_question.entity, self.current_question.attribute,
                                          self.current_question.outcomes[selected_index])

        self.selected_answer = None

        self.problem_solver.solve_problem()
        st.empty()
        self.col1.empty()
        self.load_question()
