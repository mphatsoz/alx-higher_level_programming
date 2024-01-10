import marshal
import types

def print_module_names():
    with open("hidden_4.pyc", "rb") as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code_object = marshal.load(file)

        if code_object.co_flags & 0x08:  # Check if it's a module
            module = types.ModuleType("hidden_4")
            exec(code_object, module.__dict__)
            
            names = [name for name in dir(module) if not name.startswith('__')]
            names.sort()

            for name in names:
                print(name)

if __name__ == "__main__":
    print_module_names()
