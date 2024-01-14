class Codec:
    def __init__(self):
        self.encode_dict={}
        self.decode_dict = {}
        self.base = "http://tinyurl.com/"
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_dict:
            idx = self.base+str(len(self.encode_dict)+1)
            self.encode_dict[longUrl] = idx
            self.decode_dict[idx]=longUrl

        return self.encode_dict[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))