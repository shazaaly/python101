def dance():
    # Some fancy dance moves
    # ...
    raise ValueError("Oops! Jack's dance moves are too complex for the robot.")


try:
    dance()
except ValueError as e:
    print("Haha! The robot couldn't keep up with Jack's dance moves!")
