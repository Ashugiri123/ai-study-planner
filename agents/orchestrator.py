from memory.session_memory import SessionMemory
from memory.long_term_memory import LongTermMemory
from agents.planner_agent import StudyPlannerAgent
from agents.research_agent import ResearchAgent
from agents.eval_agent import EvaluationAgent
from observability.logger import Logger

class Orchestrator:
    def __init__(self):
        self.session_memory = SessionMemory()
        self.long_term_memory = LongTermMemory()
        self.planner = StudyPlannerAgent()
        self.researcher = ResearchAgent()
        self.evaluator = EvaluationAgent()
        self.logger = Logger()

    def run(self, name, goal, subjects, days, hours_per_day):
        self.logger.log("start_run", {"name": name, "goal": goal})
        profile = self.long_term_memory.load_profile(name) or {}
        profile.update(
            {
                "name": name,
                "goal": goal,
                "subjects": subjects,
                "days": days,
                "hours_per_day": hours_per_day,
            }
        )
        self.long_term_memory.save_profile(name, profile)
        self.session_memory.set("profile", profile)
        base_plan = self.planner.create_plan(subjects, days, hours_per_day)
        self.logger.log("plan_created", {"days": days, "subjects_count": len(subjects)})
        resources = self.researcher.find_resources(subjects)
        self.logger.log("resources_found", {"subjects_count": len(resources)})
        combined_plan = self.planner.attach_resources(base_plan, resources)
        evaluation = self.evaluator.evaluate(combined_plan, days, hours_per_day)
        self.logger.log("plan_evaluated", evaluation)
        if evaluation["score"] < 70:
            improved_plan = self.planner.improve_plan(combined_plan, evaluation)
            improved_evaluation = self.evaluator.evaluate(improved_plan, days, hours_per_day)
            self.logger.log("plan_improved", improved_evaluation)
            return self.planner.format_plan(improved_plan), improved_evaluation
        return self.planner.format_plan(combined_plan), evaluation
