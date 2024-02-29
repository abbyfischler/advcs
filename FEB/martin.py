import csv
from collections import defaultdict, OrderedDict
from itertools import combinations, product

def generate_class_combinations(required, electives, grade):
    num_electives_required = 2 if grade in [9, 12] else 1

    expanded_required = [(f"{course}-1", f"{course}-2") for course in required]
    
    # Generate all possible combinations of the expanded required classes
    # This uses the product to consider all combinations of -1 and -2 versions
    all_possible_required_combinations = list(product(*expanded_required))
    
    # Now, filter these combinations to ensure we only take as many as needed
    if len(required) > (7 - num_electives_required):
        required_combinations = [comb for comb in all_possible_required_combinations if len(comb) == (7 - num_electives_required)]
    else:
        required_combinations = all_possible_required_combinations

    # Regenerate elective combinations for each student within the function
    elective_combinations = list(combinations(electives, num_electives_required))

    full_combinations = []
    for req_combo in required_combinations:
        for elec_combo in elective_combinations:
            # Combine the current required and elective combinations
            full_combination = list(req_combo) + list(elec_combo)
            full_combinations.append(full_combination)
    return full_combinations

def read_student_classes_sorted_by_grade(file_path):
    students_required_classes = defaultdict(set)
    students_elective_classes = defaultdict(set)
    student_grades = {}
#student
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_name = f"{row['Student First Name']} {row['Student Last name']}"
            student_grades[full_name] = int(row['Future Grade'])

            if row['Alternate 1 / Advanced'] or row['Alternate 2']:
                students_elective_classes[full_name].add(row['Course Name'])
                if row['Alternate 1 / Advanced']:
                    students_elective_classes[full_name].add(row['Alternate 1 / Advanced'])
                if row['Alternate 2']:
                    students_elective_classes[full_name].add(row['Alternate 2'])
            else:
                students_required_classes[full_name].add(row['Course Name'])

    # Prepare the data for combinations
    students_classes_combinations = {}
    for name, grade in student_grades.items():
        required = list(students_required_classes[name])
        electives = list(students_elective_classes[name])
        combinations = generate_class_combinations(required, electives, grade)
        students_classes_combinations[name] = {'Grade': grade, 'Combinations': combinations}

       
        print(f"Generated {len(combinations)} combinations for {name} (Grade {grade})")

    # Sort students by their grade
    sorted_students_classes_combinations = OrderedDict(sorted(students_classes_combinations.items(), key=lambda item: item[1]['Grade']))

    return sorted_students_classes_combinations


# Specify the path to your CSV file
file_path = 'student.csv'

# Call the function with your file path
sorted_student_classes_combinations = read_student_classes_sorted_by_grade(file_path)


for student, details in sorted_student_classes_combinations.items():
    print(f'{student} (Grade {details["Grade"]}):')
    for combo in details['Combinations']:
        print(combo)
    print() 