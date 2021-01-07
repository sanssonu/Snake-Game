Snake Game
======
This is an intermediate level Python program for the traditional Snake Game we all played on keypad phones.

The program constitutes of 4 python files:
1. snake.py 
2. food.py
3. scoreboard.py
4. main.py

Let's talk about each in detail.

snake.py  
======

This file is responsible for all the snake related activities. 
These are all defined in 
<font color="#ff4500"> class </font> Snake.

<font color="#ff8c00"> def </font> <font color="#ff1493"> __init__</font>(<font color="#ff69b4">self</font>):

* Constructor containing a list for storing all turtle's body's segments.
* Function call to create_snake() to create the body of the snake.
* An attribute 'head' which stores the first segment of snake's body as its head.

<font color="#ff8c00"> def </font> <font color="#daa520"> create_snake</font>(<font color="#ff69b4">self</font>):

* Method to create the initial body of the snake consisting of only 3 segments.
Their starting positions are stored in the global constant 'STARTING_POSITIONS', which is a list of tuples.

<font color="#ff8c00"> def </font> <font color="#daa520"> add_Segment</font>(<font color="#ff69b4">self <font color="#ff8c00">, </font></font> position):

* Method to add a new segment to the snake's body. Each segment will be square shaped, having white color. They won't draw while moving and their position will be the parameter passed to this function.

<font color="#ff8c00"> def </font> <font color="#daa520"> extend</font>(<font color="#ff69b4">self</font>):

* Method to extend the snake's body by adding a new segment to the position of the last segment of the snake's body.
Thus, a call to add_segment() is made where we pass position of the last segment as argument.
 
<font color="#ff8c00"> def </font> <font color="#daa520"> move</font>(<font color="#ff69b4">self</font>):

* We move the snake forward by:

            Taking last segment to the location of segment just before it.
            Taking 2nd last segment to the location of 3rd last segment.
            .
            .
            Taking 2nd segment to the location of 1st segment.
            Move 1st segment forward.

            Hence, we will loop through all the segments of segments of snake,
            Starting from end [len(snake_segments) - 1],
            Stopping at segment at index 0,
            Stepping forward by index -= 1.

<font color="#ff8c00"> def </font> <font color="#daa520"> up</font>(<font color="#ff69b4">self</font>):

* Moves the snake in upward direction(north) unless it is headed down(south). We do so by changing the heading of the head segment. All the other segments follow in lead.

<font color="#ff8c00"> def </font> <font color="#daa520"> down</font>(<font color="#ff69b4">self</font>):

* Moves the snake in downward direction(south) unless it is headed up(north). We do so by changing the heading of the head segment. All the other segments follow in lead.

<font color="#ff8c00"> def </font> <font color="#daa520"> left</font>(<font color="#ff69b4">self</font>):

* Moves the snake in left direction(west) unless it is headed right(east). We do so by changing the heading of the head segment. All the other segments follow in lead.

<font color="#ff8c00"> def </font> <font color="#daa520"> right</font>(<font color="#ff69b4">self</font>):

* Moves the snake in right direction(east) unless it is headed left(west). We do so by changing the heading of the head segment. All the other segments follow in lead.

food.py  
======

This file is responsible for all the food related activities. 
These are all defined in 
<font color="#ff4500"> class </font> Food which inherits from turtle method's Turtle class.

<font color="#ff8c00"> def </font> <font color="#ff1493"> __init__</font>(<font color="#ff69b4">self</font>):

* Constructor responsible for making food of the snake. It's green colored, circular shaped,
having 10px by 10px size, and is generated at a random (x, y) location within the range [-280, 280].

<font color="#ff8c00"> def </font> <font color="#daa520"> refresh</font>(<font color="#ff69b4">self</font>):

* Method to recreate the food of the snake at a random (x, y) location within the range of [-280, 280].

scoreboard.py  
======

This file is responsible for managing the scoreboard. 
All of this work has been done in  
<font color="#ff4500"> class </font> ScoreBoard which inherits from turtle method's Turtle class.


<font color="#ff8c00"> def </font> <font color="#ff1493"> __init__</font>(<font color="#ff69b4">self</font>):

* Constructor containing score attribute initialized to 0.
* The score will be printed in white color at location (0, 265).
* We will hide the score object otherwise we will see an arrow shaped turtle object just below where our score will be written. 

<font color="#ff8c00"> def </font> <font color="#daa520"> update_scoreboard</font>(<font color="#ff69b4">self</font>):

* Method to write the updated value of score on screen.

<font color="#ff8c00"> def </font> <font color="#daa520"> increase_score</font>(<font color="#ff69b4">self</font>):

* Method to increment the value of score by 1, clear the screen, and update the score board, by calling update_scoreboard().

<font color="#ff8c00"> def </font> <font color="#daa520"> game_over</font>(<font color="#ff69b4">self</font>):

* Method to print "GAME OVER" in red at the center of the screen.

main.py 
======

This is where our program's execution takes place. 

1. We start off by importing the 3 classes that we made above
and create their objects.

2. We also import time module and create a Screen object (from turtle module).

3. We set the screen's height, width, background color and title and turn it's animation off.

4. We set the screen animation off initially because we don't want to show
the starting segments of snake's body and our scoreboard take their respective place when
they move from middle of the screen to their respective positions. We will turn the animation on only
when they have taken their places.

5. We declare the keyboard listener methods for screen. Now, player will be able to move the snake left, right, up or down.

6. We now update the screen (turn on its animation) and add a 0.1 sec delay before we move the snake.

7. After moving the snake, we detect if there was collision of snake with food.
If yes, then the score will be incremented, food will be placed at new location and snake's body will be extended.

8. If the head of the snake collides with wall, game over will be printed and the game will end.

9. If the head of the snake collides with any segment in its body, game over will be printed and the game will end.

10. Points 6-9 will keep repeating until the game ends.

11. When the game ends, you can close the screen by clicking on it. 
