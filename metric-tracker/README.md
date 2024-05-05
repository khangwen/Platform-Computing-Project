# Getting Started with This Python Virtual Environment
See the following link for extended instructions on setting up the virtual environment:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Instructions below are for Windows operating systems. See above link for MacOS/Linux.
Begin by running the following in the metric-tracker directory:
```
python -m venv venv
```
Then start up the virtual environment:
```
venv\Scripts\activate
```
Once the virtual environment is setup, install dependencies:
```
py -m pip install -r requirements.txt
```
Be sure to update the requirements.txt file if you change any dependencies:
```
py -m pip freeze --all r > requirements.txt
```