import numpy as np
#---------
# player Name
#---------
players=np.array(["Rohit","Gill","Virat","Rahul","Hardik","Jadeja","Surya","Axar","kuldep","Bumrah","siraj"])
# ----------------------
# Batting Data
# --------------------
runs = np.array([45, 82, 67, 15, 34, 28, 91, 10, 5, 2, 0])
balls = np.array([32, 55, 49, 20, 18, 22, 43, 12, 8, 5, 1])
fours = np.array([5, 10, 6, 2, 3, 2, 8, 1, 0, 0, 0])
sixes = np.array([2, 3, 2, 0, 2, 1, 5, 0, 0, 0, 0])
#--------------
# Claculate strike rate
#-----------------
#-------------------
#
strike_rate=np.round((runs/balls)*100,2)
#-----------------------
#disply palyer record
#----------------------
print("players=",players)
print("Runs=",runs)
print("Balls=",balls)
print("Strike_rate=",strike_rate)
#---------------------------
#Team, statistics
#-----------------
print("\n--------Team, statistics--------------")
# total runs
print("Total Runs=",np.sum(runs))
#avreage rins
print("Average Runs=",np.mean(runs))
#Highest score
print("Max Runs=",np.max(runs))
#lowest score
print("Min Runs=",np.min(runs))
#-----------
#Best batman
#-----------
print("\n Highest scorer=",players[np.argmax(runs)])
#---------
#50 + run
#---------
print("\n 50 + runs players name:")
print(players[runs>=50])
#---------
#0 run
#---------
print("\n 0  runs players name:")
print(players[runs==0])
#------
# strick rate about 150 playes
#-----------
print("\nstrick rate about 150 playes=")
print(players[strike_rate>150])
#--------
# total four
#---------
print("\n total four")
print("total four=",np.sum(fours))
#--------
# total six
#---------
print("\n total six")
print("total sixes=",np.sum(sixes))
#--------
# total boundaries
#---------
print("\n total boundaries")
print("total boundaries=",np.sum(sixes)+np.sum(fours))
#--------
# top 3 scores
#---------
print("\n top 3 scores")
print("top 3 scores=",np.sort(runs)[-3:])



