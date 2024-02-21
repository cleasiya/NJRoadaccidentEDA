"""
########
Capture stats and output data to a text file
########
"""

import os


class DocWriter:
    """Contains attributes and methods related to generate output file"""
    def __init__(self, file_name):
        self.title = "Traffic Violation Data Analysis"
        self.file_name = file_name
        self.__file_path = os.path.join(os.getcwd(), file_name)
        self.__clear_contents()
        self.__write_project_headers()

    def __clear_contents(self):
        """ Clear contents of file to avoid duplicate entries"""
        try:
            with open(self.__file_path, 'w') as doc_file:
                doc_file.truncate()
        except Exception as e:
            print("Error while cleaning contents from file : {}".format(e))

    def append_content(self, content):
        """ Append content to file"""
        try:
            with open(self.__file_path, 'a') as doc_file:
                doc_file.write(content)
        except Exception as e:
            print("Error while adding contents to file : {}".format(e))

    def add_content(self, content):
        """ Create file and add content to file"""
        try:
            with open(self.__file_path, 'w') as doc_file:
                doc_file.write(content)
        except Exception as e:
            print("Error while writing output to a file : {}".format(e))

    def __write_project_headers(self):
        """Prepare the document with title"""
        self.add_content(self.title + "\n\n")

    def __str__(self):
        return "Store contents to text file"
