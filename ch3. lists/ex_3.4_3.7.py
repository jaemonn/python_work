# ex_3.4
dinner_invites = ['alex', 'stewie', 'al', 'eli']
print(dinner_invites)

# ex_3.5
dinner_invites[0] = 'laurence'
print(dinner_invites)

# ex_3.6
print(f"Hello , we rented a bigger table")
dinner_invites.insert(0, 'anna')
dinner_invites.insert(2, 'margarita')
dinner_invites.append('michael')
message = f"Hello {dinner_invites}, welcome"
print(message)

# ex_3.7
message_2 = "Hello, I am sorry to tell you that we can only accomodate for two guests for the dinner"
dinner_invites.pop()
dinner_invites.pop()
dinner_invites.pop()
dinner_invites.pop()
dinner_invites.pop()
message_3 = f"Hello {dinner_invites[0].title()} and {dinner_invites[1].title()}, you're still invited"
print(message_3)
del dinner_invites[0] ,dinner_invites[0]
print(dinner_invites)