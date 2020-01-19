def is_palindrome(s):
	i = 0
	j = len(s) - 1

	while i < j and s[i] == s[j]:
		i += 1
		j -= 1
	return j <= i

print(is_palindrome("racecar"))
print(is_palindrome("plamen"))