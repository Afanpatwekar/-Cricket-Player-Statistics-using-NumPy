# -Cricket-Player-Statistics-using-NumPy
📌 Project Overview

This project is a simple cricket statistics analysis program built using Python and NumPy.

It stores batting data of 11 cricket players in NumPy arrays and performs different statistical operations such as calculating strike rates, finding the highest scorer, total team runs, and identifying players based on their performance.

🎯 Features
Store player names and batting data using NumPy arrays.
Calculate each player's strike rate.
Display all player records.
Calculate:
Total team runs
Average runs
Highest score
Lowest score
Find the highest run scorer.
Display players who scored:
50 or more runs
0 runs (Duck)
Strike rate above 150
Calculate:
Total fours
Total sixes
Total boundaries
Display the top 3 individual scores.
📚 NumPy Functions Used
Function	Purpose
np.array()	Creates NumPy arrays
np.round()	Rounds strike rate to 2 decimal places
np.sum()	Calculates total runs, fours, and sixes
np.mean()	Calculates average runs
np.max()	Finds the highest score
np.min()	Finds the lowest score
np.argmax()	Finds the index of the highest scorer
np.sort()	Sorts runs to get the top 3 scores
📊 Formula Used

Strike Rate

Strike Rate = (Runs / Balls) * 100

Implemented as:

strike_rate = np.round((runs / balls) * 100, 2)
🛠 Technologies Used
Python 3
NumPy
▶️ How to Run
Install NumPy:
pip install numpy
Run the program:
python project.py
📂 Project Structure
Cricket-Statistics-NumPy/
│
├── project.py
├── README.md
📖 Learning Outcomes

After completing this project, you will understand:

NumPy arrays
Array indexing
Boolean indexing
Mathematical operations on arrays
Statistical functions in NumPy
Sorting arrays
Finding maximum and minimum values
Basic data analysis using Python
👨‍💻 Author

Afan Asif Patwekar

Learning Python and NumPy through practical projects.
