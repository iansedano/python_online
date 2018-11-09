'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

def week_day():
    print('type in a number for the weekday')
    usr_num = int(input())
    if usr_num < 8:
        if usr_num < 7:
            if usr_num < 6:
                if usr_num < 5:
                    if usr_num < 4:
                        if usr_num < 3:
                            if usr_num < 2:
                                if usr_num < 1:
                                    print('other')
                                else:
                                    print('Monday')
                            else:
                                print('Tuesday')
                        else:
                            print ('Wednesday')
                    else:
                        print('Thursday')
                else:
                    print('Friday')
            else:
                print('Saturday')
        else:
            print('Sunday')
    else:
        print('other')
