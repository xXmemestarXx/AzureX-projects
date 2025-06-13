import os
import tempfile
import cv2
import numpy as np

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.graphics.texture import Texture
from kivy.uix.image import Image

import sudoku_solver


class SudokuApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)

        self.solve_button = Button(text="Solve Sudoku")
        self.solve_button.bind(on_press=self.capture_and_solve)
        self.layout.add_widget(self.solve_button)

        self.result_img = Image()
        self.layout.add_widget(self.result_img)

        return self.layout

    def capture_and_solve(self, instance):
        # Capture the frame from the camera
        texture = self.camera.texture
        size = texture.size
        pixels = texture.pixels
        frame = np.frombuffer(pixels, np.uint8).reshape(size[1], size[0], 4)
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Save temporarily to a temp file
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            temp_path = temp_file.name
            cv2.imwrite(temp_path, frame_bgr)

        try:
            # Call the refactored solver function
            solved_grid, solved_img_path = sudoku_solver.solve_image(temp_path)
            
            if solved_img_path and os.path.exists(solved_img_path):
                # Load the solved image and display it
                result = cv2.imread(solved_img_path)
                result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                tex = Texture.create(size=(result.shape[1], result.shape[0]), colorfmt='rgba')
                tex.blit_buffer(result.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
                self.result_img.texture = tex
            else:
                print("Sudoku solver failed or couldn't find a solution.")
                # Optionally show an error image or clear result_img texture
                self.result_img.texture = None
        finally:
            # Cleanup temp input image
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == '__main__':
    SudokuApp().run()
