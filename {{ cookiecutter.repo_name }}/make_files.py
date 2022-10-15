import os

file_path_notes = r'_toc.yml'
if os.path.exists(file_path_notes):
    print('file already exists')
else:

    # Get the list of all files and directories
    dir_notes = "notebooks"
    files = os.listdir(dir_notes)
    files = [f for f in files if os.path.isfile(dir_notes+'/'+f)] #Filtering only the files.
    # files.pop(0)
    # print(files)
    
    # create a file
    with open(file_path_notes, 'w') as fp:
        # uncomment if you want empty file
        fp.write(
            '# Table of contents\n\t'
            '# Learn more at https://jupyterbook.org/customize/toc.html\n\n'
            'format: jb-book\n'
            'root: intro\n'
            'chapters:\n'
        )    

        for file in files:
            fp.write('- file: ' + dir_notes + '/' + file + '\n')    

#if reference file exists
file_path_ref = r'_config.yml'
if os.path.exists(file_path_ref):
    print('file already exists')
else:
    
    # Get the list of all files and directories
    dir_ref = "references"

    file_ref = os.listdir(dir_ref)
    if '.gitkeep' in file_ref:
        file_ref.pop()

    # files = [f for f in files if os.path.isfile(dir_ref+'/'+f)] #Filtering only the files.
    # print(file_ref)
    
    # create a file
    with open(file_path_ref, 'w') as fp_ref:
        # uncomment if you want empty file
        fp_ref.write(
            '# Book settings\n'
            '# Learn more at https://jupyterbook.org/customize/config.html\n\n'

            '# for html\n'
            'title: ' + {{cookiecutter.project_name}} + '\n'
            'logo: ' + dir_notes + '/figures/logo_png.png\n\n'

            '# for pdf/latex\n'
            'project: ' + {{cookiecutter.project_name}} + '\n'
            'author: ' + {{cookiecutter.author_name}} + '\n'
            'sphinx:\n'
            '   config:\n'
            '       latex_logo: \'' + dir_notes + '/figures/logo_jpg2300.jpg\'\n\n'

            '# Force re-execution of notebooks on each build.\n'
            '# See https://jupyterbook.org/content/execute.html\n'
            'execute:\n'
            '   execute_notebooks: force\n\n'

            '# Define the name of the latex output file for PDF builds\n'
            'latex:\n'
            '   latex_documents:\n'
            '       targetname: book.tex\n\n'

            '# Add a bibtex file so that we can create citations\n'
            'bibtex_bibfiles:\n'
            '- ' + dir_ref + '/' + file_ref[0] + '\n\n'

            '# Information about where the book exists on the web\n'
            'repository:\n'
            'url: https://github.com/executablebooks/jupyter-book  # Online location of your book\n'
            '#path_to_book: notebooks  # Optional path to your book, relative to the repository root\n'
            'branch: master  # Which branch of the repository should be used when creating links (optional)\n\n'

            '# Add GitHub buttons to your book\n'
            '# See https://jupyterbook.org/customize/config.html#add-a-link-to-your-repository\n'
            'html:\n'
            '   use_issues_button: true\n'
            '   use_repository_button: true'
        )    
  



        

