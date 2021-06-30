class Solution:
    def romanToInt(self, s: str) -> int:
        val_map = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        total = 0

        for i in range(len(s)):
            curr_sym, next_sym = s[i], s[i+1:i+2]

            # We need to make sure that next_sym exists, since we are using slicing it could return
            # an empty value, and that'll throw a KeyError if not handled:
            if next_sym and val_map[curr_sym] < val_map[next_sym]:
                total -= val_map[curr_sym]
            else:
                total += val_map[curr_sym]

        return total
