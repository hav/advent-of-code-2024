from itertools import pairwise
from pathlib import Path
import unittest

dataFile = "day2_data.txt"

testData = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def deltas(report):
    for a, b in pairwise(report):
        yield a - b


def isSafe(report):
    """
    Determines if a given report is safe based on specific conditions.

    A report is considered safe if:
    1. The absolute difference between consecutive numbers is between 1 and 3 (inclusive).
    2. The numbers are either strictly increasing or strictly decreasing.

    Args:
        report (list of int): A list of integers representing the report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    report = [int(i) for i in report]
    pairs = list(zip(report, report[1:]))

    deltasSafe = all(1 <= abs(i - j) <= 3 for i, j in pairs)
    incSafe = all(i > j for i, j in pairs)
    decSafe = all(i < j for i, j in pairs)

    return (incSafe or decSafe) and deltasSafe


def part1(inputData):
    return sum(isSafe(line.split()) for line in inputData)


def part2(inputData):
    def isExtraSafe(report):
        """
        Determines if a report can be made safe by removing one character from a line.

        Args:
            report (list): A list of lines representing the report.

        Returns:
            int: Returns 1 if the report can be made safe by removing one character, otherwise returns 0.
        """
        for i, _ in enumerate(report):
            newLine = report[:i] + report[i + 1 :]
            if isSafe(newLine):
                return 1
        return 0

    return sum(
        isSafe(report.strip().split()) or isExtraSafe(report.strip().split())
        for report in inputData
    )


class Day2Test(unittest.TestCase):
    def test_Part1WithTestData(self):
        self.assertEqual(part1(testData.splitlines()), 2)

    def test_Part2WithTestData(self):
        self.assertEqual(part2(testData.splitlines()), 4)

    def test_Part1(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            inputData = inputFile.readlines()
            self.assertEqual(part1(inputData), 524)

    def test_Part2(self):
        with open(Path(__file__).parent.joinpath(dataFile), "r") as inputFile:
            inputData = inputFile.readlines()
            self.assertEqual(part2(inputData), 569)


if __name__ == "__main__":
    unittest.main()
