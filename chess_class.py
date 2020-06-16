class chess():
    def __init__(self,side,id,type,dp):
        self.type = 'chess'
        self.side = side
        self.type = type
        self.id = id
        self.dp = dp

# def find(self):
#     return(gp[self].type)
#
# # def adv_type(self):
# #     return(gp[self].type)
#
# gp = {}
#
# w_pawn_location = ['a2','b2','c2','d2','e2','f2','g2','h2']
# w_rook_location = ['a1','h1']
# w_knight_location = ['b1','g1']
# w_bishop_location = ['c1','f1']
# w_queen_location = ['d1']
# w_king_location = ['e1']
#
# for i in range(len(w_pawn_location)):
#     gp[w_pawn_location[i]] = chess('white',i,'p','pawn')
#
#
# for i in range(len(w_rook_location)):
#     gp[w_rook_location[i]] = chess('white',i,'r','rook')
#
# for i in range(len(w_knight_location)):
#     gp[w_knight_location[i]] = chess('white',i,'k','knight')
#
# for i in range(len(w_bishop_location)):
#     gp[w_bishop_location[i]] = chess('white',i,'b','bishop')
#
# gp[w_queen_location[0]] = chess('white',0,'q','queen')
# gp[w_king_location[0]] = chess('white',0,'k','king')
#
# # *********************************************
#
# b_pawn_location = ['a7','b7','c7','d7','e7','f7','g7','h7']
# b_rook_location = ['a8','h8']
# b_knight_location = ['b8','g8']
# b_bishop_location = ['c8','f8']
# b_queen_location = ['d8']
# b_king_location = ['e8']
#
# for i in range(len(w_pawn_location)):
#     gp[b_pawn_location[i]] = chess('black',i,'P','pawn')
#
#
# for i in range(len(w_rook_location)):
#     gp[b_rook_location[i]] = chess('black',i,'R','rook')
#
# for i in range(len(w_knight_location)):
#     gp[b_knight_location[i]] = chess('black',i,'K','knight')
#
# for i in range(len(w_bishop_location)):
#     gp[b_bishop_location[i]] = chess('black',i,'B','bishop')
#
# gp[b_queen_location[0]] = chess('black',0,'Q','queen')
# gp[b_king_location[0]] = chess('black',0,'K','king')
#
# i = 3
# list = ['a','b','c','d','e','f','g','h']
# while i < 7:
#     for y in range(len(list)):
#         gp[str(list[y]) + str(i)] = chess('na',0,'o','blank')
#     i += 1
#
#
# def print_chess():
#     print('a-b-c-d-e-f-g-h-~')
#     i = 8
#     while i > 0:
#         print(find('a' + str(i)), find('b' + str(i)), find('c' + str(i)), find('d' + str(i)), find('e' + str(i)),
#               find('f' + str(i)), find('g' + str(i)), find('h' + str(i)),str(i))
#         i -= 1
#
#     print('----------------')
#         # print('r k b q k b k r\n'
#         #       'p p p p p p p p\n'
#         #       'o o o o o o o o\n'
#         #       'o o o o o o o o\n'
#         #       'o o o o o o o o\n'
#         #       'o o o o o o o o\n'
#         #       'p p p p p p p p\n'
#         #       'r k b q k b k r')
#
# default = []
# for x in range(8):
#     for i in range(len(list)):
#         default.append(str(list[i])+str(x+1))
#
#

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []

gp = [a,b,c,d,e,f,g,h]
for i in range(8):
    while len(gp[i]) < 8:
        gp[i].append(chess('na',0,'blank','o'))

for i in range(8):
    gp[i][6] = chess('black',i,'pawn','P')
    gp[i][1] = chess('white',i,'pawn','p')
    if i == 0 or i == 7:
        gp[i][0] = chess('white',i,'rook','r')
        gp[i][7] = chess('black',i,'rook','R')
    if i == 1 or i == 6:
        gp[i][0] = chess('white',i,'knight','k')
        gp[i][7] = chess('black',i,'knight','K')
    if i == 2 or i == 5:
        gp[i][0] = chess('white',i,'bishop','b')
        gp[i][7] = chess('black', i, 'bishop', 'B')
    if i == 3:
        gp[i][0] = chess('white', i, 'queen', 'q')
        gp[i][7] = chess('black', i, 'queen', 'Q')
    if i == 4:
        gp[i][0] = chess('white', i, 'king', 'k')
        gp[i][7] = chess('black', i, 'king', 'K')


def print_gp():
    i = 7
    while i>=0:
        print(str(i+1),'|',a[i].dp,b[i].dp,c[i].dp,d[i].dp,e[i].dp,f[i].dp,g[i].dp,h[i].dp)
        i-=1
    print('*   a-b-c-d-e-f-g-h-')
    print('-----------------------------------------')

def locat(self): #input (a1) return an array of ['letter','number'] @ actual gp array
    let = self[0]
    num = int(self[1]) - 1
    return [let,num]

def find(self):   #returns object by giving an array of ['letter','number'] also known as locat()
    temp = (globals()[self[0]])[self[1]]
    return temp

def move(sta,end,sel,des):
    if des.side == sel.side:
        print('Cant move onto your own piece.')
    elif sel.type == 'pawn':
        if des.type == 'blank':
            if (sta[1] == 1) and (end[0] == sta[0]) and (end[1] - 1 == sta[1] or end[1] - 2 == sta[1]):
                (globals()[end[0]])[end[1]] = (globals()[sta[0]])[sta[1]]
                (globals()[sta[0]])[sta[1]] = chess('na',0,'blank','o')


