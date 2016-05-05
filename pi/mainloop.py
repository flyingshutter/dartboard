import dartboard
import time
import sys


def detect_game(board):
    game_name = 'None'
    num_player = -1

    line = board.get_msg()
    while (game_name == 'None') or (line['Display1'][0] == 'G'):
        if line['Display1'][0] == 'G':
            game_name = line['Display1']
        line = board.get_msg()

    while line['Players'] == 0:
        if line['Display2'][2] == 'P':
            num_player = int(line['Display2'][1])
        line = board.get_msg()

    if num_player == -1:
        num_player = 2

    return {'num_player': num_player, 'game_name': game_name}


def register_players(game):
    player_names = []
    for i in range(game['num_player']):
        name = raw_input('Enter name of player {:}: '.format(i+1))
        player_names.append(name)
    game['player_names'] = player_names
    return game


if __name__ == '__main__':
    # parse command line args and initialize dartboard
    if len(sys.argv) > 1:
        d = dartboard.PseudoDartboard(sys.argv[1])
        d.verbose = 0
    else:
        d = dartboard.Dartboard()

    keep_running = 1
    while keep_running:      # enter main loop
        keep_running = 0
        
        # get dartboard msg
        # x = d.get_msg()
        # print x

        # detect game
        print ('#############################################')
        print ('## Waiting for game selection...')
        my_game = detect_game(d)
        print ('## game detected: game=' + str(my_game))

        # register players
        print ('#############################################')
        print ('## Register players...')
        my_game = register_players(my_game)
        print ('## Players registered: game=' + str(my_game))

        # update display
        
        # process database
        time.sleep(0.1)
