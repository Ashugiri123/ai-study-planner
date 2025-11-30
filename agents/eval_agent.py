class EvaluationAgent:
    def evaluate(self, plan, days, hours_per_day):
        total_minutes_per_day_allowed = hours_per_day * 60
        max_minutes_any_day = 0
        days_count = 0
        for day, sessions in plan.items():
            days_count += 1
            day_minutes = sum(session["minutes"] for session in sessions)
            if day_minutes > max_minutes_any_day:
                max_minutes_any_day = day_minutes
        score = 100
        too_many_minutes = False
        if max_minutes_any_day > total_minutes_per_day_allowed:
            score -= 20
            too_many_minutes = True
        if days_count < days:
            score -= 10
        feedback_parts = []
        if too_many_minutes:
            feedback_parts.append("Some days have more minutes than you planned to study.")
        if days_count < days:
            feedback_parts.append("Some days have no study sessions, consider adding light review.")
        if not feedback_parts:
            feedback_parts.append("Plan looks balanced and realistic.")
        feedback = " ".join(feedback_parts)
        return {"score": score, "feedback": feedback, "too_many_minutes": too_many_minutes}
