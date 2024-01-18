import sys

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
    QPushButton,
    QLineEdit
)

from PyQt5.QtGui import QIcon, QPixmap


author_surname = 'Baron'
author_name = 'Roksana'
databaseOpened = False

def createConnection():
    
    server = '155.158.112.85,1433'
    database = 'bazaib'
    username = 'userib'
    password = 'userib123#'
    
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(f'Driver={{SQL SERVER}}; Server={server}; Database={database}; UID={username}; PWD={password}')
    db.open()
    
    if db.open():
        
        global databaseOpened
        databaseOpened = True
        showMessageFull("Połączono z bazą danych...",QMessageBox.Information)
        return True
    else:
        showMessageFull("Brak połączenia z bazą danych...",QMessageBox.Critical)
        return False
    
def showMessageFull(messageText,messageType):
    msg = QMessageBox()
    msg.setIcon(messageType)
    msg.setText(messageText)
    
    msg.setWindowTitle("Okno komunikatu")
    
    retval = msg.exec_()
    
def login():
    if not createConnection():
        sys.exit(1)
    
def logout():
    sys.exit(1)
    
def refreshData(surnameParam, nameParam):
    
    query = QSqlQuery()
    query.prepare("SELECT id, nazwisko, imie, badanie, obraz FROM t_pacjent_autoid WHERE nazwisko LIKE :surname AND imie LIKE :name")
    query.bindValue(":surname", surnameParam)
    query.bindValue(":name", nameParam)
    query.exec()
    
    
    tableView.setRowCount(0)
    
    while query.next():
        rows = tableView.rowCount()
        tableView.setRowCount(rows + 1)
        tableView.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
        tableView.setItem(rows, 1, QTableWidgetItem(query.value(1)))
        tableView.setItem(rows, 2, QTableWidgetItem(query.value(2)))
        tableView.setItem(rows, 3, QTableWidgetItem(query.value(3)))
        
        
        it = getImageLabel(query.value(4))
        tableView.setCellWidget(rows, 4, it)
        tableView.setRowHeight(rows,130)
        
def refresh():
    
    filterSurname = '%' + filterSurnameEdit.text()+'%'
    filterName = '%' + filterNameEdit.text()+'%'
 
   
    print(databaseOpened)
    if databaseOpened:
        refreshData(filterSurname, filterName)
    else:
        showMessageFull("Użytkownik niezalogowany...",QMessageBox.Critical)
    
def getImageLabel(databaseImage):
    imageLabel = QLabel()
    imageLabel.setText("xxx")
    imageLabel.setScaledContents(True)
    pixmap = QPixmap()
    pixmap.loadFromData(databaseImage)
    imageLabel.setPixmap(pixmap)
    return imageLabel


app = QApplication(sys.argv)
databaseOpened = False


window = QMainWindow()

window.setWindowTitle("Zadanie 6: " + author_surname + ' ' + author_name)

window.resize(800, 600)



layout = QGridLayout()


layout.addWidget(QLabel('<h3>Aplikacje bazodanowe</h3>'), 0, 0)


pushButtonLogin = QPushButton('Zaloguj')
pushButtonRefresh = QPushButton('Wczytaj dane')
pushButtonLogout = QPushButton('Wyloguj')

layout.addWidget(pushButtonLogin, 0, 1)
layout.addWidget(pushButtonRefresh, 0, 2)
layout.addWidget(pushButtonLogout, 0, 3)


pushButtonLogin.clicked.connect(login)
pushButtonRefresh.clicked.connect(refresh)
pushButtonLogout.clicked.connect(logout)


surnameLabel = QLabel()
surnameLabel.setText("Nazwisko")
layout.addWidget(surnameLabel,2,0)
filterSurnameEdit = QLineEdit()
filterSurnameEdit.setText('')
layout.addWidget(filterSurnameEdit,2,1)

nameLabel = QLabel()
nameLabel.setText("Imię")
layout.addWidget(nameLabel,2,2)
filterNameEdit = QLineEdit()
filterNameEdit.setText('')
layout.addWidget(filterNameEdit,2,3)


layoutWidget = QWidget();
layoutWidget.setLayout(layout);



tableView = QTableWidget()
tableView.setColumnCount(5)
tableView.setHorizontalHeaderLabels(["ID", "Nazwisko", "Imie", "Badanie", "Obraz"])


layout.addWidget(tableView, 3, 0, 3, 10)


window.setCentralWidget(layoutWidget)


window.show()


sys.exit(app.exec_())