#Read in the data
import csv
import os
filename = "Resources/budget_data.csv"
with open(filename, newline='') as csvfile:
	dataReader = csv.reader(csvfile, delimiter=',')
	#setting months to -1 to account for header row
	months = -1
	runningTotal = 0
	greatestGain = 0
	ggTime = ""
	greatestLoss = 0
	glTime = ""
	for row in dataReader:
		months = months + 1
		#commented out - can print the data as it is being read for debugging
		#print(", ".join(row))
		if(months > 0):
			change = int(row[1])
			runningTotal = runningTotal + change
			if(change > greatestGain):
				greatestGain = change
				ggTime = row[0]
			if(change < greatestLoss):
				greatestLoss = change
				glTime = row[0]
	averageChange = 0
	if(months > 0):
		averageChange = runningTotal/months
		
	#Export final data
	if not os.path.exists('analysis'):
		os.makedirs('analysis')
	export = open("analysis/results.txt", "w")
	export.write(f"We analyzed {months} months. \n")
	export.write(f"The total change in moneys over that time was {runningTotal} \n")
	export.write(f"That's an average amount of change of ${averageChange} per month. \n")
	export.write(f"We saw the greatest gainz at {ggTime}, comin' in at ${greatestGain}. \n")
	export.write(f"the greatest loss was in {glTime}, at ${greatestLoss}. \n")
	export.close 
	
