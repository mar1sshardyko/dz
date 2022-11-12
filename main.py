# по коду с левой стороны сила света с правой сила тьмы (при чтении поймете)
import random
class Carry1:
    def __init__(self, name="Carry1",atribut=None, dengi=None):
        self.name = name
    def atribut1 (atribut_list1):
        atribut = random.choice(list(atribut_list1))
        sila = atribut_list1[atribut]["sila"]
        lovkost = atribut_list1[atribut]["lovkost"]
        intelekt = atribut_list1[atribut]["intelekt"]
        atribut = {"sila": {"power": 444, "lovkost": 222, "lntelekt":125},
                          "lovkost": {"power": 222, "lovkost": 444, "ntelekt": 125},
                          "intelekt": {"power": 125, "lovkost": 222, "ntelekt": 444}}

        def Dengi1(dengi_list1):
            dengi = random.choice(list(dengi_list1))
            dengi = dengi_list1[dengi]["dengi"]
            dengi = {"dengi1": {"dengi": 5000},
                     "dengi2": {"dengi": 12500},
                     "dengi3": {"dengu": 17500}}

class Carry2:
    def __init__(self, name="Carry2",atribut=None, dengi=None):
        self.name = name

    def atribut2( atribut_list2):
        atribut = random.choice(list(atribut_list2))
        sila = atribut_list2[atribut]["sila"]
        lovkost = atribut_list2[atribut]["lovkost"]
        intelekt = atribut_list2[atribut]["intelekt"]
        atribut = {"sila": {"power": 444, "lovkost": 222, "lntelekt":125},
                          "lovkost": {"power": 222, "lovkost": 444, "ntelekt": 125},
                          "intelekt": {"power": 125, "lovkost": 222, "ntelekt": 444}}

        def Dengi2 (dengi_list2):
            dengi = random.choice(list(dengi_list2))
            dengi = dengi_list2[dengi]["dengi"]
            dengi = {"dengi1": {"dengi": 5000 },
                       "dengi2": {"dengi": 12500},
                       "dengi3": {"dengu": 17500}}

# тут ошибка только в atr1 и atr2 де я сделал такую переменную для if алгоритмов для победы или нет по сути ёё нету
# там правильно я перепроверил 58 раз просто пайтон набухался xD
# тут ошибка только в atr1 и atr2 де я сделал такую переменную для if алгоритмов для победы или нет по сути ёё нету
# там правильно я перепроверил 58 раз просто пайтон набухался xD
# тут ошибка только в atr1 и atr2 де я сделал такую переменную для if алгоритмов для победы или нет по сути ёё нету
# там правильно я перепроверил 58 раз просто пайтон набухался xD
atr1 = atribut1()
atr2 = atribut2()

deng1 = Dengi1()
deng2 = Dengi2()

if atr1:
    atr1 = "sila"
    atr2 = "lovkost"
    print ("У кэрри сил света атрибут Сила, а у сил тьмы Ловкость")
elif atr1:
    atr1 = "sila"
    atr2 = "intelekt"
    print("У кэрри сил света атрибут Сила, а у сил тьмы Ловкость")
elif atr1:
    atr1 = "lovkost"
    atr2 = "sila"
    print("У кэрри сил света атрибут Ловкость, а у сил тьмы Сила")
elif atr1:
    atr1 = "lovkost"
    atr2 = "intelekt"
    print("У кэрри сил света атрибут Ловкость, а у сил тьмы Интелект")
elif atr1:
    atr1 = "intelekt"
    atr2 = "sila"
    print("У кэрри сил света атрибут Интелект, а у сил тьмы Сила")
elif atr1:
    atr1 = "intelekt"
    atr2 = "lovkost"
    print("У кэрри сил света атрибут Интелект, а у сил тьмы Ловкость")
elif atr1:
    atr1 = "sila"
    atr2 = "sila"
    print("У кэрри сил света атрибут Сила, а у сил тьмы тоже Cила")
elif atr1:
    atr1 = "lovkost"
    atr2 = "lovkost"
    print("У кэрри сил света атрибут Ловкость, а у сил тьмы тоже Ловкость")
elif atr1:
    atr1 = "intelekt"
    atr2 = "intelekt"
    print("У кэрри сил света атрибут Интелект, а у сил тьмы тоже Интелект")


    if deng1:
        deng1 = "dengi2"
        deng2 = "deng1"
        print("Победа сил Света!")
elif deng1:
    deng1 = "dengi3"
    deng2 = "dengi2"
    print("Победа сил Света!")
elif deng1:
    deng1 = "dengi3"
    deng2 = "dengi1"
    print("Победа сил Света!")
elif deng1:
    deng1 = "dengi1"
    deng2 = "dengi2"
    print("Победа сил Тьмы!")
elif deng1:
    deng1 = "dengi1"
    deng2 = "dengi3"
    print("Победа сил Тьмы!")
else:
    print("Долгая игра ( в доте нету ничьи)")
