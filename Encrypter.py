from random import randint

symbols = "! @ # $ % ^ & *".split(" ")

li = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)] + symbols

li_old = [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)]


def get_old(v: int):
    return li_old[v % len(li_old)]


def get(v: int):
    return li[v % len(li)]


def get_index(e):
    for i in range(0, len(li)):
        if e == li[i]:
            return i


class Encrypter:
    keys = []


    def get3(self, i, r1, r2, l):
        x = i

        for j in range(0, len(self.keys), 5):
            x += (r1 + self.key) * (self.keys[j] - r2)
            x -= self.keys[j + 1] * (self.key - l)
            x += (self.keys[j + 2] + (self.key * r1)) * len(self.keys)
            x -= (self.keys[j + 3] + l) * self.keys[j + 4]

        x += l + r2



        return li[x % len(li)]
    

    def get3_o(self, i, r1, r2, l):
        x = i

        x -= (l + r2)

        for j in range(0, len(self.keys), 5):
            x += (self.keys[j + 3] + l) * self.keys[j + 4]
            x -= (self.keys[j + 2] + (self.key * r1)) * len(self.keys)
            x += self.keys[j + 1] * (self.key - l)
            x -= (r1 + self.key) * (self.keys[j] - r2)

            
        
        return li[int(x) % len(li)]

    


    def initKeys(self, key_path: str):
        f = open(key_path)

        s = f.read()

        for t in s:
            self.keys.append(int(t) + self.key)


    def __init__(self, key: str, key_path: str):
        a = 0
        for i in key:
            a += ord(i)
        self.key = a * len(key) + 1
        
        self.initKeys(key_path)



    def encrypt(self, text: str, r1: int = -1, r2: int = -1):
        if r1 == -1:
            r1 = randint(0, len(li) - 1)
        if r2 == -1:
            r2 = randint(0, len(li) - 1)
        
        result = get(r1)

        for j in range(0, len(text)):
            t = text[j]
            i = get_index(t)
            if not i:
                result += t
                continue
            result += self.get3(i, r1, r2, j + 1)
        
        result += get(r2)


        return result, r1, r2

    def decrypt(self, text: str):

        # Encrypt 1
        result1 = ""
        if text.lower() == text:  # it means using old method
            for i in range(0, len(text)):
                if li_old.__contains__(text.lower()[i]):
                    result1 += get_old(li_old.index(text.lower()[i]) - self.key - i)
                else:
                    result1 += text[i]


        # Encrypt 2
        result2 = ""
        r1 = get_index(text[0])
        r2 = get_index(text[len(text) - 1])
        for i in range(1, len(text) - 1):
            t = text[i]
            j = get_index(t)
            if not j:
                result2 += t
                continue
            result2 += get(j - r1 - self.key + r2 - i + 1)


        # Encrypt 3
        result3 = ""
        for i in range(1, len(text) - 1):
            t = text[i]
            j = get_index(t)
            if not j:
                result3 += t
                continue
            result3 += self.get3_o(j, r1, r2, i)
        

        return result1, result2, result3
