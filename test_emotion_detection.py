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

        resultj = emotion_detector('I am glad this happened')
        self.assertEqual(self.__emotion_sel(resultj), 'joy')

        resultj = emotion_detector('I am glad this happened')
        self.assertEqual(self.__emotion_sel(resultj), 'joy')

        resultj = emotion_detector('I am glad this happened')
        self.assertEqual(self.__emotion_sel(resultj), 'joy')

        resultj = emotion_detector('I am glad this happened')
        self.assertEqual(self.__emotion_sel(resultj), 'joy')

        

        return

'''
	
I am really mad about this	anger
I feel disgusted just hearing about this	disgust
I am so sad about this	sadness
I am really afraid that this will happen	fear
'''


if __name__ == '__main__':
    unittest.main()