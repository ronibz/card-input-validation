card_number = input()
y = int(card_number)
i = len(str(y))

if i < 16 or i > 16:
	print("invalid input")


if i == 16:
	print("5XXX XXXX XXXX XXXX")
	if y >= 5000000000000000 and y <= 5999999999999999:
		print("thank you")
	else:
		print("invalid number")

