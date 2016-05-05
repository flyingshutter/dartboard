import dartboard
import time
import sys


def parse_line(line):
    line = line.replace(':', '#').replace('@', '#').split('#')
    stat = {}
    for i in [1, 3, 5, 7, 9, 11, 13]:
        stat[line[i]] = line[i+1]

    # convert Players string to int
    stat['Players'] = int(stat['Players'])
    return stat


def detect_game(board):
    game_name = 'None'
    num_player = -1

    line = parse_line(board.get_line())

    while (game_name == 'None')  or (line['Display1'][0] == 'G'):
        if line['Display1'][0] == 'G':
            game_name = line['Display1']
        line = parse_line(board.get_line())

    while line['Players'] == 0:
        if line['Display2'][2] == 'P':
            num_player = int(line['Display2'][1])
        line = parse_line(board.get_line())

    if num_player == -1:
        num_player = 2

    return {'num_player': num_player, 'game_name': game_name}


if __name__ == '__main__':

    print len(sys.argv)
    print sys.argv

    if len(sys.argv) > 1:
        d = dartboard.PseudoDartboard(sys.argv[1])
    else:
        d = dartboard.Dartboard()

    keep_running = 1
    while keep_running:
        # check if end
        keep_running = 0
        
        # get and process dartboard info
        # x = d.get_line()
        # print x

        # detect game
        game = detect_game(d)
        print game
        time.sleep(0.1)

        # update display
        
        # process database
