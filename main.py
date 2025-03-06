from PyQt5 import QtWidgets
from design import Ui_MainWindow
from copy_file import FileCopier
from run_file import ExeRunner
from add_exception import add_exception
import functools


def installation_exe(self, exe_name):
    copier = FileCopier()
    exe = ExeRunner()
    copier.set_paths(fr"\\192.168.1.191\shared\Public\ToolsHelper\{exe_name}",
                     r"C:\Users\d.gurov\Desktop")
    copier.copy_file()
    exe.set_exe_path(fr'C:\Users\d.gurov\Desktop\{exe_name}')
    exe.run()
    copier.delete_file(fr'C:\Users\d.gurov\Desktop\{exe_name}')


if __name__ == "__main__":
    import sys

    add_exception()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.WinRAR.clicked.connect(functools.partial(installation_exe, exe_name='winrar.exe'))
    ui.Zip.clicked.connect(functools.partial(installation_exe, exe_name='7z.exe'))
    ui.OPORA.clicked.connect(functools.partial(installation_exe, exe_name='OPORA.exe'))
    MainWindow.show()
    sys.exit(app.exec_())
