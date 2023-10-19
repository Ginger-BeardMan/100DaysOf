
with open('./Input/Names/invited_names.txt') as roster:
    names = roster.readlines()
  
    for guest in names:
        
        with open('./Input/Letters/starting_letter.txt') as letter:
            current_letter = letter.read()
            final_letter = current_letter.replace('[name]', guest.strip('\n'))
            

            with open(f'./Output/ReadyToSend/{guest}_invitation.txt', 'w') as f:
                f.write(final_letter)
