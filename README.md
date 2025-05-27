# 🔰 Day 44 – GFG 160 Days DSA Challenge
## Problem: Find Triplets with Zero Sum (Using Indexes)
### Language: Python
### Date: 26 May 2025
### Tag: #Day44 #gfg160 #geekstreak2025

## ✅ Problem Statement:
Given an array of integers, return all index triplets (i, j, k) such that:

- arr[i] + arr[j] + arr[k] == 0
Ensure each triplet is unique and based on indexes, not values.

## 💡 Approach:
- Iterate the array with index i (outer loop)

- Use a hash map (seen) to store previously seen values with their indexes

- For every j > i, compute the third element as:
complement = -(arr[i] + arr[j])
- If complement exists in seen, append the triplet (i, seen[complement], j)

- Add current element arr[j] to the seen dictionary

This avoids sorting and keeps track of actual indices.


## ⏱️ Time & Space Complexity:
- Time: O(n²)

- Space: O(n) per outer loop due to the hash map

## 🔖 Hashtags:
#gfg160 #geekstreak2025 #Day44
#tripletsum #twopointer #hashing #python
#framesbyvikash #dsa #leetcodeprep

