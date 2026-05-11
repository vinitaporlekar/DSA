class Codec:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])

            i = j

        return res


codec = Codec()

# test
encoded = codec.encode(["neet", "code"])
print("Encoded:", encoded)

decoded = codec.decode(encoded)
print("Decoded:", decoded)