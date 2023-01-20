from . import b_helper

def main():
    print("This is submodule_y's helper module b" )

def where():
    print("/project_template/src/submodule_y/y_helper_b.py")

if __name__ == '__main__':
    print('Called by __main__')
    main()