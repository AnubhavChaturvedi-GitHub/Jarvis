from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
import threading
import subprocess
import os
import pyautogui as gui

class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Jarvis UI')
        self.setGeometry(100, 100, 800, 600)

        # Set window attributes for transparency
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Microphone image (zoomed and larger)
        self.mic_label = QLabel(self)
        self.add_gif_to_label(self.mic_label, r"C:\Users\vlogp\Desktop\J.A.R.V.I.S\user_interface\MIKE2.gif", size=(1920, 770))  # Adjusted size
        self.mic_label.setAlignment(Qt.AlignCenter)
        self.mic_label.mousePressEvent = self.start_listening  # Connect mouse press event to start_listening

        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.mic_label, alignment=Qt.AlignCenter)

        # Add some margins and spacing
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        self.process = None
        self.is_listening = False

    def add_gif_to_label(self, label, gif_path, size=None):
        movie = QMovie(gif_path)
        label.setMovie(movie)
        self.movie = movie  # Save reference to the movie
        movie.start()

        if size:
            label.setFixedSize(*size)

        # Add drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        label.setGraphicsEffect(shadow)

    def start_listening(self, event):
        # Run the main file in a separate thread
        if not self.is_listening:
            self.is_listening = True
            subprocess_thread = threading.Thread(target=self.run_main_file)
            subprocess_thread.start()

    def run_main_file(self):
        try:
            # Get the directory where ui.py is located
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Specify the path to main.py based on the current directory
            path_to_main_py = os.path.join(current_directory, r"C:\Users\vlogp\Desktop\J.A.R.V.I.S\main.py")

            command = ["python", path_to_main_py]
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

            # Wait for the subprocess to complete
            self.process.wait()

            # Reset listening flag
            self.is_listening = False

        except subprocess.CalledProcessError as e:
            # Handle subprocess errors
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    gui.hotkey("win","d")
    app = QApplication([])

    jarvis_ui = JarvisUI()
    jarvis_ui.showFullScreen()

    app.exec_()
