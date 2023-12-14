#Write a function that checks if a teacher can teach what class.

#The output needs to be a dictanory where the key is the class name and the value is the teachers that can teach it. 
def can_teach(teacher, class_name):
    # DANNY WILL THIS BE GIVEN: 
    can_teach_dict = {}

    #is class name local or regular
    for class_name in class_name:
        can_teach_list = []
        for teacher_name, teacher_classes in teacher.items():
            if class_name in teacher_classes:
                can_teach_list.append(teacher_name)
                can_teach_dict[class_name] = can_teach_list
    return can_teach_dict