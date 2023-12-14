# from BlockWorldAgent import BlockWorldAgent
import copy
import time


class BlockWorldAgent:

    def __init__(self):
        pass

    def solve(self, initial_arrangement, goal_arrangement):

        start = time.time()

        class State:
            def __init__(self, first_stack, second_stack, total_num, moves=None):
                if moves is None:
                    moves = []
                self.first_stack = first_stack
                self.second_stack = second_stack
                self.total_num = total_num
                self.moves = moves

            def __eq__(self, other):
                return (self.first_stack == other.first_stack and self.second_stack == other.second_stack
                        and self.total_num == other.total_num and self.moves == other.moves)

            def goal_state_move(self):
                while self.difference() != 0:
                    self = self.select_move()
                return self.moves

            def select_move(self):  # will select and return the best move
                # first try moving the top block to a stack, if the diff is not reduced, then move it to the temp_table
                for index, stack in enumerate(self.first_stack):
                    for index2, stack2 in enumerate(self.first_stack):
                        if index != index2:  # don't move to itself stack
                            curr_table, move = self.valid_state_move(self.first_stack, index, index2)
                            new_state = State(curr_table, self.second_stack, self.total_num, copy.copy(self.moves))
                            new_state.moves.append(move)
                            if new_state.difference() < self.difference():
                                return new_state

                # move the top block to the temp_table, skip if it is already on the table (itself alone on a table)
                for index, stack in enumerate(self.first_stack):
                    if len(stack) > 1:  # not it self alone
                        curr_table, move = self.valid_state_move(self.first_stack, index, -1)  # -1 means table
                        new_state = State(curr_table, self.second_stack, self.total_num, copy.copy(self.moves))
                        new_state.moves.append(move)
                        if new_state.difference() <= self.difference():
                            return new_state

            def valid_state_move(self, table, start_index, end_index):
                temp_table = copy.deepcopy(table)
                left = temp_table[start_index]
                top_block = left.pop()
                right = []

                if end_index < 0:  # move to table (-1)
                    temp_table.append(right)
                    move = (top_block, 'Table')
                else:  # move to stack
                    right = temp_table[end_index]
                    move = (top_block, right[-1])
                right.append(top_block)

                if len(left) == 0:
                    temp_table.remove(left)
                return temp_table, move

            def difference(self):
                same_num = 0
                # compare each stack on two stacks
                for left in self.first_stack:
                    for right in self.second_stack:
                        index = 0
                        while index < len(left) and index < len(right):
                            if left[index] == right[index]:
                                same_num += 1
                                index += 1
                            else:
                                break
                diff = self.total_num - same_num
                return diff

        total_num = 0
        for ls in initial_arrangement:
            for e in ls:
                total_num += 1
        state = State(initial_arrangement, goal_arrangement, total_num)
        solution = state.goal_state_move()

        end = time.time()
        run_time = str((end - start) * 1000)
        print("Running time:" + run_time + "ms")
        return solution

def test():
    # This will test your BlockWorldAgent
    # with eight initial test cases.
    test_agent = BlockWorldAgent()

    initial_arrangement_1 = [["A", "B", "C"], ["D", "E"]]
    goal_arrangement_1 = [["A", "C"], ["D", "E", "B"]]
    goal_arrangement_2 = [["A", "B", "C", "D", "E"]]
    goal_arrangement_3 = [["D", "E", "A", "B", "C"]]
    goal_arrangement_4 = [["C", "D"], ["E", "A", "B"]]

    print(test_agent.solve(initial_arrangement_1, goal_arrangement_1))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_2))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_3))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_4))

    initial_arrangement_2 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    goal_arrangement_5 = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
    goal_arrangement_6 = [["I", "H", "G", "F", "E", "D", "C", "B", "A"]]
    goal_arrangement_7 = [["H", "E", "F", "A", "C"], ["B", "D"], ["G", "I"]]
    goal_arrangement_8 = [["F", "D", "C", "I", "G", "A"], ["B", "E", "H"]]

    print(test_agent.solve(initial_arrangement_2, goal_arrangement_5))
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_6))
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_7))
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_8))


if __name__ == "__main__":
    test()