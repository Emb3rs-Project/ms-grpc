import traceback


class SimulationWrapper:
    def __init__(self, project_path: str):
        self.project_path = project_path

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            trace = traceback.format_exc()
            trace = trace.replace(self.project_path, "")
            raise Exception(f"{exc_val} Trace: {trace}")
