# prog. for module not found
try:
    import math1
    print(math1.pow(2,3))
except ModuleNotFoundError:
    print("Module not available.")
