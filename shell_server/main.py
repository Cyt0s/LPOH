from bootstrapper import BootStrapper

def main():
    bootstrapper = BootStrapper({})
    bootstrapper.bootstrap()
    bootstrapper.shell_brain.start()
    


if __name__ == '__main__':
    main()