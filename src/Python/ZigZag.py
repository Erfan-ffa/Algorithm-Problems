# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int):
    	if(numRows == 1):
    		return s

    	sentence = s
    	rows = numRows
    	columns = 100
    	matrix = [["" for i in range(columns)] for i in range(rows)]
    	wordIndex = 0
    	i = 0
    	j = 0
    	while wordIndex != len(sentence):
    		if i == rows - 1:
    			while i > 0:
    				if(wordIndex > len(sentence) - 1):
    					break

    				selectedWord = sentence[wordIndex]
    				wordIndex += 1
    				matrix[i][j] = selectedWord
    				i -= 1
    				j += 1
    		else:
    			selectedWord = sentence[wordIndex]
    			wordIndex += 1
    			matrix[i][j] = selectedWord
    			i +=1

    	print(matrix)
    	oneRowWords = ""
    	for i in range(numRows):
    		for j in range(columns):
    			oneRowWords += matrix[i][j]

    	return oneRowWords


x = Solution()
result = x.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 2)
print(result)