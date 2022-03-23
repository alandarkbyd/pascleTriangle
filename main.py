
arr1 = [1]
arr2 = [1,1]

stepOne = int(input("Tell me the length of the pascle triangle: "))
yon = input('Do you want to get a specific line from the pascle triangle?(y/n): ')
if yon == 'y':
	line = int(input("Tell me the line number: "))
else:
	line = 0
newarr = []
steps = 0
spaces = stepOne

class PacleTriangle:
	line = []
	def themainTriangle(self,stepOne):
		# global newarr, steps, spaces
		arr1 = [1]
		arr2 = [1,1]
		newarr = []
		spaces = stepOne
		if stepOne == 1:
			print(1)
		elif stepOne < 0:
			print('None')
		elif stepOne == 0:
			print()
		else:
			print(" "*(spaces-2),1)
			print(" "*(spaces-3),1,1)
			for i in range(stepOne-2):
				for j in range(len(arr2)-1):
					newarr.append(arr2[j] + arr2[j+1])
				newarr.insert(0, 1)
				newarr.insert(len(arr2), 1) # newarr.append(1)
				arr2.clear()
				arr2.extend(newarr)
				print(" "*(spaces-3), end='')
				for k in newarr:
					print(k, end=' ')
				print()
				newarr.clear()
				spaces -= 1


	def getTheLine(self, line):
		# global newarr, steps, spaces, arr2
		if line == 1:
			print(f'The {line}th line is: {1}')
		arr1 = [1]
		arr2 = [1,1]
		newarr = []
		steps = 0
		stepOne = line+1
		spaces = stepOne
		trackline = []
		for i in range(stepOne-2):
			steps += 1
			for j in range(len(arr2)-1):
				newarr.append(arr2[j] + arr2[j+1])
			newarr.insert(0, 1)
			newarr.insert(len(arr2), 1) # newarr.append(1)
			arr2.clear()
			arr2.extend(newarr)
			trackline.extend(newarr)
			newarr.clear()
			if steps == line-2:
				return trackline
				print(f'The {line}th line is: {trackline}')
			elif line == 2:
				print(f'The {line}th line is: {str("1 1")}')
			spaces -= 1	
			trackline.clear()	






triangle = PacleTriangle()
triangle.themainTriangle(stepOne)
if line > 0:
	tgtl = triangle.getTheLine(line)
	print(f'The {line}th line is: {tgtl}')
	adding = []
	print(1, end=' + ')
	for h in range(1,len(tgtl)):
		adding.append(f"{tgtl[h]}y")
	print(' + '.join(adding))
# equation = (1 + y)^6, where 6 is the power


