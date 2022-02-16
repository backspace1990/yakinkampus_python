import re

strings = "Hello my dear friend world"

patern = "e"

print(re.search(patern, strings))  # ilk eslesmeyi gosterir

objects = re.search(patern, strings)

print(objects.span())
for i in objects.__dir__():
    if i == 'span':
        print(re.search(patern, strings).span())
        break
    print(i)

print(50 * "*")
print(objects.start())
print(objects.end())
print(50 * "*")

for i in re.findall(patern, strings):
    print(i)

for i in re.finditer(patern, strings):
    print(i.span(), "\n", i.groups)

print(50 * "*")

###########################################################################
#  Ifade        Aciklama              Ornek             Patern            #
# ------------------------------------------------------------            #
#   \d -------> Rakam          -----> base42    ------> base\d\d          #
#   \w -------> Karakter       -----> R2-D2     ------> \w\w\w\w\w        #
#   \s -------> Bosluk         -----> Ping Pong ------> Ping\sPong        #
#   \D -------> Rakam degil    -----> base      ------> \D\D\D\D          #
#   \W -------> Karakter degil -----> R2D2      ------> \W\W\W\W          #
#   \S -------> Bosluk degil   -----> PingPong  ------> \S\S\S\S\S\S\S\S  #
# ----------------------------------------------------------------------- #
###########################################################################

prmr = "umit hi base4-2222 umi311231 - base42 my  telephone nomer - +79672827880"
patern2 = r"\d\d\d\d\d\d\d\d\d\d\d"
print(re.search(patern2, prmr))
print(100 * "*")

#####################################################################
#  Ifade          Aciklama              Ornek             Patern    #
# ----------------------------------------------------------------- #
#   {5}  -------> Adet            -----> aaaa     ------> \w{4}     #
#  {3,4} -------> veya            -----> abc      ------> \w{3,4}   #
#   {2,} -------> en az           -----> 3215732  ------> \d{2,}    #
#   *    -------> 0 ya da  fazla  -----> x        ------> \w?       #
#   +    -------> 1 ya da fazla   -----> Ahmet1   ------> \w+\d+    #
#   ?    -------> ya 1 ya hic     -----> Mura     ------> Murat?    #
# ----------------------------------------------------------------- #
#####################################################################


patern3 = r"\d{7,}"
patern4 = r"base\d{1}"
patern5 = r"base\d{1,2}"
patern6 = r"base\d*"
patern7 = r"umi?"
patern8 = r"umi\d+"

print("\npatern : 3 ---> ", re.search(patern3, prmr), "\npatern : 4 ---> ", re.search(patern4, prmr),
      "\n patern : 5 ---> ", re.search(patern5, prmr))
print("\npatern : 6 ---> ", re.search(patern6, prmr), "\npatern : 7 ---> ", re.search(patern7, prmr),
      "\npatern : 8 ---> ", re.search(patern8, prmr))
print(100 * "*")
############################


number1 = "Hi my numbers - 0537-8881111"
number2 = "Hi my numbers - 0501-8881111"
number3 = "Hi my numbers -  0543-8881111"
number4 = "Hi my numbers - 0523-8881111"
number5 = "Hi my numbers - 05da-8881111"


def gsm_operators(tel_no):
    paten_gsm = r"(\d{3,4})-(\d{7})"
    result = re.search(paten_gsm, tel_no)

    if result:
        gsm_code = result.groups()[0]
        if gsm_code.startswith("054"):
            return "Vodafone"
        elif gsm_code.startswith("0501") or gsm_code.startswith("0505") or gsm_code.startswith("0506"):
            return "AVEA"
        elif gsm_code.startswith("053"):
            return "Turkcell"
        else:
            return "Undefined operators gsm"
    else:
        return "Noting patern"


print(gsm_operators(number1))
print(gsm_operators(number2))
print(gsm_operators(number3))
print(gsm_operators(number4))
print(gsm_operators(number5))
print(100 * "*")

#######################################################################
#  Ifade           Aciklama             Ornek             Patern      #
# ------------------------------------------------------------------- #
#   |   ------->    veya         -----> slm       ------> selam|slm   #
#   ^   ------->   baslar        -----> Ahmet     ------> ^\w+        #
#   $   ------->   biter         -----> base42    ------> \d$         #
#   .   -------> herhangi        -----> abcdef    ------> .*          #
#   \   ------->   esc           -----> (not)     ------> \(w{3}\)    #
# ------------------------------------------------------------------- #
#######################################################################

cumle1 = "Merhaba ! :)"
cumle2 = "Selam "
cumle3 = "Slm"
cumle4 = "Birak bu isleri"
cumle5 = "Elbet bir gun!"
cumle6 = "asdsadbshiak"
cumle7 = ":)"


def msg_emoji(mesages):
    emoji = []

    possitive_pattern = r"(Merhaba|Selam|Slm|:\)+)"
    negative_pattern = r"(Birak|Elbet)"

    if re.search(possitive_pattern, mesages):
        emoji.append("Possitive")
    elif re.search(negative_pattern, mesages):
        emoji.append("Negative")
    else:
        emoji.append("Emoji is not defined")

    return emoji


cumleler = [cumle1, cumle2, cumle3, cumle4, cumle5, cumle6, cumle7]

for cumle in cumleler:
    print(cumle, '\t', msg_emoji(cumle))
