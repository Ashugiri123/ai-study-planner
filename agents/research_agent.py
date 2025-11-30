from tools.search_tool import SearchTool

class ResearchAgent:
    def __init__(self):
        self.search_tool = SearchTool()

    def find_resources(self, subjects):
        resources = {}
        for subject in subjects:
            resources[subject] = self.search_tool.search_resources(subject)
        return resources
