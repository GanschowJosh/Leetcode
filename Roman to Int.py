class Solution:
    def romanToInt(self, s):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for i in range(len(s) - 1, -1, -1):
            current_value = roman_to_int[s[i]]
            if prev_value > current_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total