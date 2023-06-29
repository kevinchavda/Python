#Python function that checks whether a passed string is palindrome or not

"""
A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('madam')) 
