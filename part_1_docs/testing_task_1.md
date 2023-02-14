### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False

# Line 21: Should read if card.value == 1: missing the double =
# Line 23: The else is missing:

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
 
# Line 29: Typo in "def" for defining the funtcion. 
# Line 29: There is a missing comma after card1 
# Line 30: The if should be indented and not on the same line as the def, this means that everything needs to be intended by one to correct. 
# Line 30: Missing number, simple says card and should say card1


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

#Line 42: Missing what the total is equal to, so should be total = 0 
#Line 45: The function is returning a string, therefore the total should also be converted to a sting using str(total)

```