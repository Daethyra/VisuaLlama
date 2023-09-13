# Test all modules in the current directory
import os
import subprocess
import threading

# Run a python file
def run_python_file(python_file):
    print(f"Running {python_file}...")
    try:
        subprocess.run(['python', python_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Execution failed for {python_file} with error: {e}")

# Run all modules in the current directory
def run_all_modules_in_cwd():
    current_directory = os.getcwd()
    python_files = [f for f in os.listdir(current_directory) if f.endswith('.py')]

    threads = []
    for python_file in python_files:
        thread = threading.Thread(target=run_python_file, args=(python_file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All tests completed.")

if __name__ == '__main__':
    run_all_modules_in_cwd()
