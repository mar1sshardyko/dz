# по коду с левой стороны сила света с правой сила тьмы (при чтении поймете)
import random
class Carry1:
    def __init__(self, name="Carry1",atribut=None, dengi=None):
        self.name = name
        self.atribut = atribut
        self.dengi = dengi

    def get_atribute(self, atribut_list1):
        self.atribut = random.choice(list(atribut_list1))
        self.sila = atribut_list1[self.atribut]["sila"]
        self.lovkost = atribut_list1[self.atribut]["lovkost"]
        self.intelekt = atribut_list1[self.atribut]["intelekt"]
        atribut = {"sila": {"power": 444, "lovkost": 222, "lntelekt":125},
                          "lovkost": {"power": 222, "lovkost": 444, "ntelekt": 125},
                          "intelekt": {"power": 125, "lovkost": 222, "ntelekt": 444}}

        def get_dengi(self, dengi_list1):
            self.dengi = random.choice(list(dengi_list1))
            self.dengi = dengi_list1[self.dengi]["dengi"]
         dengi = {"dengi1": {"dengi": 5000 },
                       "dengi2": {"dengi": 12500},
                       "dengi3": {"dengu": 17500}}

class Carry2:
    def __init__(self, name="Carry1",atribut=None, dengi=None):
        self.name = name
        self.atribut = atribut
        self.dengi = dengi

    def get_atribute(self, atribut_list2):
        self.atribut = random.choice(list(atribut_list2))
        self.sila = atribut_list2[self.atribut]["sila"]
        self.lovkost = atribut_list2[self.atribut]["lovkost"]
        self.intelekt = atribut_list2[self.atribut]["intelekt"]
        atribut = {"sila": {"power": 444, "lovkost": 222, "lntelekt":125},
                          "lovkost": {"power": 222, "lovkost": 444, "ntelekt": 125},
                          "intelekt": {"power": 125, "lovkost": 222, "ntelekt": 444}}

        def get_dengi(self, dengi_list2):
            self.dengi = random.choice(list(dengi_list2))
            self.dengi = dengi_list2[self.dengi]["dengi"]
         dengi = {"dengi1": {"dengi": 5000 },
                       "dengi2": {"dengi": 12500},
                       "dengi3": {"dengu": 17500}}

def win_or_no:
    if
 atribut_list1 = "sila"
                        and atribut_list2 ="lovkost"
    print ("У Кэрри сил света атрибут Сила, а у сил тьмы Ловкость ")
    if
        atribut_list1 = "lovkost"
                        and atribut_list2 ="sila"
    print ("У Кэрри сил света атрибут Ловкость, а у сил тьмы Сила ")
    if
        atribut_list1 = "intelekt"
                        and  atribut_list2 ="sila"
    print ("У Кэрри сил света атрибут Интелект, а у сил тьмы Сила ")
    if
        atribut_list1 = "sila"
                        and atribut_list2 ="sila"
    print ("У Кэрри сил света атрибут Сила, а у сил тьмы тоже Сила ")
    if
        atribut_list1 = "intelekt"
                        and atribut_list2 ="lovkost"
    print ("У Кэрри сил света атрибут Интелект, а у сил тьмы Ловкость ")
    if
    atribut_list1 = "intelekt"
                    and atribut_list2 ="intelekt"
    print ("У Кэрри сил света атрибут Интелект, а у сил тьмы тоже Интелект")
    if
        atribut_list1 = "lovkost"
                        and atribut_list2 ="lovkost"
    print ("У Кэрри сил света атрибут Ловкость, а у сил тьмы тоже Ловкость ")
    if
    atribut_list1 = "intelekt"
                    and atribut_list2 ="lovkost"
    print ("У Кэрри сил света атрибут Интелект, а у сил тьмы Ловкость ")
    wait (2)
    if
        dengi_list1 = "dengi2"
                      and dengi_list2 = "dengi1"
    print ('Победа сил Света')
    if
        dengi_list1 = "dengi3"
                      and dengi_list2 = "dengi1"
    print ('Победа сил Света')
    if
    dengi_list1 = "dengi1"
                  and dengi_list2 = "dengi3"
    print ('Победа сил Тьмы')
    if
        dengi_list1 = "dengi2"
                      and dengi_list2 = "dengi3"
    print ('Победа сил Тьмы'')
           else:
    print ("Долгая игра(в оригинальной игре нету ничьи"))
