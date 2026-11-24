# prog. for KeyError Exception
try:
    student={"rollno":202,
    "name":"naman",
    "age":21}
    print(student["city"])
except:
    print("key is not found.")
