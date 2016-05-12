import dartboard
import time
import sys


class PlayDart:
    board = None
    game = {}
    turn = {}
    log_turns = []
    log_hits = []

    def __init__(self, filename=''):
        if filename != '':
            self.board = dartboard.PseudoDartboard(filename)
        else:
            self.board = dartboard.Dartboard()

    def detect_game(self):
        game_name = 'None'
        num_player = -1

        line = self.board.update_msg()
        while (game_name == 'None') or (line['Display1'][0] == 'G'):
            if line['Display1'][0] == 'G':
                game_name = line['Display1']
            line = self.board.update_msg()

        while line['Players'] == 0:
            if line['Display2'][2] == 'P':
                try:
                    num_player = int(line['Display2'][1])
                except:
                    pass
            line = self.board.update_msg()

        if num_player == -1:
            num_player = 2

        self.game = {'id': int(self.board.msg['Time']),
                     'num_player': num_player,
                     'game_name': game_name,
                     'player_active': [1 for i in range(num_player)],
                     'ranking': []
                     }

    def register_players(self):
        player_names = []
        for i in range(self.game['num_player']):
            name = raw_input('Enter name of player {:}: '.format(i+1))
            player_names.append(name)
        self.game['player_names'] = player_names

    def parse_hit(self, candidate, hit_time, player):
        if ')' in candidate:
            multiplier = 3
            candidate = candidate.split(')')[1]
        elif '(' in candidate:
            multiplier = 2
            candidate = candidate.split('(')[1]
        else:
            multiplier = 1

        candidate = int(candidate)
        return {'multiplier': multiplier,
                'time': hit_time,
                'number': candidate,
                'player': player,
                'game_id': self.game['id'],
                }

    def process_turn(self, player):
        bar = 'Bar' + str((player % 2)+1)
        display = 'Display' + str((player % 2)+1)
        score = 'Score' + str((player % 2)+1)
        num_hits = 0
        hits = []

        self.turn = {'player': player, 'score_begin': self.board.msg[display]}
        # msgs have to be read from self without update_msg first, because it's already there from detect_game
        while self.board.msg['Players'] == pow(2, player):
            print [self.board.msg[i] for i in [bar, display, score]]
            # detect hit
            if self.board.msg[display] == '   ':
                hit_time = self.board.msg['Time']
                self.board.update_msg()
                candidate = self.board.msg[display]
                self.board.update_msg()
                self.board.update_msg()
                if self.board.msg[display] == candidate:
                    num_hits += 1
                    hit = self.parse_hit(candidate, hit_time, player)
                    hits.append(hit)
                    self.log_hits.append(hit)
                else:
                    print('WEIRD HIT: {:} does not match {:}\n'.format(candidate, self.board.msg[display]))
                self.board.update_msg()

            self.turn['score_end'] = self.board.msg[display]
            self.board.update_msg()

        self.turn['hits'] = hits
        self.turn['num_hits'] = num_hits
        print self.turn

    def play_game(self):
        turn_num = 0
        while sum(self.game['player_active']) > 1:
            print ('-------- Turn number:  {:} -------------'.format(turn_num))
            # loop over players that haven't finished yet
            for i in [j for j in range(self.game['num_player']) if self.game['player_active'][j] == 1]:
                while self.board.msg['Players'] != pow(2, i):
                    self.board.update_msg()

                print ('-------- Player {:}: {:}'.format(i + 1, self.game['player_names'][i]))
                self.process_turn(i)
                self.log_turns.append(self.turn)
                if '15t' in self.turn['score_end']:
                    self.game['ranking'].append(i)
                    self.game['player_active'][i] = 0
                turn_num += 1

        print('-------------------------------------------------------')
        print('------------GAME FINISHED------------------------------')
        print('-------------------------------------------------------')


if __name__ == '__main__':
    # parse command line args and initialize dartboard
    if len(sys.argv) > 1:
        g = PlayDart(sys.argv[1])
        g.board.verbose = 0
    else:
        g = PlayDart()
        g.board.verbose = 0
        
    keep_running = 1
    while keep_running:      # enter main loop
        keep_running = 0
        
        # get dartboard msg
        # x = d.update_msg()
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

        print('Really........')
        # process database
