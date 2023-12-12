def read_course_data(file_path):
    courses = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                course_info = line.strip().split()
                courses.append(course_info)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return courses

def display_courses(courses):
    course_crns = set(course[0] for course in courses)
    print("Available courses:")
    for course_crn in sorted(course_crns):
        print(course_crn)

def number_of_courses():
    while True:
        try:
            n = int(input("How many courses would you like to register for? "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please input an integer.")

def enter_course_numbers(courses, n):
    selected_courses = set()
    for i in range(n):
        while True:
            course_number = input(f"Enter course number {i + 1}:").upper()
            conflicting_courses = get_conflicting_courses(course_number, selected_courses, courses)

            if not conflicting_courses:
                selected_courses.add(course_number)
                break
            else:
                print(f"Conflicting courses detected: {', '.join(conflicting_courses)}")
                print("Please enter a valid course number")

    return selected_courses

def get_conflicting_courses(new_course, selected_courses, courses):
    conflicting_courses = set()

    for selected_course in selected_courses:
        print(f"New Course: {new_course}, Selected Course: {selected_course}")
        if time_overlap(get_course_info(new_course, courses), get_course_info(selected_course, courses)):
            print("Time overlap detected.")
            conflicting_courses.add(selected_course)

    return conflicting_courses

def get_course_info(course_number, courses):
    for course in courses:
        if course[0] == course_number:
            return course

    return None
        
def generate_schedule(courses, selected_courses):
    def backtrack(schedule, selected_times):
        for course in courses:
            if course[0] in selected_courses and course[0] not in (c[0] for c in schedule):
                try:
                    course_number, section, days, start_time, end_time = course
                    course_time = (course_number, days, start_time, end_time)

                    if not has_time_conflict(course_time, selected_times):
                        schedule.append(course)
                        selected_times.add(course_time)

                        if len(schedule) == len(selected_courses):
                            # All courses are scheduled, return the result
                            return schedule

                        result = backtrack(schedule, selected_times)

                        if result:
                            return result

                        # If the current course didn't lead to a valid schedule, backtrack
                        schedule.pop()
                        selected_times.remove(course_time)
                except ValueError:
                    print(f"Debugging: ValueError in course data: {course}")

        # No valid schedule found
        return None

    return backtrack([], set())


def has_time_conflict(course, selected_times):
    for existing_time in selected_times:
        if time_overlap(course, existing_time):
            return True
    return False

def time_overlap(time1, time2):
    try:
        days_overlap = any(day in time1[2] for day in time2[2]) or any(day in time2[2] for day in time1[2])
        time1_start, time1_end = int(time1[3]), int(time1[4])
        time2_start, time2_end = int(time2[3]), int(time2[4])
        time_conflict = (time1_start < time2_end and time1_end > time2_start) or (time2_start < time1_end and time2_end > time1_start)

        return days_overlap and time_conflict
    except IndexError:
        print(f"Debugging: IndexError in time data: {time1}")
        return False

def display_schedule(schedule):
    if not schedule:
        print("A valid schedule could not be generated.")
    else:
        print ("\nYour Schedule")
        for course in schedule:
            print (f"Course: {course [0]} Section: {course[1]} Days: {course[2]} Time: {course[3]} - {course[4]}")

def main():
    file_path = "file2.txt"
    courses = read_course_data(file_path)

    if not courses:
        print("No course data available. Exiting.")
        return

    display_courses(courses)

    n = number_of_courses()
    selected_courses = enter_course_numbers(courses, n)

    schedule = generate_schedule(courses, selected_courses)

    display_schedule(schedule)

if __name__ == "__main__":
    main()