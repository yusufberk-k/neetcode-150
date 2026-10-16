# NeetCode 150

My solutions to the [NeetCode 150](https://neetcode.io/roadmap) list.

## Status tags

Every file starts with a status comment:

| Tag | Meaning |
|---|---|
| `solo` | Solved it myself |
| `hint` | Got stuck, took a hint, wrote the rest myself |
| `looked` | Read the solution |

Anything tagged `looked` or `hint` gets a retry date: 7 days after solving for
`hint`, 3 days for `looked`. On that date I rewrite it
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
| 2026-10-11 | 84. Largest Rectangle in Histogram | `hint` | [stack/largest-rectangle-in-histogram.py](stack/largest-rectangle-in-histogram.py) |
| 2026-10-11 | 424. Longest Repeating Character Replacement | `looked` | [sliding-window/longest-repeating-character-replacement.py](sliding-window/longest-repeating-character-replacement.py) |
| 2026-10-13 | 76. Minimum Window Substring | `looked` | [sliding-window/minimum-window-substring.py](sliding-window/minimum-window-substring.py) |
| 2026-10-14 | 239. Sliding Window Maximum | `looked` | [sliding-window/sliding-window-maximum.py](sliding-window/sliding-window-maximum.py) |
| 2026-10-17 | 567. Permutation in String | `hint` | [sliding-window/permutation-in-string.py](sliding-window/permutation-in-string.py) |
| 2026-10-18 | 875. Koko Eating Bananas | `looked` | [binary-search/koko-eating-bananas.py](binary-search/koko-eating-bananas.py) |
| 2026-10-21 | 74. Search a 2D Matrix | `hint` | [binary-search/search-a-2d-matrix.py](binary-search/search-a-2d-matrix.py) |