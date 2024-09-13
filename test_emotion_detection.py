import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def __emotion_sel(self, result):
        res = 0
        emo = ''

        for k, v in result.items():
            if v > res:
                emo = k
                res = v

        return emo
    
    def test_emotion_detection(self):

        resultj = emotion_detector('I am glad this happened')
        self.assertEqual(self.__emotion_sel(resultj), 'joy')

        resulta = emotion_detector('I am really mad about this')
        self.assertEqual(self.__emotion_sel(resulta), 'anger')

        resultd = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(self.__emotion_sel(resultd), 'disgust')

        results = emotion_detector('I am so sad about this')
        self.assertEqual(self.__emotion_sel(results), 'sadness')

        resultf = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(self.__emotion_sel(resultf), 'fear')

        return


if __name__ == '__main__':
    unittest.main()