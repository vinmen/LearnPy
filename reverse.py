# Reverse string using recursion.

def reverse(input):
	if len(input) == 1:
		return input
	else:
		return input[-1] + reverse(input[0:len(input) - 1])

if __name__ == "__main__":
	reverse("hello")
