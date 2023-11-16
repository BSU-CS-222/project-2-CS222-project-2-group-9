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

if __name__ == "__main__":
    unittest.main()
