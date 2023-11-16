def read_course_data(file_path):
    courses = []
    with open(file_path, 'r') as file:
        for line in file:
            course_info = line.strip().split()
            courses.append(course_info)
    return

def display_courses(courses):
    course_crns = set(course[0] for course in courses)
    print("Available courses:")
    for course_crn in sorted(course_crns):
        print(course_crn)

def number_of_courses():
    while True:
        try:
            n = int(input("How many courses would you like to register for?"))
            if n > 0:
                return n
            else:
                print ("Please enter a positive integer")
        except ValueError:
            print ("Invalid input. Please input an integer")

def enter_course_numbers(courses, n):
    selected_courses = set()
    for i in range(n):
        while True:
            course_number = input(f"Enter course number {i + 1}:").upper()
            if any(course_number == course[0] for course in courses):
                selected_courses.add(course_number)
                break
            else:
                print("Please enter a valid course number")
            return selected_courses
        
def generate_schedule(courses, selected_courses):
    schedule = []
    for course in courses:
        if course[0] in selected_courses:
            schedule.append(course)

    return schedule

def display_schedule(schedule):
    if not schedule:
        print("A valid schedule could not be generated.")
    else:
        print ("\nYour Schedule")
        for course in schedule:
            print (f"Course: {course [0]} Section: {course[1]} Days: {course[2]} Time: {course[3]} - {course[4]}")

def main():
    file_path = file.txt
    courses = read_course_data(file_path)

    display_courses(courses)

    n = number_of_courses()
    selected_courses = enter_course_numbers(courses, n)

    schedule = generate_schedule(courses, selected_courses)

    display_schedule(schedule)

    if __name__ == "__main__":
        main()


