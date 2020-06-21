from chess_class import *
import os
# for key,values in gp.items():
#     print(key,values.name,values.side)

z = input('Single player or Multi-player?[s/m]')
if z  == 'm':
    while True:
        print_gp()
        st = input('[ ? ] Select\n')
        selected = find(locat(st))
        if selected.type == 'blank':
            print("[ ! ]Invalid select @ {}{}".format(locat(st)[0],locat(st)[1] + 1))
        else:
            print('[ OK ]',selected.type,'@',str(locat(st)[0])+str(locat(st)[1] + 1),'has been selected.')
            dt = input('[ ? ] Destination\n')
            destination = find(locat(dt))
            move(locat(st),locat(dt),selected,destination)
        input('[ Await ]type anything to clear screen.')
        os.system('cls')


