import dartboard
import time
import sys


class PlayDart:
    board = 0
    game = 0

    def __init__(self, filename=''):
        if filename != '':
            self.board = dartboard.PseudoDartboard(filename)
        else:
            self.board = dartboard.Dartboard()

    def detect_game(self):
        game_name = 'None'
        num_player = -1

        line = self.board.get_msg()
        while (game_name == 'None') or (line['Display1'][0] == 'G'):
            if line['Display1'][0] == 'G':
                game_name = line['Display1']
            line = self.board.get_msg()

        while line['Players'] == 0:
            if line['Display2'][2] == 'P':
                num_player = int(line['Display2'][1])
            line = self.board.get_msg()

        if num_player == -1:
            num_player = 2

        self.game = {'num_player': num_player, 'game_name': game_name}

    def register_players(self):
        player_names = []
        for i in range(self.game['num_player']):
            name = raw_input('Enter name of player {:}: '.format(i+1))
            player_names.append(name)
        self.game['player_names'] = player_names

    def process_turn(self, i):
        # msgs have to be read from self without get_msg first, because it's already there from detect_game
        while self.board.msg['Players'] == pow(2,i):
            print(i)
            self.board.get_msg()

    def play_game(self):
        while 1:
            for i in range(self.game['num_player']):
                while self.board.msg['Players'] != pow(2,i):
                    self.board.get_msg()

                self.process_turn(i)


if __name__ == '__main__':
    # parse command line args and initialize dartboard
    if len(sys.argv) > 1:
        g = PlayDart(sys.argv[1])
        # g.board.verbose = 0
    else:
        g = PlayDart()

    keep_running = 1
    while keep_running:      # enter main loop
        keep_running = 0
        
        # get dartboard msg
        # x = d.get_msg()
        # print x

        # detect game
        print ('#############################################')
        print ('## Waiting for game selection...')
        g.detect_game()
        print ('## game detected: game=' + str(g.game))

        # register players
        print ('#############################################')
        print ('## Register players...')
        g.register_players()
        print ('## Players registered: game=' + str(g.game))

        # play game
        g.play_game()
        # update display
        
        # process database
        time.sleep(0.1)
