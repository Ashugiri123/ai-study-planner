class TimeTool:
    def allocate_time(self, subjects, days, hours_per_day):
        total_minutes_per_day = int(hours_per_day * 60)
        subjects_count = max(len(subjects), 1)
        base_minutes_per_subject = total_minutes_per_day // subjects_count
        allocation = {}
        for day in range(1, days + 1):
            allocation[day] = {}
            for subject in subjects:
                allocation[day][subject] = base_minutes_per_subject
        return allocation
