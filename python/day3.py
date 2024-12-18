from itertools import pairwise
from pathlib import Path
import re
import unittest

dataFile = "day3_data.txt"

testData = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


def parseInput(inputData, regex):
    return re.findall(regex, inputData)


def part1(inputData):
    regex = r"mul\((\d+),(\d+)\)"
    ops = parseInput(inputData, regex)
    return sum(int(i) * int(j) for i, j in ops)


def part2(inputData):
    pass


class Day2Test(unittest.TestCase):
    def test_Part1WithTestData(self):
        self.assertEqual(part1(testData), 161)

    def test_Part2WithTestData(self):
        self.assertEqual(part2(testData), 4)

    def test_Part1(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            inputData = inputFile.read()
            self.assertEqual(part1(inputData), 190604937)

    # def test_Part2(self):
    #     with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
    #         inputData = inputFile.readlines()
    #         self.assertEqual(part2(inputData), 569)


if __name__ == "__main__":
    unittest.main()
