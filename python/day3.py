from itertools import pairwise
from pathlib import Path
import re
import unittest

dataFile = "day3_data.txt"

p1TestData = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)

p2TestData = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


def part1(inputData):
    regex = r"mul\((\d+),(\d+)\)"
    return sum(int(i) * int(j) for i, j in re.findall(regex, inputData))


def part2(inputData):
    regex = r"don't|do|mul\((\d+),(\d+)\)"
    ops = re.finditer(regex, inputData)

    do = 1
    mul = 0

    for i in ops:
        if i.groups()[0] and do:
            mul += int(i.groups()[0]) * int(i.groups()[1])
        elif (i.group(0)) == "do":
            do = 1
        elif (i.group(0)) == "don't":
            do = 0

    return mul


class Day2Test(unittest.TestCase):
    def test_Part1WithTestData(self):
        self.assertEqual(part1(p1TestData), 161)

    def test_Part2WithTestData(self):
        self.assertEqual(part2(p2TestData), 48)

    def test_Part1(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            inputData = inputFile.read()
            self.assertEqual(part1(inputData), 190604937)

    def test_Part2(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            inputData = inputFile.read()
            self.assertEqual(part2(inputData), 82857512)


if __name__ == "__main__":
    unittest.main()
