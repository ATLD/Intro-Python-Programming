# Intro to Python Programming Setup Guide
Once you complete the instructions on this page, navigae to the Week 1 directory to complete your first assignment. This document contains instructions that cover... 

1. Installation and basics of git/github
1. Installation of Anaconda
1. Sourcing all material for course
1. Completing assignments

# Course Assumptions
There is no pre-requisite knowledge assumed for this course other than your desire to learn how to program using Python. 

# Learning Model
This course utilizes a flipped classroom model where students do the assigned readings and problems sets at home and come to class to get help and work with other students.

# Class Material
This class uses 4 different sources to teach the material. You are expected to complete all the readings, video lectures and problem sets from the following:
1. This Github Repository
1. Coursera Learn to Program Online Class
1. Think Python 2nd Edition by Allen Downey
1. Corey Schafer YouTube videos

# Getting Class Material
1. Register for [Learn to Program](https://www.coursera.org/learn/learn-to-program) by signing up for a Coursera account and choosing to audit the class. You can pay for a certificate or learn for free.
1. Download a copy of the book [Think Python 2nd Edition](http://greenteapress.com/wp/think-python-2e/)
1. Bookmark [Corey Schafer's YouTube channel](https://www.youtube.com/user/schafer5)

# Installing Anaconda
We will be using the excellent and free Anaconda Python distribution to install Python, Jupyter notebooks and a host of other useful third party packages (mainly for scientific computing). Python has been undergoing an agonizingly slow change from version 2 to 3 though Python 3 came out in 2008. Currently, nearly all major libraries have Python 3 support so please [download Anaconda for python 3.X](https://www.continuum.io/downloads). Use command `conda install <packagename>` to get new packages and `conda update --all` to update all packages. There is of course plenty more you can do [with conda](http://conda.pydata.org/docs/using/using.html) including setting up different environments for python 2 and 3 separately.

# Install a Text Editor
Some of the assignments will require a text editor. Sublime, Atom and Notepad++ are good choices.

# Git
Since you have access to this repository you have already successfully created a github account. To get the most out of this course you will need to locally install [git](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics), a very popular open-source version control system that takes snapshots in time of what your current project looks like. Git itself can be very complex and there are many books written on just how to use git but we don't need anything except the very basics for our purposes. 

## Git vs Github 
Github is a private company that hosts your git repositories online for others to view and collaborate with. Git is your local version control system that keeps track of all local file changes. In this course you will be using github to bring our online repositories to your local machines where you will make changes(i.e. complete the assignments) and push those changes back to us where we will be able view and comment on your assignments.  

### Let's get started with git!
1. [Download git.](https://git-scm.com/download) I believe both mac and linux machines should have git pre-installed.
1. If you've never set-up git before, you need to set your username and email. [Go here](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#Your-Identity) and follow the short instructions.
1. Fork this repository by going to the top right corner of this page and clicking fork.
1. Clone this repository to your local computer. Above the file listings towards the top of this page you will see a green button with the words 'clone or download' in it. Click that button and click the small clipboard icon with the url of this repo with .git appended to it. This will copy the url.
1. Open a terminal and `cd` into a directory that you'd like to save all your work for this class. Perhaps call it `Dunder Data Python Class`
1. Once in that directory, type in `git clone https://github.com/<your username>/Intro-Python-Programming.git`. Use your copied url here. This will pull all the files down into your local file system. You now have an exact replica of what you are reading here on github.

### Submitting your first assignment on github

1. As you are making changes to your files locally, it is a good idea to be continually committing your changes and pushing them to github.
1. Run `git add <filename>.<extension>` to tell git this is the file you would like to be committing
1. If you have edited multiple files of the same type (like Jupyter notebooks) you can simply write `git add *.ipynb` to add all the Jupyter notebooks to the index (index is a term for the staging area - the area right before you commit and take the snapshot)
1. Run `git commit -m "I have finished the section on lists"` to commit your file locally and 'take a snapshot'. Always add messages to your commits with `-m "<your message here>"`
1. Run `git push origin master` to push your changes to your remote repository on github. Check github to make sure the remote files were changed
1. repeat steps 3-6 several times during an assignment to ensure you don't lose your changes

# Completing Assignments
Each week's assignments are contained in this repo in its respective directory. Read the instructions in each week's README.md file to complete the assignments.

# Go to Week 1 and finish the assignment

## Resources
https://github.com/tdpetrou/Intro-Python-Programming/resources.md
