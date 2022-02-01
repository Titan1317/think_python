import turtle


def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.fd(length*n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2*angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length*n)

bob = turtle.Turtle()
length = 10
n = 2
draw(bob, length, n)

stack_diagram:

	__main__ --> bob -> turtle.Turtle()
		     length -> 10
		     n -> 2

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 2

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 1

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 0

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 0

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 1

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 0

	draw	 --> t -> turtle.Turtle()
		 --> length -> 10
		 --> n -> 0


