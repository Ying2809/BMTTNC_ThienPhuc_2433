from .rsa_cipher import RSACipher
def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.Generate_Keys.clicked.connect(self.btnGenerateKeys)
    self.ui.Encrypt.clicked.connect(self.btnEncrypt)
    self.ui.Decrypt.clicked.connect(self.btnDecrypt)
    self.ui.sign.clicked.connect(self.btnSign)
    self.ui.verify.clicked.connect(self.btnVerify)