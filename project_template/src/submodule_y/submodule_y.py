from . import y_helper_a, y_helper_b

def main():
    print("This is submodule_y" )

def where():
    print("/project_template/src/submodule_y/submodule_y.py")

if __name__ == '__main__':
    print('Called by __main__')
    main()