class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])   
            j += 1                 

            res.append(s[j : j + length])

            i = j + length

        return res


sol = Solution()

tests = [
    ["Hello", "World"],
    [""],
    ["", ""],
    ["#", "##", "###"],
    ["123", "4567", "89"],
    ["a#b#c", "###", "##a##"],
    ["", "#", "##", "###", "####"],
    ["hello world", "foo", "bar"],
    ["😀😃😄😁", "emoji test"],  # unicode
    ["a" * 50, "b" * 100, "c" * 150],  # long strings
    ["", " ", "   ", "      "],  # whitespace
    ["|", "||", "|||", "|#|#|"],  # delimiter-like characters
    ["0#0#0", "1#1#1", "2#2#2"],  # strings containing digits + '#'
]

for idx, case in enumerate(tests):
    encoded = sol.encode(case)
    decoded = sol.decode(encoded)
    print(f"Test {idx+1}: {'PASS' if decoded == case else 'FAIL'}")
    print("Original:", case)
    print("Encoded :", encoded)
    print("Decoded :", decoded)
    print("-" * 40)


        
        
        