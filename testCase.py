import unittest
from unittest.mock import patch
from io import StringIO
from project2 import read_course_data, display_courses, number_of_courses, enter_course_numbers, generate_schedule, display_schedule

class TestCourseSchedulingSystem(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "CS120"])
    def test_course_scheduling(self, mock_input):
        file_path = "file.txt"

        # Redirect stdout to capture print statements
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            courses = read_course_data(file_path)
            display_courses(courses)

            n = number_of_courses()
            selected_courses = enter_course_numbers(courses, n)
            self.assertEqual(selected_courses, {"CS120"})

            schedule = generate_schedule(courses, selected_courses)
            display_schedule(schedule)

        # Check the printed output
        expected_output = "\nYour Schedule\nCourse: CS120 Section: 001 Days: MWF Time: 0900 - 0950"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["3", "CS120", "CS121", "CS222"])
    def test_multiple_course_scheduling(self, mock_input):
        file_path = "file.txt"

        # Redirect stdout to capture print statements
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            courses = read_course_data(file_path)
            display_courses(courses)

            n = number_of_courses()
            selected_courses = enter_course_numbers(courses, n)
            self.assertEqual(selected_courses, {"CS120", "CS121", "CS222"})

            schedule = generate_schedule(courses, selected_courses)
            display_schedule(schedule)

        # Check the printed output
        expected_output = "\nYour Schedule\nCourse: CS120 Section: 001 Days: MWF Time: 0900 - 0950\nCourse: CS121 Section: 001 Days: TR Time: 1230 - 1345\nCourse: CS222 Section: 005 Days: TR Time: 1100 - 1215"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["2", "CS120", "CS121"])
    def test_conflicting_course_scheduling(self, mock_input):
        file_path = "file.txt"

        # Redirect stdout to capture print statements
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            courses = read_course_data(file_path)
            display_courses(courses)

            n = number_of_courses()
            selected_courses = enter_course_numbers(courses, n)
            self.assertEqual(selected_courses, {"CS120", "CS121"})

            schedule = generate_schedule(courses, selected_courses)
            display_schedule(schedule)

        # Check the printed output
        expected_output = "Debugging: Time conflict for course"
        self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
