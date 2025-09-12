#!/usr/bin/python3
def best_score(a):
    return max(a.keys(), key=lambda x: a[x]) if a else None
