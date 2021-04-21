def main():

	while True:
		Test1Word = input("What's your name?: ")

		try:
			Test1Num = int(input("Please choose one of three presidential candidates: \n 1. Donald Trump \n 2. Joe Biden \n 3. Bernie Sanders \n"))

			if Test1Num >= 1 and Test1Num <= 3:
				print("Congratulations," , Test1Word, ", you have voted!")
			else:
				print("Please choose a valid option between 1 and 3, or this session will be closed\n\n")
				Test1Num = int(input("Please choose one of three presidential candidates: \n 1. Donald Trump \n 2. Joe Biden \n 3. Bernie Sanders \n"))
				if Test1Num >= 1 and Test1Num <= 3:
					print("Congratulations, You have voted")
				else:
					print("This session will close. Please ask election staff for assistance")

			
		except ValueError:
			print("Error! This is not a number. This session will close. Please ask election staff for assistance \n\n")



		break
main()