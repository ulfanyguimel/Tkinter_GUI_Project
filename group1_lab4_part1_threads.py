import time
import threading

def do_task(task_name):
    """Does a task that takes a while by looping and pausing."""
    for _ in range(100_000):
        time.sleep(0.000_1)
    print(f"Task {task_name} is done.")

def run_tasks_one_by_one(count):
    """Runs the task one at a time and checks how long it takes."""
    start_time = time.time()
    for i in range(count):
        do_task(f"Task-{i+1}")
    end_time = time.time()
    print(f"Doing tasks one by one took {end_time - start_time:.4f} seconds.")

def run_tasks_at_same_time(count):
    """Runs the task using threads and checks how long it takes."""
    threads = []
    start_time = time.time()
    for i in range(count):
        thread = threading.Thread(target=do_task, args=(f"Thread-{i+1}",))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Doing tasks at the same time took {end_time - start_time:.4f} seconds.")

# Run the functions 10 times like the instructions say
print("Running tasks one at a time 10 times:")
run_tasks_one_by_one(10)

print("\nRunning tasks at the same time 10 times:")
run_tasks_at_same_time(10)