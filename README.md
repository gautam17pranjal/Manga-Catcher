# Manga Catcher

This is a personal project. This was done so that Manga chapters can be taken offline anywhere to read.
##
#### Requirements:
 - You must have Python 3.x installed
 - The following modules are required:
	 - [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
	 - [requests](https://pypi.org/project/requests/)
	 - [os](https://docs.python.org/3/library/os.html)
	 - [shutil](https://docs.python.org/3/library/shutil.html)
	 - [img2pdf](https://pypi.org/project/img2pdf/)
##
#### How to Use it:
 - The user needs to enter the starting chapter number and the last chapter number he/she wants to download in the variables "start", "last". For a single chapter both variable values will be same.
 - The user also needs to enter the Manga URL in the variable "manga_url" under the function "catch_chapter".
##
#### After running:
- The chapters will be saved in the location where the source file is present, under the Manga named folder.
##
Hope you enjoy reading offline!
##
