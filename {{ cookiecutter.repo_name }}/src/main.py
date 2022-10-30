from .folderA import fileA_func

def main():
    """
    Typical entrypoint to project or pipeline.
    If your pipeline really only has one way to be executed,
    it is a good idea to string together all the operations here 
    """
    fileA_func()
    return True

if __name__ == "__main__":
    main()