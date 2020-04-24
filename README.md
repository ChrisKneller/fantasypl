# fantasypl
My repo for accessing the fantasy premier league API.

This project has basic functionality but there is a lot of scope for expansion.

## Usage

Clone the repo:
```bash
git clone https://github.com/ChrisKneller/fantasypl.git
```

Try out some basic commands.

```python
>>> from fantasypl import FPL, User, ClassicLeague 
>>> fpl = FPL()
>>> fpl.login()
Enter your fpl email address: christiankneller@gmail.com
Enter the password associated with 'christiankneller@gmail.com': 
Connected to FPL server. Attempting login...
Successfully logged in: Chris Kneller - Holding Matip
>>> me = fpl.User
>>> fpl.get_plplayers()
Getting all players...
Got players
>>> fpl.get_plplayer_by_id(318)  
McCarthy
>>> fpl.get_plplayer_by_id(182) 
Alexander-Arnold
>>> fpl.get_plplayer_by_id(191) 
Salah
>>> myteam = me.get_team()
>>> for player in myteam:
...     fpl.get_plplayer_by_id(player['element'])  
... 
McCarthy
Alexander-Arnold
Lundstram
Williams
Salah
De Bruyne
Saka
Mané
Jiménez
Jota
Aubameyang
McGovern
Hayden
Aurier
Taylor
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
