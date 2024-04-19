import copy
import pandas as pd

# Loads the second part of the file containing instructions into the DataFrame, cleans the data and retypes Series into
# integers.
file = "uloha_5_data.txt"
instructions_df = pd.read_csv(file, skiprows=10, header=None, sep=" ")
instructions_df.drop(columns=[0, 2, 4], axis=1, inplace=True)
instructions_df.rename(columns={1: "move", 3: "from", 5: "to"}, inplace=True)
instructions_df.astype(int)

# This part loads the first part of the exercise(first 9 lines) containing stacks of cargo into a list of lists,
# each containing one stack without empty spaces or square brackets.
cargo = []
with open(file) as my_file:
    for line in range(9):
        cargo.append(my_file.readline())
stacks = [[] for _ in range(9)]
for line in cargo[:-1]:
    for i, s in enumerate(stacks):
        if line[1 + i * 4] != ' ':
            s.append(line[1 + i * 4])
for s in stacks:
    s.reverse()

# Creates hard copies of stacks, so it works for both parts of the solution.
stacks_one = copy.deepcopy(stacks)
stacks_two = copy.deepcopy(stacks)


def part_one(stacks_part_one, instructions):
    """
    This function provides the solution for part of one of the exercise.
    :list stacks_part_two:  includes the list of stacks
    :DataFrame instructions: includes DataFrame of instructions
    :return: prints the result in a single line
    """
    for rows, cols in instructions.iterrows():
        operation = stacks_part_one[cols["from"] - 1][-cols["move"]:]
        del stacks_part_one[cols["from"] - 1][-cols["move"]:]
        for op in range(len(operation)):
            sub_operation = operation[-1]
            del operation[-1]
            stacks_part_one[cols["to"] - 1].extend(sub_operation)

    for stack in stacks_part_one:
        print(stack[-1], end="")


def part_two(stacks_part_two, instructions):
    """
    This function provides the solution for part of two of the exercise.
    :list stacks_part_two:  includes the list of stacks
    :DataFrame instructions: includes DataFrame of instructions
    :return: prints the result in a single line
    """
    for rows, cols in instructions.iterrows():
        operation = stacks_part_two[cols["from"] - 1][-cols["move"]:]
        del stacks_part_two[cols["from"] - 1][-cols["move"]:]
        stacks_part_two[cols["to"] - 1].extend(operation)

    for stack in stacks_part_two:
        print(stack[-1], end="")


def main():
    print("The result of the part one of the exercise is: ", end="")
    part_one(stacks_one, instructions_df)
    print()
    print("The result of the part two of the exercise is: ", end="")
    part_two(stacks_two, instructions_df)


if __name__ == "__main__":
    main()
