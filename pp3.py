# tapes: list of char list. each char list represents an infinite tape
# heads: list of head position. heads[i] is position of head in tapes[i]

class TM:
    START_STATE = 3
    FINAL_STATE = 2 # Single final state
    BLANK = '_'
    delta = [{} for i in range(8)]

    # delta[x][y] = [a, b, c]
    # '-> from state x with transition y, go to state a, write b and move c
    delta[0]['II_'] = [0, 'III', 'RRR']
    delta[0]['I__'] = [1, 'I__', 'SLL']
    delta[0]['_I_'] = [2, '_I_', 'SSS']

    delta[1]['III'] = [1, 'II_', 'SLL']
    delta[1]['I__'] = [0, 'I__', 'SRR']

    delta[3]['I__'] = [3, 'I__', 'RSS']
    delta[3]['#__'] = [4, '#__', 'RSS']

    delta[4]['I__'] = [4, 'II_', 'RRS']
    delta[4]['___'] = [5, '___', 'LLS']

    delta[5]['II_'] = [5, '_I_', 'LLS']
    delta[5]['#__'] = [6, '___', 'LRS']

    delta[6]['II_'] = [6, 'II_', 'LSS']
    delta[6]['_I_'] = [0, '_I_', 'RSS']

    def __init__(self, input_string):
        self.tapes = []
        self.heads = []
        for i in range(3):
            self.tapes.append([])
            self.heads.append(0)
        self.tapes[0] = [c for c in input_string]

    def write(self, tape_id, position, symbol):
        if position >= 0:
            if len(self.tapes[tape_id]) <= position:
                self.tapes[tape_id].append(symbol)
            else:
                self.tapes[tape_id][position] = symbol

    def move(self, tape_id, direction):
        self.heads[tape_id] += 'LSR'.index(direction)-1

    def read(self):
        on_tape = ''
        for i in range(3):
            if 0 <= self.heads[i] < len(self.tapes[i]):
                on_tape += self.tapes[i][self.heads[i]]
            else:
                on_tape += '_'
        return on_tape

    def getNextState(self, state, reading):
        curr = self.read()
        if curr in self.delta[state]:
            next_state = self.delta[state][curr][0]
            to_write = self.delta[state][curr][1]
            to_move = self.delta[state][curr][2]
            for i in range(3):
                self.write(i, self.heads[i], to_write[i])
                self.move(i, to_move[i])
            return next_state
        else:
            return None

    def run(self):
        curr_state = self.START_STATE
        while 1:
            next_state = self.getNextState(curr_state, self.read())
            if next_state == None:
                return 0
            elif next_state == self.FINAL_STATE:
                return 1
            curr_state = next_state

    def getTape(self, tape_id):
        return "".join([str(c) for c in self.tapes[tape_id] if c != self.BLANK])

def main():
    try:
        word = input()
        tm = TM(word)
        answer = word+"="
        if tm.run():
            answer += tm.getTape(2)+" ACEITA"
        else:
            answer += "REJEITA"
        print(answer)

        return main()
    except EOFError:
        return 0

if __name__ == '__main__':
    main()
