import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox


class AverageSpeedCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Avegage Speed Calculator")

        grid = QGridLayout()

        distance_label = QLabel("Enter Distance of your way")
        self.distance_line_edit = QLineEdit()

        self.choice = QComboBox()
        self.choice.addItems(['Km', 'Miles'])

        time_label = QLabel("Enter consumed Time (hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Average Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("sdd")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.choice, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate_speed(self):

        distance = float(self.distance_line_edit.text())
        consumed_time = float(self.time_line_edit.text())
        average = distance / consumed_time
        if self.choice.currentText() == 'Km':
            average = round(average, 2)
            self.output_label.setText(f"Average Speed is {average} km/h ")
        if self.choice.currentText() == 'Miles':
            average = round(average * 0.62137, 2)
            self.output_label.setText(f"Average Speed is {average} mph")



app = QApplication(sys.argv)
speed_calculator = AverageSpeedCalc()
speed_calculator.show()
sys.exit(app.exec())

