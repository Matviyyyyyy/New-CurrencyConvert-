
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from forex_python.converter import CurrencyRates
from  PyQt5.QtGui import QPixmap

c = CurrencyRates()
app = QApplication([])
win_card = QWidget()
win_card.setWindowTitle('Конвертор валют') 
win_card.resize(400, 400)

app.setStyleSheet("""
        QWidget {
            background: #061c3b;
            border-radius: 11px;    

        }
        
        QPushButton{
            background: #8f7efc;
            color: #ffffff;
            border-radius: 11px;
            min-width: 6em;    
            min-height: 2em;
            font-family: Arial;
            font: bold 18px;      
        }
        
        QLineEdit{
            background-color: ;
            max-width: 20em;
            max-height: 7em;
            font-family: Arial;
            font: bold 18px;
            border-color: beige;
            color:#ff0505;
            
        }

"""
)

im = QPixmap("D:\\Projects\\unnamed (8).png")
label = QLabel()
label.setPixmap(im) 

oneline_edit = QLineEdit()
oneline_edit.setPlaceholderText("From which currency")
twoline_edit = QLineEdit()
twoline_edit.setPlaceholderText("In what currency")
threeline_edit = QLineEdit()
threeline_edit.setPlaceholderText("Result count")
threeline_edit.setReadOnly(True) 
fiveline_edit = QLineEdit()
fiveline_edit.setPlaceholderText("Count of currency")

button = QPushButton("Convert")

ver_line = QVBoxLayout()
ver_line.addWidget(label)
ver_line.addWidget(oneline_edit)
ver_line.addWidget(twoline_edit)
ver_line.addWidget(fiveline_edit)
ver_line.addWidget(threeline_edit)

ver_line.addWidget(button)

def convert():
    withsomething = oneline_edit.text()
    getrate = twoline_edit.text()
    count = int(fiveline_edit.text())
    rate = c.get_rate(withsomething, getrate)
    result = (rate * count)
    threeline_edit.setText(str(result))

button.clicked.connect(convert)
win_card.setLayout(ver_line)
win_card.show()
app.exec_()