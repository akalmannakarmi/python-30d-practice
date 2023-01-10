# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(full_stack.index("Redux")+1,"SQL")
full_stack.insert(full_stack.index("Redux")+1,"Python")
print(front_end)
print(full_stack)