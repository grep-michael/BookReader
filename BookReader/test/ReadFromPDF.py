import unittest
import BookReader.main.pdfextractor.PDFxrefExtractor as pdf


class TestClass(unittest.TestCase):
    ManifestoFile = open('./TestData/Manifesto.pdf','rb')
    ManifestoExtractor = pdf.PdfXrefExtractor(ManifestoFile.read())
    
    
    def test_ExtractObjectCountManifesto(self):
        segments = self.ManifestoExtractor.getAllXrefSegments()
        self.assertEqual(2,len(segments))
        

