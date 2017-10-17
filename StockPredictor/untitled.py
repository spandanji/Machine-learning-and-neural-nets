import sys
from PyQt4 import QtGui, QtCore
import stocks as st


# quandlKey = 'KyDThnJDLaoE4Nk2xtoV'
# st.assignQuandlKey(quandlKey)

'''
#Library's Application

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()

window.show()
app.exec_()

'''
class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle('Stocks??')
		self.setWindowIcon(QtGui.QIcon('logo.jpg'))

		#MENU

		extractAction = QtGui.QAction("&Exit the App", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.closeApplication)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

		self.home()
		self.show()
	def home(self):
		btn = QtGui.QPushButton('Quit',self)
		btn.clicked.connect(self.closeApplication)
		btn.resize(50,20)
		btn.move(450,280)


		extractAction = QtGui.QAction(QtGui.QIcon('google.jpg'),'Quit',self)
		extractAction.triggered.connect(self.Google)
		self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(extractAction)

		# self.show()

	def Google(self, state):
		
		#df, pctDataOut = st.retrieve('WIKI/CCE'), 0.005

		#df,pctDataOut== st.retrieve('WIKI/TCS'),0.01
		df, pctDataOut = st.retrieve('WIKI/GOOGL'),0.01
		#df,pctDataOut== st.retrieve('WIKI/MSFT'),0.01
		self.processData(df,pctDataOut)

	def processData(self,df,pctDataOut):
		df = st.featureSelect(df)
		forecast_out, df = st.labelGen( df, train_out=pctDataOut )
		print(df.head())

		X,y,X_train,y_train,X_test,y_test,X_lately = st.matrixGen(df,forecast_out)
		forecast_set,accuracy = st.trainAndTestLinear(X_train,y_train,X_test,y_test,X_lately) 

		df = st.forecastAdd(df,forecast_set)
		st.plotThem(df,forecast_out,accuracy)

	def closeApplication(self):
		#print("Customized!")
		choice  = QtGui.QMessageBox.question(self, 'Extract!',
											"Are you sure you want to quit? ",
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice ==QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()