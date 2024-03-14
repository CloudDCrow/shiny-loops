import unittest
import tkinter as tk
from unittest.mock import patch
from shiny_loops import ShinyLoops


class TestShinyLoops(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = ShinyLoops(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('shiny_loops.custom_loops.eevee_loop')
    def test_start_auto_loop_eevee(self, mock_eevee_loop):
        self.app.start_auto_loop('eevee')
        mock_eevee_loop.assert_called_once()

    @patch('shiny_loops.custom_loops.aero_loop')
    def test_start_auto_loop_aero(self, mock_aero_loop):
        self.app.start_auto_loop('aero')
        mock_aero_loop.assert_called_once()

    @patch('shiny_loops.custom_loops.starter_loop')
    def test_start_auto_loop_starter(self, mock_starter_loop):
        self.app.start_auto_loop('starter')
        mock_starter_loop.assert_called_once()

    @patch('shiny_loops.custom_loops.route1_loop')
    def test_start_auto_loop_route1(self, mock_route1_loop):
        self.app.start_auto_loop('route1')
        mock_route1_loop.assert_called_once()

    @patch('shiny_loops.custom_loops.shiny_test')
    def test_start_auto_loop_test(self, mock_shiny_test):
        self.app.start_auto_loop('test')
        mock_shiny_test.assert_called_once()


if __name__ == '__main__':
    unittest.main()
