# TweetCensor #
Censor tweets by changing characters with similar looking ones, not appearing in searches.

## How to use ##
* Create a text file named _message.txt_ in the same folder as _main.py_ with the desired text to be censored.
* Run _main.py_.
* The edited text can be found in _censored.txt_.

## Example ##
Original text:
```
the quick "brown" fox, jumps over the lazy dog.
THE QUICK "BROWN" FOX; JUMPS OVER THE LAZY DOG!
```
Censored text:
```
tհе qᴜісk "𝖻rоᴡո" fох, јᴜmрѕ оᴠеr tհе lаᴢу ԁоɡ.
ТНЕ Q∪ІСК "ВRОᎳΝ" ᖴОХ; Ј∪МРЅ ОᏙЕR ТНЕ ᏞАΖҮ ᎠОԌ!
```
