from catalyst.dl import ConfigExperiment


class Experiment(ConfigExperiment):
    def get_datasets(
        self,
        stage: str,
        **kwargs
    ):
        pass
