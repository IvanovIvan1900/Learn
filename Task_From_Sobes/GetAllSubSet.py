if __name__ == '__main__':
    subsets([1, 2, 2]) -> [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    subsets([1, 2, 3]) -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    subsets([0]) -> [[], [0]]