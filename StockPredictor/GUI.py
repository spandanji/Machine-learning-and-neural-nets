#!/usr/bin/python3
#The GUI
import sys
from PyQt4 import QtGui, QtCore
import stocks as st

# quandlKey = 'KyDThnJDLaoE4Nk2xtoV'
# st.assignQuandlKey(quandlKey)
class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,520,300)
		self.setWindowTitle('Stocks??')
		self.setWindowIcon(QtGui.QIcon('logo.jpg'))

		#MENU
		
		QuitFunc = QtGui.QAction("&Exit the App", self)
		QuitFunc.setShortcut("Ctrl+Q")
		QuitFunc.setStatusTip('Leave The App')
		QuitFunc.triggered.connect(self.closeApplication)

		tickerC = QtGui.QAction("&Enter Custom Ticker", self)
		tickerC.setShortcut("Ctrl+T")
		tickerC.setStatusTip('Enter a custom Quandl Ticker')
		tickerC.triggered.connect(self.ticker)

		ApiKey = QtGui.QAction("&Api Key", self)
		ApiKey.setShortcut("Ctrl+K")
		ApiKey.setStatusTip('Enter your Quandl API key')
		ApiKey.triggered.connect(self.apiSet)

		PCT_OUT = QtGui.QAction("&PCT_OUT", self)
		PCT_OUT.setShortcut("Ctrl+P")
		PCT_OUT.setStatusTip('Change the Precentage out of the data that you wish to predict')
		PCT_OUT.triggered.connect(self.changePCTout)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(QuitFunc)
		fileMenu.addAction(tickerC)
		
		editMenu = mainMenu.addMenu('&Edit')
		editMenu.addAction(ApiKey)
		editMenu.addAction(PCT_OUT)

		self.setKey()

		self.home()
		self.show()

	def home(self):
		btn = QtGui.QPushButton('Quit',self)
		btn.clicked.connect(self.closeApplication)
		btn.resize(50,20)
		btn.move(450,280)

		ticker = QtGui.QPushButton('Provide Custom Quandl ticker',self)
		ticker.clicked.connect(self.ticker)
		ticker.setStatusTip('Enter a custom Quandl Ticker')
		ticker.resize(250,30)
		ticker.move(150,150)

		apiKey = QtGui.QPushButton('Enter Quandl API Key',self)
		apiKey.clicked.connect(self.apiSet)
		apiKey.resize(150,30)
		apiKey.move(200,190)

		chPCT = QtGui.QPushButton('Change PCT_out',self)
		chPCT.setStatusTip('Change the Precentage out of the data that you wish to predict')
		chPCT.clicked.connect(self.changePCTout)
		chPCT.resize(150,30)
		chPCT.move(200,230)


		GoogleStock = QtGui.QAction(QtGui.QIcon('google.jpg'),'Google',self)
		GoogleStock.setStatusTip('Click to get stock Data from Quandl')
		GoogleStock.triggered.connect(self.Google)
		self.toolbar = self.addToolBar('Big Guns')
		self.toolbar.addAction(GoogleStock)

		MicrosoftStock = QtGui.QAction(QtGui.QIcon('microsoft.jpg'),'Microsoft',self)
		MicrosoftStock.triggered.connect(self.Microsoft)
		MicrosoftStock.setStatusTip('Click to get stock Data from Quandl')
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(MicrosoftStock)

		YahooStock = QtGui.QAction(QtGui.QIcon('yahoo.png'),'Yahoo',self)
		YahooStock.setStatusTip('Click to get stock Data from Quandl')
		YahooStock.triggered.connect(self.Yahoo)
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(YahooStock)

		AppleStock = QtGui.QAction(QtGui.QIcon('apple.png'),'Apple',self)
		AppleStock.setStatusTip('Click to get stock Data from Quandl')
		AppleStock.triggered.connect(self.Apple)
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(AppleStock)

		NvidiaStock = QtGui.QAction(QtGui.QIcon('nvidia.jpg'),'Nvidia',self)
		NvidiaStock.setStatusTip('Click to get stock Data from Quandl')
		NvidiaStock.triggered.connect(self.Nvidia)
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(NvidiaStock)

		QuallacommStock = QtGui.QAction(QtGui.QIcon('quallacomm.png'),'Quallacomm',self)
		QuallacommStock.setStatusTip('Click to get stock Data from Quandl')
		QuallacommStock.triggered.connect(self.Quallacomm)
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(QuallacommStock)

		AtiStock = QtGui.QAction(QtGui.QIcon('ati.png'),'Ati',self)
		AtiStock.setStatusTip('Click to get stock Data from Quandl')
		AtiStock.triggered.connect(self.Ati)
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(AtiStock)

		TiStock = QtGui.QAction(QtGui.QIcon('ti.jpg'),'Texas Instruments',self)
		TiStock.setStatusTip('Click to get stock Data from Quandl')
		TiStock.triggered.connect(self.Ti)
		# self.toolbar = self.addToolBar('Extraction')
		self.toolbar.addAction(TiStock)

		TcsStock = QtGui.QAction(QtGui.QIcon('tcs.png'),'TCS',self)
		TcsStock.setStatusTip('Click to get stock Data from Quandl')
		TcsStock.triggered.connect(self.TCS)
		self.toolbar = self.addToolBar('IT ..')
		self.toolbar.addAction(TcsStock)

		CogStock = QtGui.QAction(QtGui.QIcon('cog.jpg'),'Cognizant',self)
		CogStock.setStatusTip('Click to get stock Data from Quandl')
		CogStock.triggered.connect(self.COG)
		#self.toolbar = self.addToolBar('IT ..')
		self.toolbar.addAction(CogStock)

		CokeStock = QtGui.QAction(QtGui.QIcon('coke.png'),'Coca-Cola',self)
		CokeStock.setStatusTip('Click to get stock Data from Quandl')
		CokeStock.triggered.connect(self.coke)
		self.toolbar = self.addToolBar('Food ..')
		self.toolbar.addAction(CokeStock)

		PepsiStock = QtGui.QAction(QtGui.QIcon('pep.png'),'PepsiCO',self)
		PepsiStock.setStatusTip('Click to get stock Data from Quandl')
		PepsiStock.triggered.connect(self.pep)
		#self.toolbar = self.addToolBar('Food ..')
		self.toolbar.addAction(PepsiStock)

		HyattStock = QtGui.QAction(QtGui.QIcon('hayatt.jpg'),'Hayatt',self)
		HyattStock.setStatusTip('Click to get stock Data from Quandl')
		HyattStock.triggered.connect(self.Hayatt)
		self.toolbar = self.addToolBar('Hotel Chains ..')
		self.toolbar.addAction(HyattStock)

	def Hayatt(self):
		df_link,pctDataOut = 'WIKI/H',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def pep(self):
		df_link,pctDataOut = 'WIKI/PEP',self.readPCTout()
		self.processData(df_link,pctDataOut)

		# self.show()
	def coke(self):
		df_link,pctDataOut = 'WIKI/CCE',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def Ti(self):
		df_link,pctDataOut = 'WIKI/TXN',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def COG(self):
		df_link,pctDataOut = 'WIKI/CTSH',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def TCS(self):
		df_link,pctDataOut = 'WIKI/TCS',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def Ati(self):
		df_link,pctDataOut = 'WIKI/ATI',self.readPCTout()
		self.processData(df_link,pctDataOut)



	def Quallacomm(self):
		df_link,pctDataOut = 'WIKI/QCOM',self.readPCTout()
		self.processData(df_link,pctDataOut)


	def Nvidia(self):
		

		#df_link,pctDataOut = 'WIKI/AAPL',0.005
		df_link,pctDataOut = 'WIKI/NVDA',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def Apple(self):
		#df_link,pctDataOut = 'WIKI/AAPL',0.005
		df_link,pctDataOut = 'WIKI/AAPL',self.readPCTout()
		self.processData(df_link,pctDataOut)
	

	def Yahoo(self):
		df_link,pctDataOut = 'WIKI/YHOO',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def Microsoft(self):
		
		df_link,pctDataOut = 'WIKI/MSFT',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def Google(self):
		df_link, pctDataOut = 'WIKI/GOOGL',self.readPCTout()
		self.processData(df_link,pctDataOut)

	def processData(self,df_link,pctDataOut):
		choice  = QtGui.QMessageBox.question(self, 'Listen up!',
											"Data is going to be downloaded from the internet. \n Make sure you have a working internet connection \n Continue? ",
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice ==QtGui.QMessageBox.Yes:
			df = st.retrieve(df_link)
			df = st.featureSelect(df)
			forecast_out, df = st.labelGen( df, train_out=pctDataOut )
			print(df.head())

			X,y,X_train,y_train,X_test,y_test,X_lately = st.matrixGen(df,forecast_out)
			forecast_set,accuracy = st.trainAndTestLinear(X_train,y_train,X_test,y_test,X_lately) 

			df = st.forecastAdd(df,forecast_set)
			st.plotThem(df,forecast_out,accuracy)

		else:
			pass

	def ticker(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Enter a Quandl ticker', 'Ticker:')
		if ok:
			df_link,pctDataOut = text,self.readPCTout()
		self.processData(df_link,pctDataOut)

	def readPCTout(self):
		file = open('pctout.txt', "r")
		pct = file.read()
		file.close()
		return float(pct)

	def changePCTout(self):
		file2 = open('pctout.txt', "r")
		prevPct = file2.read()
		file2.close()
		PCT, ok = QtGui.QInputDialog.getText(self, 'Tweak Away!!', 'PCT(Current :'+prevPct+') : ')
		if ok:
			file3=open("pctout.txt","w")
			file3.write(PCT)
			file3.close()	

	def setKey(self):
		file = open('key.txt', "r")
		Key = file.read()
		st.assignQuandlKey(Key)
		file.close()

	def apiSet(self):
		Key, ok = QtGui.QInputDialog.getText(self, 'Enter your Quandl Key', 'Key:')
		if ok:
			st.assignQuandlKey(Key)
			file=open("key.txt","w")
			file.write(Key)
			file.close()			

	def closeApplication(self):
		choice  = QtGui.QMessageBox.question(self, 'Extract!',
											"Are you sure you want to quit? ",
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice ==QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
