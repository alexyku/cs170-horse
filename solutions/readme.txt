The input path is '../cs170_final_inputs/'

Output files should be saved in 'solutions/'
Outputs are saved as two files:
	* '<Name>.out' is the file with the actual solutions. It should pass 'java outputvalidator <Name>'
	*'<Name>Scores.txt' is a file containing the score values of each solution. It should be formatted so line i contains the solution to i.in

This directory contains a number of useful python programs:

makesolutions.py, which produces a solution set. It requires python3, Anaconda, and the NetworkX graphing package. It should be called with two or three arguments:
	'python makesolutions.py <input path> <output path> <Timeout>'
For example:
	'python makesolutions.py ../cs170_final_inputs/ Solutions/T20 20'
The timeout can be used to control how long the algorithm spends on each input, so the runtime can be bounded above by Timeout * 600 seconds (but in practice is closer to a third of that). 

compare.py, which takes two arguments:
	'python compare.py <path1> <path2>'
For example:
	'python compare.py solutions/T20 solutions/T5'
And compares two outputs.

combine.py, which takes three arguments:
	'python combine.py <Old path 1> <Old path 2> <New path>'
For example:
	'python combine.py solutions/Better solutions/T20 solutions/Best'
and combines the best entries in each of the two old paths, putting the better of each in the new path.