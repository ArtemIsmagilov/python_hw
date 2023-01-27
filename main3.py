ticket = input()
print('yes' if sum(int(i) for i in ticket[:3]) == sum(int(i) for i in ticket[3:]) else 'no')
