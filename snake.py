from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.snake_segments.append(new_snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):

        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            # Save the X-coordinate of the segment before the current segment in new_x.
            new_x = self.snake_segments[seg_num - 1].xcor()

            # Save the Y-coordinate of the segment before the current segment in new_y.
            new_y = self.snake_segments[seg_num - 1].ycor()

            # Current segment will goto the position of segment just before it.
            # Eg: segment 3 will goto segment 2's location.
            self.snake_segments[seg_num].goto(new_x, new_y)

        # Move the first segment forward by 20 units.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

