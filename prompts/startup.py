import misc
def pu():
    print '''Please choose a number
    
    1: Start
    2: Configure'''
    
    i = raw_input(misc.ps)
    
    if i == '1':
        return True
    elif i == '2':
        return True
    else:
        print 'No. Pick one of the numbers.'
        return False
return i
def pd():
    print '''Welcome aboard the Level Bus.
    How may we serve you today?

    1: Daily routine
    2: Something different
    3: Tell me LevelBus!'''

    k = raw_input(misc.ps)

    if k == '1':
        return True
    elif k == '2':
        return True
    elif k == '3':
        return True
    else:
        print 'Don\'t be silly now.'
	return False
return i
