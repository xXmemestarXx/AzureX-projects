This project is an extension of the CSP solver for a sudoku i made. 
It uses a ML approach borrowed from https://github.com/rg1990/cv-sudoku-solver.
It uses Keras and OpenCV in combination with my CSP solver to extract the sudoku from a given image. The model has been trained on the data found in the data folder, and the model used for the extraction can be found in the models folder. 

To train your own model just install the requirments and run the train.py script.
After doing this the model is found in the models folder and can be used in the soduku_main.py to extract and solve the suduko.



