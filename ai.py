import time
import datetime

class VirtualAssistant:
    """A basic virtual assistant framework."""

    def __init__(self,
    name="Assistant"):
        self.name = name
        self.tasks = {}  # Store tasks as a dictionary {task_name: due_date}

    def greet(self):
        """Greets the user."""
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            print(f"Good morning!")
        elif 12 <= hour < 18:
            print(f"Good afternoon!")
        else:
            print(f"Good evening!")
        print(f"I am {self.name}. How can I help you?")

    def process_command(self, command):
        """Processes user commands."""
        command = command.lower()

        if "hello" in command or "hi" in command:
            print("Hello there!")
        elif "time" in command:
            now = datetime.datetime.now()
            print(f"The current time is: {now.strftime('%H:%M:%S')}")
        elif "date" in command:
            now = datetime.datetime.now()
            print(f"Today's date is: {now.strftime('%Y-%m-%d')}")
        elif "set reminder" in command or "add task" in command:
            self.add_task(command)
        elif "list tasks" in command or "show tasks" in command:
            self.list_tasks()
        elif "goodbye" in command or "exit" in command:
            print("Goodbye!")
            return False #signals exit
        else:
            print("I'm sorry, I don't understand that command.")
        return True #signals continue.

    def add_task(self, command):
        """Adds a task to the task list."""
        try:
            parts = command.split("task")
            task_details = parts[1].strip()
            task_parts = task_details.split("due")

            task_name = task_parts[0].strip()
            due_date_str = task_parts[1].strip()

            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") #example date format.

            self.tasks[task_name] = due_date
            print(f"Task '{task_name}' added with due date: {due_date.strftime('%Y-%m-%d')}")
        except (IndexError, ValueError):
            print("Invalid task format. Please use 'add task [task name] due [YYYY-MM-DD]'")

    def list_tasks(self):
        """Lists all tasks."""
        if not self.tasks:
            print("You have no tasks.")
        else:
            print("Tasks:")
            for task, due_date in self.tasks.items():
                print(f"- {task}: Due {due_date.strftime('%Y-%m-%d')}")

def main():
    assistant = VirtualAssistant("Python Assistant")
    assistant.greet()

    running = True
    while running:
        command = input("Enter command: ")
        running = assistant.process_command(command)
if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.greet()


