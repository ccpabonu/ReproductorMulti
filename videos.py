import sys
from functools import partial
from PyQt5.QtCore import QEvent, QUrl, Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,
                             QWidget, QPushButton, QSlider,
                             QVBoxLayout)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

# Ruta del archivo.
A= "video.mp4"



class MainWindow(QMainWindow):

    
    def __init__(self, A):
        super().__init__()
        VIDEO_PATH = A

        # Controles principales para organizar la ventana.
        self.widget = QWidget(self)
        self.layout = QVBoxLayout()
        self.bottom_layout = QHBoxLayout()

        # Control de reproducción de video de Qt.
        self.video_widget = QVideoWidget(self)
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(
            QMediaContent(QUrl.fromLocalFile(VIDEO_PATH)))
        self.media_player.setVideoOutput(self.video_widget)

        # Botones
        self.play_button = QPushButton("Pausa", self)
        self.stop_button = QPushButton("Detener", self)

        # Deslizadores
        self.seek_slider = QSlider(Qt.Horizontal)
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(self.media_player.volume())
        self.seek_slider.sliderMoved.connect(self.media_player.setPosition)
        self.volume_slider.sliderMoved.connect(self.media_player.setVolume)
        self.media_player.positionChanged.connect(self.seek_slider.setValue)
        self.media_player.durationChanged.connect(
            partial(self.seek_slider.setRange, 0))

        # Acomodar controles en la pantalla.
        self.layout.addWidget(self.video_widget)
        self.layout.addLayout(self.bottom_layout)
        self.bottom_layout.addWidget(self.play_button)
        self.bottom_layout.addWidget(self.stop_button)
        self.bottom_layout.addWidget(self.volume_slider)
        self.layout.addWidget(self.seek_slider)

        # Eventos.
        self.play_button.clicked.connect(self.play_clicked)
        self.stop_button.clicked.connect(self.stop_clicked)
        self.media_player.stateChanged.connect(self.state_changed)

        # Se utiliza installEventFilter() para capturar eventos
        # del mouse en el control de video.
        self.video_widget.installEventFilter(self)

        # ventana.
        self.setWindowTitle("Reproductor de video")
        self.resize(800, 600)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Reproducir el video.
        self.media_player.play()

    def play_clicked(self):
        """
        Comenzar o resumir la reproducción.
        """
        if (self.media_player.state() in
                (QMediaPlayer.PausedState, QMediaPlayer.StoppedState)):
            self.media_player.play()
        else:
            self.media_player.pause()

    def stop_clicked(self):
        """
        Detener la reproducción.
        """
        self.media_player.stop()

    def state_changed(self, newstate):
        """
        Actualizar el texto de los botones de reproducción y pausa.
        """
        states = {
            QMediaPlayer.PausedState: "Resumir",
            QMediaPlayer.PlayingState: "Pausa",
            QMediaPlayer.StoppedState: "Reproducir"
        }
        self.play_button.setText(states[newstate])
        self.stop_button.setEnabled(newstate != QMediaPlayer.StoppedState)

    def eventFilter(self, obj, event):
        """
        Establecer o remover pantalla completa al obtener
        el evento MouseButtonDblClick.
        """
        if event.type() == QEvent.MouseButtonDblClick:
            obj.setFullScreen(not obj.isFullScreen())
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(A)
    window.show()
    sys.exit(app.exec_())
