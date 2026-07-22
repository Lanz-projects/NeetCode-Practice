# Valid Sudoku

## 🔍 Problem Summary

We need to determine whether a partially filled **9×9 Sudoku board** is valid.  
A board is valid if all **filled** cells obey the rules:

- Each **row** contains digits 1–9 with no duplicates.
- Each **column** contains digits 1–9 with no duplicates.
- Each **3×3 sub-box** contains digits 1–9 with no duplicates.

Notes:

- Empty cells are represented by `"."` and should be ignored.
- A board can be valid even if it is not solvable.

---

## 🧠 Key Insight

The key idea is to track whether each digit has already appeared in its **row**, **column**, or **3×3 box**.  
To do this efficiently, we use **sets** for constant‑time membership checks:

- `rows[r]` tracks digits seen in row `r`
- `cols[c]` tracks digits seen in column `c`
- `boxes[(r//3, c//3)]` tracks digits in each 3×3 sub-box

If a digit appears twice in any of these three structures, the board is invalid.

---

## 🧩 Approaches Considered

### 1. Brute Force

- For each filled cell, scan its entire row, column, and 3×3 box to check for duplicates.
- This leads to repeated scanning and unnecessary work.
- **Time:** O(9³) = O(729) per cell → inefficient and messy.
- **Why it’s not ideal:** Too many repeated checks; not scalable or clean.

---

### 2. Better Approach (Hash Sets for Rows, Columns, Boxes)

- Maintain three hash structures:
  - `rows[r]` → digits in row `r`
  - `cols[c]` → digits in column `c`
  - `boxes[(r//3, c//3)]` → digits in the 3×3 box
- For each filled cell:
  - If the digit already exists in its row, column, or box → invalid.
  - Otherwise, add it to all three sets.
- **Time:** O(81) = O(1)
- **Why it’s better:** Single pass, constant-time checks, clean logic.

---

## 🧪 Final Code (Python)

```python
from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # key: (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                # Check row, column, and box
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[(r//3, c//3)]):
                    return False

                # Add value to tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)

        return True
```
