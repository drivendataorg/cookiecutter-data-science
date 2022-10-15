```python
import os
import shutil

   # Get the list of all files and directories
    dir_notes = "notebooks"
    files = os.listdir(dir_notes)
    files = [f for f in files if os.path.isfile(dir_notes+'/'+f)] #Filtering only the files.
    files.pop(0)
    # print(files)
    for item in files:
        shutil.copy(item, "reports")

```

# Welcome to your Jupyter Book

This is a small sample book to give you a feel for how book content is
structured.
It shows off a few of the major file types, as well as some sample content.
It does not go in-depth into any particular topic - check out [the Jupyter Book documentation](https://jupyterbook.org) for more information.

Check out the content pages bundled with this sample book to see more.

```{tableofcontents} 
```
