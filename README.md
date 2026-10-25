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
`hint`, 3 days for `looked`. If a retry fails and I need help again, the
problem is re-tagged with whatever help I needed this time, and the retry
date becomes 14 days out. On that date I rewrite it
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
| 2026-10-14 | 239. Sliding Window Maximum | `looked` | [sliding-window/sliding-window-maximum.py](sliding-window/sliding-window-maximum.py) |
| 2026-10-17 | 567. Permutation in String | `hint` | [sliding-window/permutation-in-string.py](sliding-window/permutation-in-string.py) |
| 2026-10-18 | 875. Koko Eating Bananas | `looked` | [binary-search/koko-eating-bananas.py](binary-search/koko-eating-bananas.py) |
| 2026-10-21 | 74. Search a 2D Matrix | `hint` | [binary-search/search-a-2d-matrix.py](binary-search/search-a-2d-matrix.py) |
| 2026-10-21 | 153. Find Minimum in Rotated Sorted Array | `looked` | [binary-search/find-minimum-in-rotated-sorted-array.py](binary-search/find-minimum-in-rotated-sorted-array.py) |
| 2026-10-24 | 33. Search in Rotated Sorted Array | `looked` | [binary-search/search-in-rotated-sorted-array.py](binary-search/search-in-rotated-sorted-array.py) |
| 2026-10-28 | 981. Time Based Key-Value Store | `hint` | [binary-search/time-based-key-value-store.py](binary-search/time-based-key-value-store.py) |
| 2026-10-29 | 206. Reverse Linked List | `hint` | [linked-list/reverse-linked-list.py](linked-list/reverse-linked-list.py) |
| 2026-10-31 | 424. Longest Repeating Character Replacement | `hint` | [sliding-window/longest-repeating-character-replacement.py](sliding-window/longest-repeating-character-replacement.py) |
| 2026-10-31 | 21. Merge Two Sorted Lists | `hint` | [linked-list/merge-two-sorted-linked-lists.py](linked-list/merge-two-sorted-linked-lists.py) |
| 2026-11-01 | 141. Linked List Cycle | `hint` | [linked-list/linked-list-cycle-detection.py](linked-list/linked-list-cycle-detection.py) |
