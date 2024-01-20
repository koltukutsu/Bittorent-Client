import unittest
from bencoding import Decoder, Encoder

class TestBencoding(unittest.TestCase):
    def test_decoder(self):
        decoder = Decoder(b'i3e')
        self.assertEqual(decoder.decode(), 3)

        decoder = Decoder(b'4:spam')
        self.assertEqual(decoder.decode(), b'spam')

        decoder = Decoder(b'l4:spam4:eggsi3ee')
        self.assertEqual(decoder.decode(), [b'spam', b'eggs', 3])

        decoder = Decoder(b'd3:cow3:moo4:spam4:eggse')
        self.assertEqual(decoder.decode(), {b'cow': b'moo', b'spam': b'eggs'})

    def test_encoder(self):
        encoder = Encoder(3)
        self.assertEqual(encoder.encode(), b'i3e')

        encoder = Encoder('spam')
        self.assertEqual(encoder.encode(), b'4:spam')

        encoder = Encoder(['spam', 'eggs', 3])
        self.assertEqual(encoder.encode(), b'l4:spam4:eggsi3ee')

        encoder = Encoder({'cow': 'moo', 'spam': 'eggs'})
        self.assertEqual(encoder.encode(), b'd3:cow3:moo4:spam4:eggse')

if __name__ == '__main__':
    unittest.main()