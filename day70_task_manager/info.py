print("Problem Statement")
"""
Using Python standard libraries, design and implement a mini task processing system that manages tasks assigned to users.

Use clean control flow and proper error handling
Duplicate task IDs are rejected with a custom exception
Tasks can be filtered by tags
Only timed tasks contribute to total duration


Create a base class Task with:
task_id (integer)
title (string)
tags (set of strings)



Create a derived class TimedTask that extends Task and adds:
duration (integer, in minutes)
Validation rules:
duration must be greater than 0, otherwise raise a ValueError



Define a custom exception:
DuplicateTaskError
Raised when a task with an existing task_id is added again



Create a decorator 
@log_execution that:
Prints the function name before execution
Prints "Completed" after execution, regardless of success or failure


Task Manager
Create a class TaskManager that:
Uses a list to store all tasks
Uses a dictionary to map task_id → task object



Methods

add_task(task)
Adds a task to the manager
Raises DuplicateTaskError if task_id already exists


get_tasks_by_tag(tag)
Returns a list of tuples (task_id, title)
Includes only tasks that contain the given tag



total_duration()
Returns the sum of durations of all TimedTask objects
Ignores tasks without duration

All public methods should be decorated with @log_execution.
Write unit tests to validate the requirements.
"""