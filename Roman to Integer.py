def romanToInt(s: str) -> int:
	roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	s = s[::-1]
	prev_letter = s[0]
	ans = roman_dict[prev_letter]
	for curr_letter in s[1:]:
		if roman_dict[curr_letter] < roman_dict[prev_letter]:
			ans -= roman_dict[curr_letter]
		else:
			ans += roman_dict[curr_letter]
		prev_letter = curr_letter
	return ans

print(romanToInt("MCMXCIV"))