print('Aplikacje bazodanowe')

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QGridLayout,
    QWidget,
    QPushButton
)

from PyQt5.QtGui import QIcon, QPixmap

author_surname = 'Baron'
author_name = 'Roksana'

def createConnection():
    server = '155.158.112.85,1433'
    database = 'bazaib'
    username = 'userib'
    password = 'userib123#'
    
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(f'Driver={{SQL SERVER}}; Server={server}; Database={database}; UID={username}; PWD={password}')
    db.open()
    
    if db.open():
        showMessage('Uzyskano polaczenie z baza danych')
        return True
    else:
        showMessage('Blad polaczenia z baza danych')
        
def showMessage(messageTest):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText('Komunikat')
    msg.setInformativeText(messageTest)
    msg.setWindowTitle('Okno komunikatu')
    msg.setDetailedText('Dane szczegolowe komunikatu...')
    retval = msg.exec_()
    
app = QApplication(sys.argv)

if not createConnection():
    sys.exit(1)
    
window = QMainWindow()
window.setWindowTitle('Zadanie 5: ' + author_surname + ' ' + author_name)
window.resize(800,600)

layout = QGridLayout()
layout.addWidget(QLabel('<h3> Aplikacje bazodanowe</h3>'), 0, 0)

tableView = QTableWidget()
tableView.setColumnCount(5)
tableView.setHorizontalHeaderLabels(['ID', 'Nazwisko', 'Imie', 'Badanie', 'Obraz'])

query = QSqlQuery('SELECT id, nazwisko, imie, badanie, obraz FROM t_pacjent_autoid')

while query.next():
    rows = tableView.rowCount()
    tableView.setRowCount(rows + 1)
    tableView.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
    tableView.setItem(rows, 1, QTableWidgetItem(query.value(1)))
    tableView.setItem(rows, 2, QTableWidgetItem(query.value(2)))
    tableView.setItem(rows, 3, QTableWidgetItem(query.value(3)))
    tableView.setItem(rows, 4, QTableWidgetItem('Obraz z bazy'))
    
layout.addWidget(tableView, 1, 0, 1, 10)

layoutWidget = QWidget();
layoutWidget.setLayout(layout);

window.setCentralWidget(layoutWidget)

window.show()

sys.exit(app.exec_())
        