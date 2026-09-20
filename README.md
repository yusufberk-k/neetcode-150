# NeetCode 150

My solutions to the [NeetCode 150](https://neetcode.io/roadmap) list.

## Language

C++ for the early problems, Python from #271 onward. C++ turned each
solution into buffer and type handling instead of the algorithm, and
Python is the main language in cloud security and DevSecOps anyway,
which is the track I am on.

## Status tags

Every file starts with a status comment:

| Tag | Meaning |
|---|---|
| `solo` | Solved it myself |
| `hint` | Got stuck, took a hint, wrote the rest myself |
| `looked` | Read the solution |

Anything tagged `looked` gets a retry date. On that date I rewrite it
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

6 problems a week through the list, then 4 a week on review afterwards.