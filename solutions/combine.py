import sys

def combine(f1, fsc1, f2, fsc2, fout, fscout):
	s1 = open(f1, "r")
	sc1 = open(fsc1, "r")
	s2 = open(f2, "r")
	sc2 = open(fsc2, "r")
	out = open(fout, "w")
	osc = open(fscout, "w")
	for i in range(600):
		score1 = int(sc1.readline().strip())
		sol1 = s1.readline()
		score2 = int(sc2.readline().strip())
		sol2 = s2.readline()
		if score1 > score2:
			osc.write(str(score1) + '\n')
			out.write(sol1)
		else:
			osc.write(str(score2) + '\n')
			out.write(sol2)

path1 = sys.argv[1]
path2 = sys.argv[2]
outpath = sys.argv[3]

combine(path1 + '.out', path1 + 'Scores.txt', path2 + '.out', path2 + 'Scores.txt', outpath + '.out', outpath + 'Scores.txt')