import sys
from PySide6.QtWidgets import QApplication

from bloco_de_notas.controller.bloco_de_notas_dao import DataBase
from bloco_de_notas.view.tela_principal import MainWindow

db = DataBase()
db.connect()
db.create_table_nota()
db.close_connection()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
