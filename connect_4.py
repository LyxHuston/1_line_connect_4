[running := True, WhileTrue := type("WhileTrue", (), {"__init__": lambda self, condition, exc: [self.__dict__.update(locals()), {None for _ in self}, None][-1], "__iter__": lambda self: self, "__next__": lambda self: self.exc() if self.condition() else exec("raise StopIteration")}), check_input := lambda inp, tests, on=0, done=-1, **kwargs: inp if tests(inp) else incorrect_input(tests, done, **kwargs), incorrect_input := lambda tests, done, **kwargs: check_input(input('Input was invalid.  Please enter again. '), tests, 0, done, **kwargs), record := [0, 0, 0], get_place := lambda player, stacks: int(check_input(input(f"Player {player}\'s ({('X', 'O')[player - 1]}) move: "), lambda inp: inp.isdigit() and 0 <= int(inp) < x and stacks[int(inp)] < y)), draw_line := lambda line: print("|" + str([{None: " ", 1: "X", 2: "O"}[board.get((x_val, line))] for x_val in range(x)]).replace("\', \'", "|")[2:-2] + "|"), draw_board := lambda: [print(str([x_val for x_val in range(x)]).replace(" ", "")), *(draw_line(line) for line in reversed(range(y)))], game := lambda: [board := dict(), stacks := [0 for _ in range(x)], info := [0, True, int(check_input(input("Which player should go first? (1, 2) "), lambda inp: inp.isdigit() and 0 < int(inp) <= 2)), 0], globals().update(locals()), draw_board(), WhileTrue(lambda: info[1] and info[0] < (x * y), lambda: single_loop(info, stacks)), record.__setitem__(info[3], record[info[3]] + 1), print(f"Game over on turn {info[0]}.")], check_dir := lambda at_x, at_y, vector, wanted: 1 + check_dir(at_x + vector[0], at_y + vector[1], vector, wanted) if board.get((at_x, at_y), 3) == wanted else 0, check_win := lambda at_x, at_y, player: max(collapse_nums([check_dir(at_x, at_y, vector, player) for vector in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]])) > 4, collapse_nums := lambda lst: [lst[num] + lst[num + int(len(lst)/2)] for num in range(len(lst)//2)], single_loop := lambda info, stacks: [info.__setitem__(0, info[0] + 1), print(f"Turn {info[0]}."), place := get_place(info[2], stacks), board.__setitem__((place, stacks[place]), info[2]), draw_board(), info.__setitem__(*((1, False) if check_win(place, stacks[place], info[2]) else (2, (info[2] % 2) + 1))), None if info[1] else info.__setitem__(3, info[2]), stacks.__setitem__(place, stacks[place] + 1)], loop := lambda: [game(), print(f"You have tied {record[0]} time(s)."), print(f"Player 1 has won {record[1]} time(s)."), print(f"Player 2 has won {record[2]} time(s)."), globals().__setitem__("running", input("Would you like to play again? (Y/N) ") == "Y")], pos_dig := lambda i: i.isdigit() and int(i) > 0, y := int(check_input(input('How tall should the board be? '), pos_dig)), x := int(check_input(input('How wide should the board be? '), pos_dig)), WhileTrue(lambda: running, loop)]
