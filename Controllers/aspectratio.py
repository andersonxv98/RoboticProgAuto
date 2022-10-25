import pyautogui as pya
class AspectRatio:
    def __init__(self):
        super(AspectRatio, self).__init__()
        self.whidth = pya.size().width
        self.heigth = pya.size().height
        self.aspec_ratio =  self.whidth/ self.heigth

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

        return x,y

    def posBtnNovoGrupoZap(self):
        x= 40
        y= 264

        return x,y

    def posNCZgrupoContato(self):
        x=44
        y=227

        return x,y

    def posContatoZap(self):
        x=39
        y= 317

        return  x,y

    def posBtnConfirmarZap(self):
        x= 195
        y = 665

        return x,y

    def confirmarConvite(self):
        x = 746
        y = 451

        return x,y