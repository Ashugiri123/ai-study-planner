from tools.time_tool import TimeTool

class StudyPlannerAgent:
    def __init__(self):
        self.time_tool = TimeTool()

    def create_plan(self, subjects, days, hours_per_day):
        allocation = self.time_tool.allocate_time(subjects, days, hours_per_day)
        plan = {}
        for day in range(1, days + 1):
            sessions = []
            for subject in subjects:
                minutes = allocation[day][subject]
                if minutes > 0:
                    sessions.append(
                        {
                            "subject": subject,
                            "minutes": minutes,
                            "resources": [],
                        }
                    )
            plan[day] = sessions
        return plan

    def attach_resources(self, plan, resources):
        for day, sessions in plan.items():
            for session in sessions:
                subject = session["subject"]
                session["resources"] = resources.get(subject, [])
        return plan

    def improve_plan(self, plan, evaluation):
        if evaluation.get("too_many_minutes"):
            factor = 0.9
            for day, sessions in plan.items():
                for session in sessions:
                    session["minutes"] = int(session["minutes"] * factor)
        return plan

    def format_plan(self, plan):
        lines = []
        for day in sorted(plan.keys()):
            lines.append("Day " + str(day) + ":")
            sessions = plan[day]
            if not sessions:
                lines.append("  Rest day or light review.")
            for session in sessions:
                line = "  " + session["subject"] + " - " + str(session["minutes"]) + " minutes"
                lines.append(line)
                for r in session["resources"]:
                    lines.append("    Resource: " + r)
            lines.append("")
        return "\n".join(lines)
