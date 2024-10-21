# PlexPy-Lifx-and-Notification
A Python script that I use with Plexpy to dim and brighten my lights as well as send a Join notification whenever one of my friends starts watching something. 

Plexpy runs the script whenever someone starts, stops, pauses, or resumes any media. Plexpy passes these arguments whenever the script is run:
```
python Command.py "{player}" "{user}" "{action}" "{title}"
```

Therefore a script run using these commands:
```
python Command.py "XboxOne" "tbmx12" "Play" "Iron man 3"
```
would result in a Join notification that says: "tbmx12 has started watching: Iron man 3"

And a script run using these commands:
```
python Command.py "SHIELD Android TV" "caj380" "Stop" "Iron man 3"
```
or
```
python Command.py "SHIELD Android TV" "caj380" "Pause" "Iron man 3"
```
would brighten the lights.

And a script run using these commands:
```
python Command.py "SHIELD Android TV" "caj380" "Play" "Iron man 3"
```
or
```
python Command.py "SHIELD Android TV" "caj380" "Resume" "Iron man 3"
```
would dim the lights.
