
class chess():
    def __init__(self,side,id,type,dp):
        self.type = 'chess'
        self.side = side
        self.type = type
        self.id = id
        self.dp = dp

class test():
    def __init__(self,sta,end,obj,des_obj):
        self.move = False
        self.take = False
        list_move = []
        list_take = []
        if obj.type == 'pawn' and obj.side == 'white':
            if get_glo(sta[0],sta[1] + 1).type == 'blank':
                list_move.append(get_glo(sta[0],sta[1] + 1))
            if sta[1] == 1 and get_glo(sta[0],sta[1] + 2).type == 'blank':
                list_move.append(get_glo(sta[0], sta[1] + 2))

            if glo_x(sta[0],'+',1,sta[1] + 1).side != (get_glo(sta[0],sta[1]).side and 'blank'):
                list_take.append(glo_x(sta[0],'+',1,sta[1] + 1))
            try:
                if glo_x(sta[0],'-',1,sta[1] + 1).side != (get_glo(sta[0],sta[1]).side and 'blank'):
                    list_take.append(glo_x(sta[0],'-',1,sta[1] + 1))
            except:
                pass
            finally:
                if des_obj in list_move:
                    self.move = True
                if des_obj in list_take:
                    self.take = True
        if obj.type == 'pawn' and obj.side == 'black':
            if get_glo(sta[0], sta[1] - 1).type == 'blank':
                list_move.append(get_glo(sta[0], sta[1] - 1))
            if sta[1] == 6 and get_glo(sta[0], sta[1] - 2).type == 'blank':
                list_move.append(get_glo(sta[0], sta[1] - 2))

            if glo_x(sta[0], '+', 1, sta[1] - 1).side != (get_glo(sta[0], sta[1]).side and 'blank'):
                list_take.append(glo_x(sta[0], '+', 1, sta[1] - 1))
            try:
                if glo_x(sta[0], '-', 1, sta[1] - 1).side != (get_glo(sta[0], sta[1]).side and 'blank'):
                    list_take.append(glo_x(sta[0], '-', 1, sta[1] - 1))
            except:
                pass
            finally:
                if des_obj in list_move:
                    self.move = True
                if des_obj in list_take:
                    self.take = True
        if obj.type == 'bishop':
            i = 1
            while glo_x(sta[0],'-',i,sta[1] + i).type == 'blank':   # left up to go [x -][y +]
                list_move.append(glo_x(sta[0],'-',i,sta[1] + i))
                i +=1
            if glo_x(sta[0],'-',i,sta[1] + i).side != get_glo(sta[0],sta[1]).side:
                list_take.append(glo_x(sta[0],'-',i,sta[1] + i))
            i = 1
            while glo_x(sta[0],'+',i,sta[1] + i).type == 'blank':   # right up to go [x +][y +]
                list_move.append(glo_x(sta[0],'+',i,sta[1] + i))
                i += 1
            if glo_x(sta[0],'+',i,sta[1] + i).side != get_glo(sta[0],sta[1]).side:
                list_take.append(glo_x(sta[0],'+',i,sta[1] + i))
            i = 1
            while glo_x(sta[0], '-', i, sta[1] - i).type == 'blank':  # left down to go [x -][y -]
                list_move.append(glo_x(sta[0], '-', i, sta[1] - i))
                i += 1
            if glo_x(sta[0], '-', i, sta[1] - i).side != get_glo(sta[0], sta[1]).side:
                list_take.append(glo_x(sta[0], '-', i, sta[1] - i))
            i = 1
            while glo_x(sta[0], '+', i, sta[1] - i).type == 'blank':  # left down to go [x +][y -]
                list_move.append(glo_x(sta[0], '+', i, sta[1] - i))
                i += 1
            if glo_x(sta[0], '+', i, sta[1] - i).side != get_glo(sta[0], sta[1]).side:
                list_take.append(glo_x(sta[0], '+', i, sta[1] - i))
            if des_obj in list_move:
                self.move = True
            if des_obj in list_take:
                self.take = True






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


def glo_x(self,arth,num,y):   #enter self as 'x', + / - as arth, num as amount of number to add or subtract, y as int(y) to return the calculated object
    if arth == '+':
        try:
            return gp[gp.index(globals()[self]) + num][y]
        except :
            return chess('none','none','ignore','none')
    elif arth == '-':
        try:
            return gp[gp.index(globals()[self]) - num][y]
        except :
            return chess('none','none','ignore','none')

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

def get_glo(po1,po2):
    try:
        return (globals()[po1])[po2]
    except KeyError:
        pass

def dp_str(obj,sta,end):
    print('[ OK ]',obj.side,obj.type,str(sta[0])+str(sta[1] + 1),' moved to',str(end[0])+str(end[1] + 1))

def tk(obj,end):
    print('[ OK ]',str(obj.side) + ' ' + str(obj.type) + ' @ ' + str(end[0]) + str(end[1] + 1 ) + ' will be taken.')

def move(sta,end,obj,des_obj):
    if des_obj.side == obj.side:
        print('Cant move onto your own piece.')
    else:
        temp = test(sta,end,obj,des_obj)
        if temp.move ==  True:
            (globals()[end[0]])[end[1]] = get_glo(sta[0], sta[1])
            (globals()[sta[0]])[sta[1]] = chess('na',0,'blank','o')
            dp_str(obj, sta, end)
        elif temp.move == False:
            print('[ ! ]Cant move to required destination.')
        if temp.take == True:
            (globals()[end[0]])[end[1]] = get_glo(sta[0], sta[1])
            (globals()[sta[0]])[sta[1]] = chess('na', 0, 'blank', 'o')
            tk(des_obj,end)



