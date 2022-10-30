from ..ingestion.fileB import fileB_func

def fileA_func():
    print("This is a function called from fileA.")
    print("It will now call a function from fileB")
    fileB_func()
    return True


if __name__ == "__main__":
    print("File A called directly")