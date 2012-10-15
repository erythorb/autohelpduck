def conf():
    try:
         c = open('../config.tlb', 'r+')
    except IOError:
         print "Place an empty file in '/thelevelbus' named 'config.tlb'"
    print 'yep.'
