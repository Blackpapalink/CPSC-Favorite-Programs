# Asks the user how many days has it been 
days = input('How many days has it been been since the semester started?')
days = int(days) % 30
voicemail = (2 ** days)

# Prints Dr. Edwards\' voicemail count
print('Dr. Edwards has ' + str(voicemail) + ' messages in her voicemail inbox!')
