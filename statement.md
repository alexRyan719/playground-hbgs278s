# Hello World

    def hello_world():

        # This is the classic "Hello World" program in Python. This will 
        # print whatever String (array of chars) you have between the single 
        # quotes ('') or double quotes ("")
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
        
# Control Flow

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

# Testing Control Flow

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

# Loops 

    def loops(n):
        #Loops are very useful when needing to do the same action 
        # multiple time (iterations). For loops are usually better when 
        # the amount of iterations is known and while loops are usually
        # better when the number of iterations is not known. 
        #
        # However, you can pretty much do any process (algorithm) with 
        # either style of loop. You can also use recursion.

        # Iterate through every char in a string
        test_str = "Hello World!"
        for char in test_str:
            print(char)

        # Indexes are used to keep track of what we're working with for
        # each iteration. With while loops, you have to manually change
        # the index. Be careful, infinite loops are created when a 
        # terminating condition is never met. IE the index never changes,
        # a count never changes, or whatever condition we decide for the 
        # loop. 
        index = 0
        while index < len(test_str):
        print(test_str[index])
        index += 1

        # In other languages, there are do while loops. However,
        # Python doesn't use them without some extra effort. 

        # To demonstrate recursion, we need to define a function. The 
        # concept is where we have a function that calls itself until
        # a condition is met. It's also easy to write infinite loops
        # with recursion

# Recursion

    def recurse_this(n):
        if n == -1:
            print(test_str[10 - n])
            print("This is the base case!")
        else:
            print(test_str[10 - n])
            #print("iteration: " + str(n))
            recurse_this(n-1)

        recurse_this(len(test_str))


# Main

    def main():
        test_control_flow()
        recurs_this(100)


    ### DUNDER CHECK ###
    if __name__ == "__main__":
    main()
