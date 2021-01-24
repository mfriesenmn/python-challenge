#Read in the data
import csv
import os
filename = "Resources/election_data.csv"
with open(filename, newline='') as csvfile:
	votes = csv.reader(csvfile, delimiter=',')
	#this solution uses a pair of lists, associated by order.
	#I would prefer a DTO so that they're more closely linked but I don't know how to make those in python, only in java
	candidates = []
	votesPerCandidate = []
	votersCount = 0
	
	#Main Loop Starts
	for row in votes:
		if(votersCount > 0):
			#cvf being a way to refer to the "Candidate being voted for" as a shorthand
			cvf = row[2]
			if(cvf in candidates):
				candidateIndex = candidates.index(cvf)
				votesPerCandidate[candidateIndex] = votesPerCandidate[candidateIndex]+1
			else:
				print(f"New candidate, {row[2]}, found")
				candidates.append(row[2])
				votesPerCandidate.append(1)
		votersCount = votersCount + 1
		
		#For debugging - these statements add a terminal message for each power of ten in number of votes counted
		# if(votersCount == 10):
			# print("Tenth voter processed")		
		# if(votersCount == 100):
			# print("hundredth voter processed")		
		# if(votersCount == 1000):
			# print("Tousandth voter processed")		
		# if(votersCount == 10000):
			# print("Ten Thousandth voter processed")		
		# if(votersCount == 100000):
			# print("Hundred Thousdandth voter processed")
		# if(votersCount == 1000000):
			# print("One Millionth voter processed")
		# if(votersCount == 10000000):
			# print("Ten Millionth voter processed")
		# if(votersCount == 100000000):
			# print("Hundred Millionth voter processed")
	#Main Loop Ends
	
	
	#To offset extra vote from the header row
	votersCount = votersCount - 1
	
	#Report:
	print(f"Total number of voters is {votersCount}")
	#Loop through candidates, using a counter to look up the number of votes associated with that candidate.
	candidateLoop = 0
	mostVotesIndex = 0
	currentMostVotes = 0
	for cand in candidates:
		percentWon = 100 * votesPerCandidate[candidateLoop]/votersCount
		print(f"{cand} received {votesPerCandidate[candidateLoop]} votes - %{round(percentWon,3)} of total ")
		if(votesPerCandidate[candidateLoop] > currentMostVotes):
			currentMostVotes = votesPerCandidate[candidateLoop]
			mostVotesIndex = candidateLoop
		candidateLoop = candidateLoop + 1
	print(f"The winner is {candidates[mostVotesIndex]} with {votesPerCandidate[mostVotesIndex]} votes!")
	
	#Export:
	#yeah, I know this is all basically the previous section, but with a few minor modifications.
	if not os.path.exists('analysis'):
		os.makedirs('analysis')
	export = open("analysis/election_results.txt", "w")
	export.write("Election results: \n")
	export.write("----------------- \n")
	export.write(f"Total votes: {votersCount} \n")
	candidateLoop = 0
	for cand in candidates:
		percentWon = 100 * votesPerCandidate[candidateLoop]/votersCount
		export.write(f"{cand} received {votesPerCandidate[candidateLoop]} votes, %{round(percentWon,3)} of total.\n")
		candidateLoop = candidateLoop + 1
	export.write("----------------- \n")
	#export.write(f"The winner is: JOE BIDEN!")
	export.write(f"The winner is: {candidates[mostVotesIndex]}")
	export.close

#End