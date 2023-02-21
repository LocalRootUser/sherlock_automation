import subprocess
import sys
import os


# So i dont get copyrighted 
print("All rights go to Contributors who made the sherlock project\n(MIT © Sherlock Project Original Creator - "
      "Siddharth Dushantha)")
# Code starts here
start_path = "/"
directory_name = "sherlock"
sherlock_flags = " --verbose --timeout 5 --print-all --print-found --nsfw"

# walk through the directory tree and search for the directory of sherlock
print('Checking if sherlock exist in your system, please wait..')
for dirpath, dirnames, filenames in os.walk(start_path):
    if directory_name in dirnames:
        directory_path = os.path.join(dirpath, directory_name)
        print("Sherlock exists:", directory_path)
        target_username = input("Enter the target username: ")        # using sherlock in a new terminal
        terminal_command = f"cd {directory_path} && python3 sherlock {target_username} {sherlock_flags}"
        process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', terminal_command + '; read'], stdin=subprocess.PIPE)
        process.stdin.close()
        return_code = process.wait()
        print(f"{target_username} Users will be saved in the sherlock directory with a txt")
        print("Process returned:", return_code)
        sys.exit()
else:
    print("Sherlock was not found!")
    print("Do you want to install Sherlock on your home directory from github?")
while True:
    user_input = input("y/n? : ")
    if user_input == "y":
        print("""Installing Sherlock from github: "https://github.com/sherlock-project/sherlock.git" """)
        home_dir = os.path.expanduser("~")
        print("Current working directory:", os.getcwd())
        os.chdir(home_dir)
        print("New working directory:", os.getcwd())
        install_sherlock = "cd sherlock && python3 -m pip install -r requirements.txt"
        repo_url = "https://github.com/sherlock-project/sherlock.git"
        subprocess.run(["git", "clone", repo_url])
        print('Sherlock done installing.')
        print("Go ahead and run the program again.")
        break
    elif user_input == "n":
        print("closing")
        break
    else:
        print("invalid answer, try again")
