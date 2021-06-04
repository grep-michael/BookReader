from __future__ import annotations

class PdfXrefExtractor():
    def __init__(self,fileBytes) -> None:
        self.fileBytes = fileBytes
        self.xrefBytes = b'\x78\x72\x65\x66'
        self.trailerBytes = b'\x74\x72\x61\x69\x6C\x65\x72'
        self.startSearch = 0

    def getAllXrefSegments(self) -> list:
        segments = []
        while True:
            seg = self.extractNextXrefSegment()
            if len(seg.bytes) == 0:
                break
            else:
                segments.append(seg)
        return segments

    def returnNextXrefLocation(self) -> int:
        while True:
            possibleNextSeg = self.fileBytes.find(self.xrefBytes,self.startSearch)
            if possibleNextSeg == -1:
                return -1
            if self.fileBytes[possibleNextSeg-1] == int(0x0A) or self.fileBytes[possibleNextSeg-1] == int(0x0D):
                return possibleNextSeg
            self.startSearch = possibleNextSeg+1

    def extractNextXrefSegment(self) -> xrefSegment:
        start = self.returnNextXrefLocation()
        if start == -1 :
            return xrefSegment(b"")
        offset = start + 7
        xrefBytes = self.fileBytes[start:offset]
        while xrefBytes[-7:] != self.trailerBytes:
            offset += 1 
            xrefBytes = self.fileBytes[start:offset]
        self.startSearch = offset+1
        return xrefSegment(xrefBytes)



class xrefSegment():
    def __init__(self,bytes) -> None:
        self.bytes = bytes

