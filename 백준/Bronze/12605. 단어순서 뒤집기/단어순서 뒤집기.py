# https://www.acmicpc.net/problem/12605
# 스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집기
import sys


input = sys.stdin.readline

n = int(input())
for i in range(n):
    words = input().split()
    print(f"Case #{i + 1}: {' '.join(words[::-1])}")