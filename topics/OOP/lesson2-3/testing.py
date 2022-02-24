def menu(options):
	prompt = '\n'.join([str(i+1) + ' - ' + options[i] for i in range(0, len(options))])
	print(prompt)

	user_input = input("Enter a valid choice: ")
	while user_input not in [str(i+1) for i in range(0, len(options))]:
		user_input = input("Enter a valid choice: ")
	
	return options[int(user_input)-1]

menu(['A', 'B', 'C', 'D'])