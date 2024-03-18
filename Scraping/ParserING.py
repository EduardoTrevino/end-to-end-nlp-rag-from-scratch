import re

pattern = re.compile(
    r"\[\s*(?P<Course>\d+)\s*\|\s*"
    r"(?P<Course_Title>.+?)\s*\|\s*"
    r"(?P<Units>\d+)\s*\|\s*"
    r"(?P<Sec>[^|]+?)\s*\|\s*"  
    r"(?P<Days>TBA|[^|]+?)\s*\|\s*"  
    r"(?P<Begin>TBA|\d{2}:\d{2}[AP]M)\s*\|\s*"  
    r"(?P<End>TBA|\d{2}:\d{2}[AP]M)\s*\|\s*"  
    r"(?P<Location>.+?)\s*\|\s*"
    r"(?P<BLDG_Room>[^|]+?)\s*\|\s*" 
    r"(?P<Delivery_Mode>[^|]+?)\s*\|\s*" 
    r"(?P<Instructor>[^\]]+?)\s*\]",
    re.DOTALL  
)

def extract_course_info(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    courses = []
    for match in pattern.finditer(content):
        course_info = {key: value.strip() for key, value in match.groupdict().items()}
        courses.append(course_info)

    return courses

def save_course_info(courses, output_file_path):
    with open(output_file_path, 'w') as file:
        for course in courses:
            file.write('\n'.join(f"{key}: {value}" for key, value in course.items()))
            file.write('\n\n')


input_file_path = 'course_data.txt'  
output_file_path = 'parsed_course_info.txt'  
course_data = extract_course_info(input_file_path)
save_course_info(course_data, output_file_path)

#Citation: Assisted script with gpt4 modified it thought to make it work more efficenitly 