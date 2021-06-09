def proteins(strand):
	x = []
	l = list(strand)
	while len(l) > 0:
		y = ""
		for i in range(0,3):
			y = y + l.pop(0)
		if y == "AUG":
			x.append("Methionine")
		elif y == "UUU" or y == "UUC":
			x.append("Phenylalanine")
		elif y == "UUA" or y == "UUG":
			x.append("Leucine")
		elif y == "UCU" or y == "UCC" or y == "UCA" or y == "UCG":
			x.append("Serine")
		elif y == "UAU" or y == "UAC":
			x.append("Tyrosine")
		elif y == "UGU" or y == "UGC":
			x.append("Cysteine")
		elif y == "UGG":
			x.append("Tryptophan")
		else:
			break
	return x
		
			
			
