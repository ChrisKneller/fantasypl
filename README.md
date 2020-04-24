# fantasypl
My repo for accessing the fantasy premier league API.

This project has basic functionality but there is a lot of scope for expansion.

## Usage

Clone the repo:
```bash
git clone https://github.com/ChrisKneller/fantasypl.git
```

Try out some basic commands.

```bash
>>> from fantasypl import FPL, User, ClassicLeague 
>>> fpl = FPL()
>>> fpl.login()
Enter your fpl email address: christiankneller@gmail.com
Enter the password associated with 'christiankneller@gmail.com': 
Connected to FPL server. Attempting login...
Successfully logged in: Chris Kneller - Holding Matip
>>>
>>> me = fpl.User
>>> fpl.get_plplayers()
Getting all players...
Got players
>>>
>>> fpl.get_plplayer_by_id(318)  
McCarthy
>>> fpl.get_plplayer_by_id(182) 
Alexander-Arnold
>>> fpl.get_plplayer_by_id(191) 
Salah
>>> myteam = me.get_team()
>>> for player in myteam:
...     player = fpl.get_plplayer_by_id(player['element'])
...     print(f"{player} has a first name of {player.first_name}, costs {player.cost} and plays for {player.team}. Their FPL position is {player.position}")
... 
McCarthy has a first name of Alex, costs 45 and plays for Southampton. Their FPL position is Goalkeeper
Alexander-Arnold has a first name of Trent, costs 78 and plays for Liverpool. Their FPL position is Defender
Lundstram has a first name of John, costs 49 and plays for Sheffield Utd. Their FPL position is Defender
Williams has a first name of Brandon, costs 42 and plays for Man Utd. Their FPL position is Defender
Salah has a first name of Mohamed, costs 127 and plays for Liverpool. Their FPL position is Midfielder
De Bruyne has a first name of Kevin, costs 106 and plays for Man City. Their FPL position is Midfielder
Saka has a first name of Bukayo, costs 47 and plays for Arsenal. Their FPL position is Midfielder
Mané has a first name of Sadio, costs 125 and plays for Liverpool. Their FPL position is Midfielder
Jiménez has a first name of Raúl, costs 81 and plays for Wolves. Their FPL position is Forward
Jota has a first name of Diogo, costs 64 and plays for Wolves. Their FPL position is Forward
Aubameyang has a first name of Pierre-Emerick, costs 111 and plays for Arsenal. Their FPL position is Forward
McGovern has a first name of Michael, costs 41 and plays for Norwich. Their FPL position is Goalkeeper
Hayden has a first name of Isaac, costs 44 and plays for Newcastle. Their FPL position is Midfielder
Aurier has a first name of Serge, costs 49 and plays for Spurs. Their FPL position is Defender
Taylor has a first name of Charlie, costs 43 and plays for Burnley. Their FPL position is Defender
>>>
>>> salah = fpl.get_plplayer_by_name("Salah") 
>>> salah.first_name 
'Mohamed'
>>> salah.cost 
127
>>> salah.position 
'Midfielder'
>>> salah.team    
'Liverpool'
>>> salah.points
{'gamweweek': 0, 'total': 186}
```

Please explore the codebase to discover further uses. Unfortunately I don't have the time to expand this or write up any docs at the moment, but if there happens to be the demand for it I will try to free up some time.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
