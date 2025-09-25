# Stack implementation using list
irembo_stack = []

# Push actions
irembo_stack.append("Start")
irembo_stack.append("Fill Form")
irembo_stack.append("Submit")

# Undo last action (pop)
irembo_stack.pop()

# Show remaining stack
print("Remaining actions in Irembo:", irembo_stack)