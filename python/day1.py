import collections
from pathlib import Path
import unittest

dataFile = "day1_data.txt"

testData = """3   4
4   3
2   5
1   3
3   9
3   3"""


def formatInput(inputData):
    inputs = [[], []]
    for line in inputData.splitlines():
        l, r = line.split()
        inputs[0].append(int(l))
        inputs[1].append(int(r))

    [i.sort() for i in inputs]
    return inputs


def part1(inputData):
    deltas = []
    for i, j in zip(inputData[0], inputData[1]):
        deltas.append(abs(j - i))

    return sum(deltas)


def part2(inputData):
    similarityScores = []

    appearances = collections.Counter(inputData[1])

    for i in inputData[0]:
        similarityScores.append(i * appearances[i])

    return sum(similarityScores)


class Day1Test(unittest.TestCase):
    def test_Part1WithTestData(self):
        self.assertEqual(part1(formatInput(testData)), 11)

    def test_Part2WithTestData(self):
        self.assertEqual(part2(formatInput(testData)), 31)

    def test_Part1(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            data = inputFile.read()
            self.assertEqual(part1(formatInput(data)), 2430334)

    def test_Part2(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            data = inputFile.read()
            self.assertEqual(part2(formatInput(data)), 28786472)


if __name__ == "__main__":
    unittest.main()
