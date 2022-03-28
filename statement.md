
def hello_world():
    #!/usr/bin/env python3

    print('Hello World!')

    # Formatting is a major part of problem solving with code. String
    # manipulation can be done a few ways in python
    print("Hello! " * 3)

    # Slicing is where you target or work with only parts of a string.
    # To do this, use square brackets ([]). Within the square 
    # brackets you can set the start, stop, and step. Or in other 
    # words, the starting point, ending point, and how much to count # by
    test_string = "Hello World!"
    print(test_string[1:6])

    # Print every other letter
    print(test_string[::2])

    # Reverse the string
    print(test_string[::-1])

    # Print single char at a certain index 
    print(test_string[0])

    # This also works backwards with a negative index
    print(test_string[-1])
    print(test_string[-5])

    # Set the start point as the fifth character from the end
    print(test_string[-5:])
    print(test_string[-10:-3])

def control_flow(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

def test_control_flow():
  print(control_flow(1000000))
  print(control_flow(95))
  print(control_flow(90))
  print(control_flow(89))
  print(control_flow(85))
  print(control_flow(75))
  print(control_flow(65))
  print(control_flow(59))
  print(control_flow(0))
  print(control_flow(-1000))

def main():
    test_control_flow()


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
