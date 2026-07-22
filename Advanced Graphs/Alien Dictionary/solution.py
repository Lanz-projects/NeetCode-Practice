class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)


def is_valid_order(words, order):
    # Invalid dictionary check
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if len(w1) > len(w2) and w1.startswith(w2):
            return order == ""

    if order == "":
        return False

    # All unique letters must appear exactly once
    letters = set()
    for word in words:
        letters.update(word)

    if set(order) != letters:
        return False

    if len(order) != len(letters):
        return False

    pos = {c: i for i, c in enumerate(order)}

    # Check every precedence constraint
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        for a, b in zip(w1, w2):
            if a != b:
                if pos[a] > pos[b]:
                    return False
                break

    return True


tests = [
    ["wrt", "wrf", "er", "ett", "rftt"],
    ["z", "x"],
    ["z", "o"],
    ["abc", "ab"],               # invalid prefix
    ["ab", "adc"],
    ["x"],
    ["a", "b", "c"],
    ["baa", "abcd", "abca", "cab", "cad"],
    ["za", "zb", "ca", "cb"],
    ["abc", "abc"],              # identical words
]


sol = Solution()

passed = 0

for i, words in enumerate(tests, 1):
    ans = sol.foreignDictionary(words)
    ok = is_valid_order(words, ans)

    if ok:
        print("Test {}: PASS".format(i))
    else:
        print("Test {}: FAIL".format(i))
        print("  words =", words)
        print("  output =", repr(ans))

    passed += ok

print("\nPassed {}/{} tests".format(passed, len(tests)))