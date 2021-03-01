class InterventionSaveUseCase:
    def __init__(self, repo, inter):
        self.repo = repo
        self.inter = inter

    def execute(self):
        return self.repo.save(self.inter)
