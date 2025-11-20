# Name: ANIKET AHIRWAR
# Enrollment: 0103CS231054
# Batch: 6
# Batch Time: 12:10 PM - 1:50 PM



# ---------- QUIZ SYSTEM ------------

import random

STUDENT_FILE = "students.txt"
SCORE_FILE = "scores.txt"

def register():
    print("STUDENT REGISTRATION")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(STUDENT_FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username:
                print(" Username already exists!")
                return

    name = input("Enter full name: ")
    roll = input("Enter roll number: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    branch = input("Enter your branch: ")
    year = input("Enter your current year: ")
    dob = input("Enter your DOB: ")
    address = input("Enter your address: ")
    gender = input("Enter your gender: ")

    with open(STUDENT_FILE, "a") as f:
        f.write(username + "|" + password + "|" + name + "|" + roll + "|" + email + "|" + phone + "|" + branch + "|" + year + "|" + dob + "|" + address + "|" + gender )

    print("Registration successful!")

def login():
    print("LOGIN")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "admin123":
        print("Hello Admin")
        admin_menu()
        return

    with open(STUDENT_FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username and data[1] == password:
                print(" Welcome ", data[2])
                student_menu(username)
                return
    print("wrong username or password")

def show_profile(username):
    with open(STUDENT_FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username:
                print("Student Profile:")
                print("Name:", data[2])
                print("Roll No:", data[3])
                print("Email:", data[4])
                print("Phone:", data[5])
                print("Branch:", data[6])
                print("Year:", data[7])
                print("DOB:", data[8])
                print("Address:", data[9])
                print("Gender:", data[10])
                print()
                return
    print("Profile not found")

def update_profile(username):
    lines = []
    updated = False

    with open(STUDENT_FILE, "r") as f:
        lines = f.readlines()

    with open(STUDENT_FILE, "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == username:
                print("UPDATE PROFILE")
                new_name = input("Enter new Name (" + data[2] + "): ")
                if new_name != "":
                    data[2] = new_name
                new_email = input("Enter new Email (" + data[4] + "): ")
                if new_email != "":
                    data[4] = new_email
                new_contact = input("Enter new Contact (" + data[5] + "): ")
                if new_contact != "":
                    data[5] = new_contact
                new_branch = input("Enter new Branch (" + data[6] + "): ")
                if new_branch != "":
                    data[6] = new_branch
                new_year = input("Enter new Year (" + data[7] + "): ")
                if new_year != "":
                    data[7] = new_year
                updated = True
            f.write("|".join(data) + "\n")

    if updated:
        print("Profile updated successfully")
    else:
        print("profile not found")

def get_questions(category):
    if category == "DSA":
        return [
            ("Which data structure uses LIFO?", ["A. Queue", "B. Stack", "C. Array", "D. Tree"], "B"),
            ("Which traversal is used in DFS?", ["A. Level", "B. Preorder", "C. Inorder", "D. Postorder"], "B"),
            ("What is the time complexity of binary search?", ["A. O(n)", "B. O(n^2)", "C. O(log n)", "D. O(1)"], "C"),
            ("Which structure uses FIFO?", ["A. Stack", "B. Queue", "C. Graph", "D. Array"], "B"),
            ("Which is not linear DS?", ["A. Stack", "B. Queue", "C. Tree", "D. Array"], "C")
        ]
    elif category == "DBMS":
        return [
            ("DBMS stands for?", ["A. DataBase Manage System", "B. DataBase Management System", "C. Data Management System", "D. None"], "B"),
            ("Which key uniquely identifies a record?", ["A. Primary key", "B. Foreign key", "C. Super key", "D. Candidate key"], "A"),
            ("SQL stands for?", ["A. Structured Query Language", "B. Standard Query Language", "C. Simple Query Language", "D. None"], "A"),
            ("Which normal form removes transitive dependency?", ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"], "C"),
            ("Which command is used to remove table?", ["A. DELETE", "B. REMOVE", "C. DROP", "D. ERASE"], "C")
        ]
    elif category == "PYTHON":
        return [
            ("Python is a ____ language?", ["A. High-level", "B. Low-level", "C. Machine", "D. Assembly"], "A"),
            ("Which keyword defines a function?", ["A. func", "B. def", "C. define", "D. function"], "B"),
            ("Lists are enclosed in?", ["A. {}", "B. []", "C. ()", "D. <>"], "B"),
            ("Which is not a keyword?", ["A. pass", "B. eval", "C. assert", "D. else"], "B"),
            ("Which library is used for math?", ["A. calc", "B. num", "C. math", "D. number"], "C")
        ]
    return []

def attempt_quiz(username):
    print("QUIZ CATEGORIES")
    print(""" 1. DSA
              2. DBMS
              3. PYTHON """)
    choice = input("Choose category(1/2/3): ")

    if choice == "1":
        category = "DSA"
    elif choice == "2":
        category = "DBMS"
    elif choice == "3":
        category = "PYTHON"
    else:
        print(" Invalid choice!")
        return

    questions = get_questions(category)
    random.shuffle(questions)
    score = 0
    total = len(questions)

    for i, (q, opts, ans) in enumerate(questions, start=1):
        print("Q" + str(i) + ". " + q)
        for o in opts:
            print(o)
        user_ans = input("Enter answer (A/B/C/D): ").upper()
        if user_ans == ans:
            score += 1

    print(f"You scored {score}/{total}")

    with open(SCORE_FILE, "a") as f:
        f.write(f"{username}|{category}|{score}/{total}\n")

def view_score(username):
    print("YOUR QUIZ SCORE:")
    found = False
    with open(SCORE_FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username:
                print(f"Category: {data[1]} | Score: {data[2]}")
                found = True
    if not found:
        print("No scores found")

def admin_menu():
    while True:
        print("ADMIN MENU")
        print("1. View scores")
        print("2. Exit Admin Panel")
        choice = input("Enter the choice: ")

        if choice == "1":
            print(" All quiz scores:")
            with open(SCORE_FILE, "r") as f:
                for line in f:
                    print(line.strip())
        elif choice == "2":
            break
        else:
            print("Invalid choice")

def student_menu(username):
    while True:
        print("STUDENT MENU")
        print("1. Show Profile")
        print("2. Update Profile")
        print("3. Attempt Quiz")
        print("4. View Score")
        print("5. Logout")
        ch = input("Enter your choice: ")

        if ch == "1":
            show_profile(username)
        elif ch == "2":
            update_profile(username)
        elif ch == "3":
            attempt_quiz(username)
        elif ch == "4":
            view_score(username)
        elif ch == "5":
            print("Logged out!")
            break
        else:
            print("Invalid choice!")

def main():
    open(STUDENT_FILE, "a").close()
    open(SCORE_FILE, "a").close()

    while True:
        print("STUDENT QUIZ SYSTEM")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            register()
        elif ch == "2":
            login()
        elif ch == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()