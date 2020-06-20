from chess_class import *
# for key,values in gp.items():
#     print(key,values.name,values.side)

# print_chess()
# # print(default)
# turn = 1
# while True:
#     if turn % 2 == 1:
#         inp = input('[White] Select.\n')
#         if gp[inp].type == 'o':
#             print('Nothing is selected')
#         elif gp[inp].side == 'white':
#             print(str(gp[inp].side),str(gp[inp].dp),'at',str(inp),'has been selected.')
#             fin = input('Destination?\n')
#             if gp[fin].type == 'o':
#                 gp[fin] =  chess(gp[inp].side,gp[inp].id,gp[inp].type,gp[inp].dp)
#                 gp[inp] = chess('na', 0, 'o', 'blank')
#                 print('Done.')
#                 turn +=1
#             elif gp[inp].side != gp[fin].side:
#                 print(str(gp[fin].side),str(gp[fin].dp),'at',str(fin),'has been taken.')
#                 gp[fin] = chess(gp[inp].side, gp[inp].id, gp[inp].type, gp[inp].dp)
#                 gp[inp] = chess('na', 0, 'o', 'blank')
#                 turn +=1
#             else:
#                 print('You cant take your own chess.')
#         else:
#             print('Its not your turn.')
#     elif turn % 2 == 0:
#         inp = input('[Black] Select.\n')
#         if gp[inp].type == 'o':
#             print('Nothing is selected')
#         elif gp[inp].side == 'black':
#             print(str(gp[inp].side),str(gp[inp].dp),'at',str(inp),'has been selected.')
#             fin = input('Destination?\n')
#             if gp[fin].type == 'o':
#                 gp[fin] =  chess(gp[inp].side,gp[inp].id,gp[inp].type,gp[inp].dp)
#                 gp[inp] = chess('na', 0, 'o', 'blank')
#                 print('Done.')
#                 turn +=1
#             elif gp[inp].side != gp[fin].side:
#                 print(str(gp[fin].side),str(gp[fin].dp),'at',str(fin),'has been taken.')
#                 gp[fin] = chess(gp[inp].side, gp[inp].id, gp[inp].type, gp[inp].dp)
#                 gp[inp] = chess('na', 0, 'o', 'blank')
#                 turn +=1
#             else:
#                 print('You cant take your own chess.')
#         else:
#             print('Its not your turn.')
#
#     print_chess()

z = input('Single player or Multi-player?[s/m]')
if z  == 'm':
    while True:
        print_gp()
        st = input('[ ? ] Select\n')
        selected = find(locat(st))
        print(selected.type)
        dt = input('[ ? ] Destination\n')
        destination = find(locat(dt))
        move(locat(st),locat(dt),selected,destination)



