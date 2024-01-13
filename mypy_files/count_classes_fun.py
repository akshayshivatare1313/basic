import ast

def count_and_print_classes(file_path):
    with open('C:/Users/Akshay/Desktop/B05_Ferilion_Pyth0n/mypy_files/Class_practice/class_10.py', 'r') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    class_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

    print(f"Number of classes in '{file_path}': {len(class_names)}")
    print("Class Names:")
    for class_name in class_names:
        print(f"- {class_name}")

    return len(class_names)

file_path = r'C:\Users\Akshay\Desktop\B05_Ferilion_Pyth0n\mypy_files\Class_practice\class_10.py'
class_count = count_and_print_classes(file_path)

print(f"\nTotal number of classes: {class_count}")

