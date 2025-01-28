import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the web browser view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        # Set the web browser as the central widget
        self.setCentralWidget(self.browser)

        # Create navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_btn = QAction('Back', self)
        back_btn.setStatusTip('Back to previous page')
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button
        forward_btn = QAction('Forward', self)
        forward_btn.setStatusTip('Forward to next page')
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload Button
        reload_btn = QAction('Reload', self)
        reload_btn.setStatusTip('Reload page')
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Home Button
        home_btn = QAction('Home', self)
        home_btn.setStatusTip('Go home')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Stop Button
        stop_btn = QAction('Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # URL Changed Event
        self.browser.urlChanged.connect(self.update_urlbar)

        # Go Back, Go Forward, Refresh, URL Bar Context Menu
        navbar.addSeparator()

        # Go Back Button
        back_btn = QAction('Go Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Go Forward Button
        forward_btn = QAction('Go Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Refresh Button
        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        # Clear URL Bar Button
        clear_url_btn = QAction('Clear URL', self)
        clear_url_btn.triggered.connect(self.clear_urlbar)
        navbar.addAction(clear_url_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def clear_urlbar(self):
        self.url_bar.clear()


app = QApplication(sys.argv)
QApplication.setApplicationName("Python Web Browser")

main = WebBrowser()
main.show()

app.exec_()
