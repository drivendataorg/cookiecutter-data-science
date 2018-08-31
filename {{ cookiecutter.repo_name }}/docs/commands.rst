Commands
========

The Makefile contains the central entry points for common tasks related to this project.

Syncing data to S3
^^^^^^^^^^^^^^^^^^

* `upload_data` uploads the contents of the `data` directory and its subdirectories to an external storage outside version control. The command is not configured initially and must be manually configured in the `Makefile`.  
* `download_data` downloads the contents of the `data` directory and its subdirectories to an external storage outside version control. The command is not configured initially and must be manually configured in the `Makefile`.  
