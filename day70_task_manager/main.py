class DuplicateTaskError(Exception):
    pass


class Task:
    def __init__(self, task_id, title, tags):
        self.task_id: int = task_id
        self.title: str = title
        self.tags: set[str] = set(tags)






class TimedTask(Task):
    def __init__(self, task_id, title, tags, duration):
        super().__init__(task_id, title, tags)
        self.duration = duration

        if self.duration <= 0:
            raise ValueError("Duration Must be greater than 0")



TASK_LIST = []
class TaskManager():
    def __init__(self, task_id, title, tags):
        task = Task()
        TASK_LIST.append({task.task_id: task})

    def add_task(task):
        if task.task_id in TASK_LIST:
            raise DuplicateTaskError("Task already exists")
        else:
            TASK_LIST.append(task)


def log_execution(func):
    def wrapper():
        print(f"Function : {func}")
        func()
        print("completed")
    return wrapper

work = TimedTask(2, "work", ("important", ), duration=120)
work2 = TimedTask(2, "running", ("personal", ), duration=120)
TaskManager.add_task(work)
TaskManager.add_task(work2)
print([(i.task_id, i.title) for i in TASK_LIST])
print(work.task_id, work.title, work.tags)
