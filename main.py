from agents.orchestrator import Orchestrator

def main():
    print("AI Study Planner")
    name = input("Enter your name: ").strip()
    goal = input("Enter your main study goal: ").strip()
    subjects_raw = input("Enter subjects or topics separated by commas: ").strip()
    subjects = [s.strip() for s in subjects_raw.split(",") if s.strip()]
    days = int(input("Enter number of days you want to study: ").strip())
    hours_per_day = float(input("Enter how many hours per day you can study: ").strip())
    planner = Orchestrator()
    study_plan, eval_result = planner.run(name, goal, subjects, days, hours_per_day)
    print("\nGenerated Study Plan:\n")
    print(study_plan)
    print("\nEvaluation:")
    print("Score:", eval_result["score"])
    print("Feedback:", eval_result["feedback"])

if __name__ == "__main__":
    main()
