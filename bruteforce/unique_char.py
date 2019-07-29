
Create a function that returns only strings with unique characters.

filter_unique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
# "b" occurs in "abb" more than once, "b" occurs in "abcdb" more than once, etc.

filter_unique(["88", "999", "989", "9988", "9898"]) ➞ []

filter_unique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]) ➞ ["ABCDE", "BED", "BAC"]


def filter_unique(lst):
	unique = []
	for i in range(len(lst)):
		if len(set(lst[i])) == len(lst[i]):
			unique.append(lst[i])
	return unique
			
		
		
