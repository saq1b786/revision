import json 
from pathlib import Path
class Player(): 

    def __init__(self, name: str, position: str):
        self.name = name 
        self.position = position 
        self.tallies = 0 

    def __str__(self):
        return f' {self.name}, {self.position}, {self.tallies}'

    def add_tally(self): 
        self.tallies += 1 

    def is_flagged(self):
        return self.tallies >= 3

    def to_dict(self): 

        player_dict = {
            'name': self.name,
            'position': self.position,
            'tallies': self.tallies
        }
        return player_dict


def main():

    if Path('players.json').exists():
        with open('players.json', 'r') as file:
            player_list = json.load(file)
        for item in player_list:
            player = Player(item["name"], item["position"])
            player.tallies = item["tallies"]
            players.append(player)

    players = []

    while True:
        print('1. Add player')
        print('2. View all players')
        print('3. Add tally to player')
        print('4. View flagged players')
        print('5. Save and quit')

        try:
            option = int(input('Pick a number: '))
        except ValueError:
            print('Must be a number')
            continue

        if option == 1:
            name = input('enter player name: ')
            position = input('enter player position: ')
            new_player = Player(name, position)
            players.append(new_player)

        elif option == 2: 
            for player in players: 
                print(player)

        elif option == 3: 
            player_name = input('player name: ')
            for player in players: 
                if player.name == player_name: 
                    player.add_tally()
                    print(f' tally added to {player.name}')
                    break

        elif option == 4: 
            for player in players: 
                if player.is_flagged():
                    print(player)

        elif option == 5: 
            player_list = []
            for player in players: 
                player_list.append(player.to_dict())

            with open('players.json', 'w') as file: 
                json.dump(player_list, file, indent=4)

            print('saved!')
            break

            


            





