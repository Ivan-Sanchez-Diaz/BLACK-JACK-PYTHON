
#Instalar Librerias PySide6
#pip install PySide6

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from random import randint
import sys
from ui_main import Ui_MainWindow

cardCount = [0]
playerCount = [0]
dalerCount = [0]
data = []
end = [True]
loses = []
class MainWindow(QMainWindow):
    def __init__(self):

        #PARAMETROS BASICOS(QUITAR MARCO DE WINDWOS,TAMAÑO;GUI)
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(QSize(500,550))
        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_minimize.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #ARRASTRAR VENTANA
        def move(event,self):
          if event.buttons() == Qt.LeftButton:
              self.move(self.pos() + event.globalPos() - self.dragPos)
              self.dragPos = event.globalPos()
              event.accept()

        #ARRASTRAR VENTANA
        def moveWindow(event):
          move(event,self)
  
        self.ui.frame_title.mouseMoveEvent = moveWindow

        #DAR CARTA AL CRUPIER
        def hitDaler(self):
          if dalerCount[0]<17:
            addCard(self,self.ui.daler_page_layout,randint(1,11),dalerCount,False)
            
          if dalerCount[0]>21:
            self.ui.hit.setEnabled(False)
            self.ui.hit.setText("YOU WIN!")
            self.ui.stand.setText("ClOSE")
            self.ui.simulate.setEnabled(False)
            self.ui.simulate.setText("YOU WIN!")
            loses.append("WIN")
            self.ui.stand.clicked.connect(lambda: self.close())

            for buttons in self.ui.daler_page.findChildren(QPushButton):
              buttons.setStyleSheet('''
                QPushButton {
                    background-color: rgb(35,35,35); 
                    color:white;
                }
                QPushButton:pressed {
                    background-color : rgba(35,35,35,155);
                    color:white;
                }
            ''')
               
          
        #PLANTARSE
        def stand(self):
          for buttons in self.ui.daler_page.findChildren(QPushButton):
            buttons.setStyleSheet('''
              QPushButton {
                  background-color: rgb(35,35,35); 
                  color:white;
              }
              QPushButton:pressed {
                  background-color : rgba(35,35,35,155);
                  color:white;
              }
          ''')
               

          if playerCount[0]>dalerCount[0]:
            self.ui.hit.setEnabled(False)
            self.ui.hit.setText("YOU WIN!")
            self.ui.stand.setText("ClOSE")
            self.ui.simulate.setEnabled(False)
            self.ui.simulate.setText("YOU WIN!")
            loses.append("Win")
            self.ui.stand.clicked.connect(lambda: self.close())
          else:
            self.ui.hit.setEnabled(False)
            self.ui.hit.setText("YOU LOSE!")
            self.ui.stand.setText("ClOSE")
            self.ui.simulate.setEnabled(False)
            self.ui.simulate.setText("YOU LOSE!")
            loses.append("Lost")
            self.ui.stand.clicked.connect(lambda: self.close())

          


        def Lose(self):
          loses.append("Lost")
          for buttons in self.ui.daler_page.findChildren(QPushButton):
            buttons.setStyleSheet('''
              QPushButton {
                  background-color: rgb(35,35,35); 
                  color:white;
              }
              QPushButton:pressed {
                  background-color : rgba(35,35,35,155);
                  color:white;
              }
          ''')
          self.ui.hit.setEnabled(False)
          self.ui.hit.setText("YOU LOSE!")
          self.ui.stand.setText("ClOSE")
          self.ui.simulate.setEnabled(False)
          self.ui.simulate.setText("YOU LOSE!")
          self.ui.stand.clicked.connect(lambda: self.close())
          end.append(True)
        
          
        def simulate(self):
          
          ############SIMULACION DE LAS 100 PARTIDAS
          for i in range(0,100):
            simulate = []
            cardCount = [0]
               
            if end[0] == True:
              playerCount = [0]
              dalerCount = [0]   
              
              for buttons in self.ui.daler_page.findChildren(QWidget):
                buttons.deleteLater()
              
              for buttons in self.ui.player_page.findChildren(QWidget):
                buttons.deleteLater()

              addCard(self,self.ui.player_page_layout,randint(1,11),playerCount,True)
              addCard(self,self.ui.player_page_layout,randint(1,11),playerCount,True)
              addCard(self,self.ui.daler_page_layout,randint(1,11),dalerCount,True)
              addCard(self,self.ui.daler_page_layout,randint(1,11),dalerCount,False)

              
              while playerCount[0]<15:
                addCard(self,self.ui.player_page_layout,randint(1,11),playerCount,True)
                if dalerCount[0]<17:
                  addCard(self,self.ui.daler_page_layout,randint(1,11),playerCount,False)
                if dalerCount[0]>21:
                  break
              else:
                stand(self)
              
              if playerCount[0]>dalerCount[0] and playerCount[0]<21:
                data.append("win")

          self.ui.hit.setText("WIN RATE: "+str(len(data)) + "%")
          self.ui.simulate.setText("WIN RATE: "+str(len(data)) + "%")

        def findOut(self):
          if playerCount[0]>21:
            Lose(self)

        #AGREGAR CARTA JUGADOR
        def addCard(self,layout,value,list,bool):
          button = QPushButton("1",self)
          list.append(list[0]+1)
          last = list.pop()
          button.setObjectName("card_"+str(last))
          sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
          sizePolicy3.setHorizontalStretch(0)
          sizePolicy3.setVerticalStretch(0)
          sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
          button.setSizePolicy(sizePolicy3)
          button.setMinimumSize(QSize(60, 100))
          button.setMaximumSize(QSize(60,100))

          if bool:
            button.setStyleSheet('''
              QPushButton {
                  background-color: rgb(35,35,35); 
                  color:white;
              }
              QPushButton:pressed {
                  background-color : rgba(25,25,25,155);
              }
          ''')
          else:
            button.setStyleSheet('''
              QPushButton {
                  background-color: rgb(35,35,35); 
                  border-radius = 0;
                  color:rgb(35,35,35);
              }
              QPushButton:pressed {
                  background-color : rgba(35,35,35,155);
                  color:rgba(35,35,35,0)
              }
          ''')
          button.setLayoutDirection(Qt.LeftToRight)
          button.setText(str(value))
          list[0] = list[0] + value
          findOut(self)
          layout.addWidget(button)

        addCard(self,self.ui.player_page_layout,randint(1,11),playerCount,True)
        addCard(self,self.ui.player_page_layout,randint(1,11),playerCount,True)


        addCard(self,self.ui.daler_page_layout,randint(1,11),dalerCount,True)
        addCard(self,self.ui.daler_page_layout,randint(1,11),dalerCount,False)

        self.ui.hit.clicked.connect(lambda:addCard(self,self.ui.player_page_layout,randint(1,11),playerCount,True))
        self.ui.hit.clicked.connect(lambda:hitDaler(self))
        self.ui.stand.clicked.connect(lambda:stand(self))
        self.ui.simulate.clicked.connect(lambda:simulate(self))

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())