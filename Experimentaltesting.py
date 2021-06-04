
xrefBytes = b'\x78\x72\x65\x66'

file = open("./TestData/Manifesto.pdf",'rb')
bytes = file.read()
start = bytes.find(xrefBytes)
print()
