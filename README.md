# Cell Counter
**By Zoë McGinnis**

## Setup
First, please install python3. You can find instructions to do so for your specific OS [here](https://www.python.org/downloads/). 
### Jupyter Notebook (Recommended)
If you are planning to use only the jupyter notebook version of the cell counter, run `pip3 install jupyter notebook`. 
### Python Executable
If you are planning to use the regular python version of the code, run the following command from your terminal to install the required libraries: `pip3 install -r requirements.txt`.

## Running the Code
First, navigate to this folder, `bsc`, using the terminal. If it's in your home directory, you can just run `cd bsc`. Next, move the image you want to use into the folder called `originals`. **Make sure to crop you image manually before using the code.**
### Jupyter Notebook (Recommended)
To run the jupyter notebook version of the code, enter the following into your terminal: `jupyter notebook`. This should open a firefox window. Navigate to the window and click on `cell_counter.ipynb`. You should be able to follow the instructions in the file to run the code blocks there.
### Python Executable
Open cell_counter.py in a text editor or IDE and change `filename` to the name of the image you want to use. Save and run the following from your terminal: `python3 cell_counter.py`.