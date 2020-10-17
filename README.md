# Coach Ride to Devil Castle

Implementing the broad game *Coach Ride to Devil Castle* by Python.

## Introduction

Castle of the Devil is a 4-8 player card game.

All players are passengers within a carriage that is rushing to Devil's Castle. They each act as a member of a secret association, but no one knows who is friend and who is foe.

Each player starts in one of two secret associations. He also gets a secret profession with a special ability. So at the beginning of the game you have no information about the membership and the professions of the others. To win the game, each association has to collect 3 defined artifacts jointly. Therefore you have to find out who your allies are and where to find the artifacts among the other secret objects that are in possession of other players. 

You can get this information during the game either by trading objects with other players, because every object has a special ability, e.g. "Trade it in and you may take a look at your trading partners-association." or by struggling with other players, because the winner of a struggle can view the cards of the underdog and steal one of them. But be careful, all players can support the attacker OR defender in a struggle. If they know about your identity but you don't know theirs it may be risky to struggle.

You may find more information about this game in the [Borad Game Geek Page](https://boardgamegeek.com/boardgame/25951/castle-devil).

## Development Log

- [x] Main processes
    - [x] Trade
    - [x] Duel
    - [x] Proclaim the victory
- [ ] Professions
    - [x] Basic introduction
    - [ ] Effects
- [ ] Objects
    - [x] Basic introduction
    - [ ] Effects
- [ ] Multi Users
    - [ ] Interaction System
    - [ ] Network Transform System
    - [ ] Host System
    - [ ] Clint System
- [ ] Optimization
    - [ ] Robustness Check

## File Structure

`main.py` The main process of this game: initialize, turns and victory calculation, containing functions about trade, duel and proclaim the victory actions.

`object.py` The class for 21 objects, containing the describes and effects functions.

`profession.py` The class for 10 professions, containing the describes and effects functions. 

`passenger.py` The class for players, each player has the properties of association, profession and objects, also with the detected list about other players' properties. 

## Environment Requirements

```
Python version: 3.8 or later
Python package: prettytable
```

## How to Play

So far, the developing status is really poor, only have the main process, which means, you can only trade or duel with other players without the effects of your trading objects. But at least you can detect others' association by duel, and you can also proclaim the victory, ..., with guessing randomly.  

Anyway, if you still want to try, just clone the code, and run `main.py` by `python main.py`, then it will guide you what to do next. 

## Game Process

At the beginning, after the game initialization, the game will start from player 0. At this time, player 0 will see:

```
Now is the turn for Passenger 1
+----------------------------------------------------------+
|                  Status for Passengers                   |
+-----------+-------------+------------+-------------------+
| Passenger | Association | Profession | Number of objects |
+-----------+-------------+------------+-------------------+
|     0     |     Red     |   Doctor   |         1         |
|     1     |   Unknown   |  Unknown   |         1         |
|     2     |   Unknown   |  Unknown   |         1         |
|     3     |   Unknown   |  Unknown   |         1         |
|     4     |   Unknown   |  Unknown   |         1         |
+-----------+-------------+------------+-------------------+
+----------------------------------------------------------+
|                   Your Objects                           |
+-------+----------------+---------------------------------+
| Index | Name of Object |            Describe             |
+-------+----------------+---------------------------------+
|   0   |      Key       | Blue team Victory with 3 keys.  |
+-------+----------------+---------------------------------+
What are you going to do? 
[1 - Trade; 2 - Duel; 3 - Proclaim the victory; 0 - Skip]
```

At the table **Status for Passengers,** you will see everyone's status about *association*, *profession* and *number of object* there, if they have been detected. 

Then at your turn, we will show all your objects, you may use them to trade with others. 

As the rule of this game, you have four choices in your turn, just input number to choose one. 

### Trade

If you want to trade with someone else, we will continuously ask you who you want to trade with. 

```
You are going to make a trade, who are you want to trade with? 
[Passenger Number]
```

Input the player number to initiate a trade. And don't forget you have choose one object for transaction, please also input the object number you want to trade out. 

```
Which object are you going to trade? 
[Object Number]
```

Your trade request will be sent to the player you chose. He will receive a message like this: 

```
Passenger 0 want to trade with you by Key. Do you agree? 
[y/n]
```

If this player denied this trade, your turn will be finished immediately. 

```
Your trade query is rejected.
```

Or he may accepted, then he will give something back, with or without effect. (Note that it still do not have real effect for the develop version so far.) At the receiver's terminal, we will also show what objects he has, and he can choose one to give back.  

```
Here are what you have, which one do you want to give back? 
+---------------------------------------------------------+
|                      Your Objects                       |
+-------+----------------+--------------------------------+
| Index | Name of Object |           Describe             |
+-------+----------------+--------------------------------+
|   0   | Casting Knives |    +1 if you are attacker      |
+-------+----------------+--------------------------------+
[Object Number]
```

```
Do you want to active the effect? 
[y/n]
```

After the settlement, this trade is completed. 

### Duel

If you want to make a duel with someone, just choose his player number. 

```
You are going to duel with someone, who are you want to duel with? 
[Passenger Number]
```

Then, from the next player, we will ask him who he will fight for.

```
Passenger 1 is going to duel with passenger 0
Ask passenger 1.Who are you going to fight for? 
[1 - Attacker; 2 - Defender; 0 - Skip]
```

We will show him who are making a duel now, and then he can choose to fight for the attacker or the defender, or just drink a cup of tea. 

After this, winner will have two choices to enjoy his winning. 

```
The winner is 1, what are you going to do? 
[1 - Check the association and profession; 2 - Get an object]
```

You can detect the loser's association and profession, or get an object. 

After that, the duel is done. 

### Proclaim the victory

Proclaim the victory is complex, please read the rule of this broad game firstly, I will just show you how to do this. 

Firstly, you can choose the positive victory or the negative victory. 

```
You are going to proclaim the victory. Which type of victory do you want to proclaim? 
[1 - Positive Victory; 2 - Negative Victory]
```

After that, just input the player index you want to choose, we will calculate everything for you. 

```
Choose passengers you think they will win. 
[Passengers index without split]
```

Then the game will end, your team will win or not, we just output a really simple result:

```
The RED association WIN!!!
```

You can have a big feast to celebrate it. See you next time. 

Until now, one round of this game is completed, let's move to the next player, until the end of this game. 

## Contact us

If you find bugs... please do not contact me at present. This is a really, really basic review, even we can not say it can work. 

But anyway, I will continuously work on this project.  Hope some day I can show you a not bad game, can be played game, a beautiful game, rather than a simple black box. 

See you. 