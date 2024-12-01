import unittest


def formatInput(inputData):
    inputs = [[], []]
    for line in inputData.split("\n"):
        print(line)
        inputs[0].append(int(line.split()[0]))
        inputs[1].append(int(line.split()[1]))
    return inputs


def part1(inputData):
    deltas = []
    for line in inputData:
        line.sort()

    for i, j in zip(inputData[0], inputData[1]):
        deltas.append(abs(j - i))

    return sum(deltas)


class Day1Test(unittest.TestCase):
    def test_WithTestData(self):
        testData = """3   4
4   3
2   5
1   3
3   9
3   3"""
        self.assertEqual(part1(formatInput(testData)), 11)

    def test_Part1(self):
        with open("day1_data.txt", "r") as inputFile:
            data = inputFile.read()
            self.assertEqual(part1(formatInput(data)), 2430334)


if __name__ == "__main__":
    unittest.main()
