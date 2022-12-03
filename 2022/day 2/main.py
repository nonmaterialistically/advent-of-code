file = open('input.txt', 'r')
Lines = file.readlines()

move_values = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

move_meanings = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

what_wins_over = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

result_meanings = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

score1 = 0
score2 = 0

for i in Lines:
    #part1
    opponent = i.strip().split()[0]
    response = i.strip().split()[1]
    score1 = score1 + move_values[move_meanings[response]]
    if move_meanings[opponent] == move_meanings[response]:
        score1 = score1 + 3
    if (move_meanings[opponent] == "rock" and move_meanings[response] == "paper") or (move_meanings[opponent] == "paper" and move_meanings[response] == "scissors") or (move_meanings[opponent] == "scissors" and move_meanings[response] == "rock"):
        score1 = score1 + 6
    #part2
    result = i.strip().split()[1]
    if result_meanings[result] == "draw":
        response = move_meanings[opponent]
        score2 = score2 + 3
        score2 = score2 + move_values[response]
    if result_meanings[result] == "win":
        response = what_wins_over[move_meanings[opponent]]
        score2 = score2 + 6
        score2 = score2 + move_values[response]
    if result_meanings[result] == "lose":
        response = [k for k, v in what_wins_over.items() if v == move_meanings[opponent]][0]
        score2 = score2 + move_values[response]
print("Part 1 score: " + str(score1))
print("Part 2 score: " + str(score2))