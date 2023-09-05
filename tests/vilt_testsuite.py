"""
This module contains the test suite for the VisuaLlama application.

Author:
    Daemon 'Daethyra' Carino
    
LICENSE: 
    Affero GNU GPL v3.0
"""

import unittest
from vilt_power import VILTChatbotModule, get_prediction

class TestVILTChatbotModule(unittest.TestCase):

    def setUp(self):
        self.vilt_module = VILTChatbotModule()

    def test_initialization(self):
        self.assertIsNotNone(self.vilt_module.processor, "Processor should not be None.")
        self.assertIsNotNone(self.vilt_module.model, "Model should not be None.")

    def test_load_image(self):
        self.assertIsNotNone(self.vilt_module.load_image('sample_image.jpg'), "Image loading failed.")
        self.assertIsNone(self.vilt_module.load_image('invalid_path.jpg'), "Invalid image path should return None.")
        
    def test_predict_answer(self):
        result = get_prediction('local_image.jpg', 'What color is the sky?')
        self.assertNotEqual(result.get('error'), 'An error occurred during prediction.', 'Prediction should not fail.')
        
    def test_invalid_prediction(self):
        result = get_prediction('invalid_path.jpg', 'What color is the sky?')
        self.assertEqual(result.get('error'), 'An error occurred during prediction.', 'Prediction should fail for invalid image.')

if __name__ == '__main__':
    unittest.main()
