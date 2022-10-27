import pyautogui as pya
class AspectRatio:
    def __init__(self):
        super(AspectRatio, self).__init__()
        self.whidth = pya.size().width
        self.heigth = pya.size().height
        self.aspec_ratio =  self.whidth/ self.heigth
        self.zapmax = False
        self.zapMid = False
        self.max1366= False
    def verAspectRatio(self):
        return self.aspec_ratio

    def posBntCriarContato(self):
        x = 85
        y = 175
        if self.aspec_ratio <= 4/3:
            if self.whidth < 1024:
                x=705
                y=530
            else:
                x=923
                y=693
        return x,y

    def posBtnCriarContato2(self):
        x = 85
        y = 175
        if self.aspec_ratio <= 4 / 3:
            if self.whidth < 1024:
                x = 564
                y = 481
            else:
                x = 780
                y = 643
        return x, y

    def posCampoNome(self):
        #posicaoX = 413
        #posicaoY = 375
        x = 413
        y = 375
        if self.aspec_ratio <= 4 / 3:
            if self.whidth < 1024:
                x = 111
                y = 414
            else:
                x = 142
                y = 382
        return x, y

    def posCampoTel(self):
        x = 510
        y = 632
        if self.aspec_ratio <= 4 / 3:
            x = 230
            y = 634
            if self.whidth < 1024:
                x = 183
                y = 277


        return x, y

    def posSalvar(self):
        #posicaoX = 1196
        #posicaoY = 303
        x = 1196
        y = 303
        if self.aspec_ratio <= 4 / 3:
            x = 911
            y = 304
            if self.whidth < 1024:
                x = 682
                y = 167


        return x, y

    def posBtnVoltar(self):
        x = 19
        y = 174
        if self.whidth < 1024:
            x = 24
            y = 166

        return x, y

    def posBtnNovaConverssaZap(self):
        x = 308
        y = 104
        if self.whidth < 1024:
            x= 250
            y = 101

        return x,y

    def posBtnNovoGrupoZap(self):
        x= 40
        y= 264
        if self.aspec_ratio < 4/3:
            x= 39
            y=268
            if self.whidth < 1024:
                x= 34
                y = 271

        return x,y

    def posNCZgrupoContato(self):
        x=44
        y=227
        #if self.whidth < 1024:
         #   x = 41
          #  y = 227

        return x,y

    def posContatoZap(self):
        x = 39
        y = 317
        if self.whidth < 1024:
            if self.zapMid:
                y = 390
            elif self.zapmax:
                y = 415
        elif self.whidth > 1024:

            if self.max1366:
                y= 450
            elif self.zapMid:
                y = 360
            elif self.zapmax:
                y = 415

        return  x,y

    def posBtnConfirmarZap(self):
        x= 195
        y = 665
        if self.whidth < 1024:
            x = 167
            y = 515

        return x,y

    def confirmarConvite(self):
        x = 746
        y = 451

        return x,y

    def changeMax(self, i):

        if i >= 7 and self.whidth < 1024:
            self.zapmax = True
        elif(i >= 7 and self.whidth > 1024):
            self.zapmax = True
        return

    def changeMid(self, i):

        if i > 4 and i < 7 :
            self.zapMid= True


        return

    def chanceMax1366(self, i):
        if i > 11:
            self.max1366 = True;