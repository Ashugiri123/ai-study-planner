class SearchTool:
    def search_resources(self, subject):
        subject_lower = subject.lower()
        if "math" in subject_lower:
            return [
                "Khan Academy - Mathematics",
                "YouTube - Math Exam Preparation",
            ]
        if "physics" in subject_lower:
            return [
                "HyperPhysics - Physics Concepts",
                "YouTube - Physics Crash Course",
            ]
        if "chem" in subject_lower:
            return [
                "ChemGuide - Chemistry Concepts",
                "YouTube - Organic Chemistry Basics",
            ]
        return [
            "Search online for: " + subject + " basics",
            "YouTube: Beginner guide to " + subject,
        ]
