# Encode and Decode Strings

## 🔍 Problem Summary

We need a way to convert a list of strings into a single string (encode) and then reconstruct the original list (decode).  
The challenge is that strings may contain **any ASCII characters**, including `#`, spaces, digits, or even be empty — so we cannot rely on simple delimiters like splitting on `#`.

---

## 🧠 Key Insight

The key idea is to **prefix each string with its length**, followed by a separator.  
This guarantees that during decoding, we always know _exactly_ how many characters to read, regardless of what the string contains.

In other words:

> **Use length-prefix encoding → avoids delimiter ambiguity.**

---

## 🧩 Approaches Considered

### 1. Brute Force (Delimiter-Based)

- Join strings using a special character (e.g., `"|"` or `"#"`), then split on that character.
- **Why it fails:** Any string may contain the delimiter, making decoding ambiguous or impossible.
- **Time:** O(n)
- **Why it’s not ideal:** Cannot reliably handle arbitrary strings.

---

### 2. Optimal Approach (Length-Prefix Encoding)

- For each string, encode as:  
  `"<length>#<string>"`
- During decoding:
  - Read characters until `#` → this gives the length.
  - Read exactly that many characters → this gives the string.
- **Why it works:** Never depends on delimiters inside the string; length tells us exactly where each string ends.
- **Time:** O(n) for both encode and decode
- **Why it’s better:** Works for all edge cases — empty strings, unicode, special characters, repeated delimiters, etc.

---

## 🧪 Final Code (Python)

```python
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
```
