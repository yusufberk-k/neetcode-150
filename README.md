# NeetCode 150

My solutions to the [NeetCode 150](https://neetcode.io/roadmap) list.

## Status tags

Every file starts with a status comment:

| Tag | Meaning |
|---|---|
| `solo` | Solved it myself |
| `hint` | Got stuck, took a hint, wrote the rest myself |
| `looked` | Read the solution |

Anything tagged `looked` or `hint` gets a retry date. On that date I rewrite it
from scratch without opening the file. If it passes, the tag becomes
`solo` and the commit message says `retry passed`.

The tags exist so progress is measurable. A repo where everything looks
solved from day one measures nothing.

```python
# Encode and Decode Strings
# status: looked | retry: 2026-09-22
# note: did not know the length-prefix pattern
```

## Commit format

```
Add <LC number>. <Problem Name> (<approach>, <complexity>)
```

Examples:

```
Add 49. Group Anagrams (frequency map, O(nk))
Add 271. Encode and Decode Strings (length-prefix encoding, O(n))
Add 347. Top K Frequent Elements (max-heap O(n log n), bucket sort O(n))
```

## Pace

1 problem a day through the list, then 5 a week on review afterwards.

## Retry queue

Sorted by date. A row is removed when the retry passes and the tag becomes `solo`.

| Retry date | Problem | Status | File |
|---|---|---|---|
| 2026-10-07 | 11. Container With Most Water | `hint` | [two-pointers/container-with-most-water.py](two-pointers/container-with-most-water.py) |
| 2026-10-07 | 42. Trapping Rain Water | `hint` | [two-pointers/trapping-rain-water.py](two-pointers/trapping-rain-water.py) |
| 2026-10-08 | 155. Min Stack | `hint` | [stack/min-stack.py](stack/min-stack.py) |
| 2026-10-09 | 150. Evaluate Reverse Polish Notation | `hint` | [stack/evaluate-reverse-polish-notation.py](stack/evaluate-reverse-polish-notation.py) |
| 2026-10-09 | 238. Product of Array Except Self | `hint` | [arrays-hashing/products-of-array-except-self.py](arrays-hashing/products-of-array-except-self.py) |
| 2026-10-11 | 84. Largest Rectangle in Histogram | `hint` | [stack/largest-rectangle-in-histogram.py](stack/largest-rectangle-in-histogram.py) |