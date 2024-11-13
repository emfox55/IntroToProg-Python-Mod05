# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   EFox,11/13/24,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict[str,str] = [] # one row of student data
students: list[dict[str,str]] = []  # a table of student data

# When the program starts:
# Read the file data into a list of dictionary rows, with structured error handling.
try:
    file = open(FILE_NAME,'r')
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print('Text file must exist before running this script!')
    print('-- Technical Error Message --')
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print('There was a non-specific error!')
    print('-- Technical Error Message -- ')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input('What would you like to do: ')
    print('\n')

    # Input user data, with structured error handling for first and last name entry.
    if menu_choice == '1':
        try:
            student_first_name = input('Please enter the student\'s first name: ')
            if not student_first_name.isalpha():
                raise ValueError('Invalid entry: the first name cannot contain numbers.')
            student_last_name = input('Please enter the student\'s last name: ')
            if not student_last_name.isalpha():
                raise ValueError('Invalid entry: the last name cannot contain numbers.')
            course_name = input('Please enter the name of the course: ')
            student_data = {'FirstName':student_first_name,
                            'LastName':student_last_name,
                            'CourseName':course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print('------Technical Error Message-------')
            print(e.__doc__)
        except Exception as e:
            print('------Non-Specific Error--------')
            print('------Technical Error Message-------')
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == '2':
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.\n')
        print("-"*50)
        continue

    # Save the data to a file, with structured error handling
    elif menu_choice == '3':
        try:
            file = open(FILE_NAME,'w')
            json.dump(students,file)
            file.close()
        except TypeError as e:
            print('Are the file contents in a valid JSON format?')
            print('------Technical Error Message-------')
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('------Non-Specific Error--------')
            print('------Technical Error Message-------')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

        print('The following data was saved to file!')
        for student in students:
            print(f'Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.')
        continue

    # End program
    elif menu_choice == '4':
        break
    else:
        print('Invalid entry, please enter a valid menu option')

print('Program Ended')
