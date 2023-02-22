# https://contest.yandex.ru/contest/23389/problems/D/

from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    temperatures.append(-274)
    temperatures.insert(0,-274)
    for i in range(len(temperatures)):
        if ((temperatures[i] > temperatures[i-1]) and (temperatures[i] > temperatures[i+1])):
            count += 1
    return count

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
