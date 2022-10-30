from ..folderB.FileB import fileB_func

def fileA_func():
    print("This is a function called from fileA. It will not call a function from fileB")
    fileB_func
    return True


if __name__ == __main__:
    print("File A called directly")