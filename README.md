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
python
```

```python
>>> from fantasypl import FPL, User, ClassicLeague 
>>> fpl.login()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fpl' is not defined
>>> fpl = FPL()
>>> fpl.login()
Enter your fpl email address: christiankneller@gmail.com
Enter the password associated with 'christiankneller@gmail.com': 
Connected to FPL server. Attempting login...
Successfully logged in: Chris Kneller - Holding Matip
<Response [200]>
>>> me = fpl.User
>>> fpl.get_plplayers()
Getting all players...
Got players
>>> me.get_team()       
[{'element': 318, 'position': 1, 'selling_price': 44, 'multiplier': 1, 'purchase_price': 43, 'is_captain': False, 'is_vice_captain': False}, {'element': 182, 'position': 2, 'selling_price': 74, 'multiplier': 1, 'purchase_price': 70, 'is_captain': False, 'is_vice_captain': False}, {'element': 297, 'position': 3, 'selling_price': 44, 'multiplier': 1, 'purchase_price': 40, 'is_captain': False, 'is_vice_captain': False}, {'element': 549, 'position': 4, 'selling_price': 41, 'multiplier': 1, 'purchase_price': 40, 'is_captain': False, 'is_vice_captain': False}, {'element': 191, 'position': 5, 'selling_price': 124, 'multiplier': 1, 'purchase_price': 122, 'is_captain': False, 'is_vice_captain': True}, {'element': 215, 'position': 6, 'selling_price': 104, 'multiplier': 1, 'purchase_price': 103, 'is_captain': False, 'is_vice_captain': False}, {'element': 541, 'position': 7, 'selling_price': 46, 'multiplier': 1, 'purchase_price': 46, 'is_captain': False, 'is_vice_captain': False}, {'element': 192, 'position': 8, 'selling_price': 124, 'multiplier': 2, 'purchase_price': 123, 'is_captain': True, 'is_vice_captain': False}, {'element': 409, 'position': 9, 'selling_price': 79, 'multiplier': 1, 'purchase_price': 78, 'is_captain': False, 'is_vice_captain': False}, {'element': 410, 'position': 10, 'selling_price': 62, 'multiplier': 1, 'purchase_price': 61, 'is_captain': 
False, 'is_vice_captain': False}, {'element': 11, 'position': 11, 'selling_price': 110, 'multiplier': 1, 'purchase_price': 110, 'is_captain': False, 'is_vice_captain': False}, {'element': 281, 'position': 12, 'selling_price': 40, 'multiplier': 0, 'purchase_price': 40, 'is_captain': False, 'is_vice_captain': False}, {'element': 271, 'position': 13, 'selling_price': 43, 'multiplier': 0, 'purchase_price': 43, 'is_captain': False, 'is_vice_captain': False}, {'element': 336, 'position': 14, 'selling_price': 49, 'multiplier': 0, 'purchase_price': 49, 'is_captain': False, 'is_vice_captain': False}, {'element': 87, 'position': 15, 'selling_price': 43, 'multiplier': 0, 'purchase_price': 43, 'is_captain': False, 'is_vice_captain': False}]
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
```

Please explore the codebase to discover further uses. Unfortunately I don't have the time to expand this or write up any docs at the moment, but if there happens to be the demand for it I will try to free up some time.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT