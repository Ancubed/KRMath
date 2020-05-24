from PyQt5 import QtWidgets, uic
from NU import NonlinearEquation
from SNU import SystemsOfNonlinearEquations


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        uic.loadUi('math_kr.ui', self)
        self.buttons_action_init()

    def buttons_action_init(self):
        self.nu_btn_calc.clicked.connect(self.nu_calc)
        self.snu_btn_calc.clicked.connect(self.snu_calc)
        self.slau_btn_calc.clicked.connect(self.slau_calc)

    def nu_calc(self):
        nu = NonlinearEquation(self.nu_lineEdit_eq.text(), self.nu_lineEdit_deq.text(), self.nu_lineEdit_ddeq.text(),
                               self.nu_dspinBox_interval_from.value(), self.nu_dspinBox_interval_to.value(),
                               self.nu_dspinBox_precision.value())
        answer = nu.calc()
        try:
            for x in answer[1]:
                self.nu_listWidget_answer_2.addItem(str(x))
            for x in answer[2]:
                self.nu_listWidget_answer_3.addItem(str(x))
            for x in answer[0]:
                self.nu_listWidget_answer_1.addItem(str(x))
        except Exception:
            self.nu_listWidget_answer_1.addItem("Ошибка.")
            self.nu_listWidget_answer_1.addItem(answer[0])

    def snu_calc(self):
        if self.snu_rb_iteration.isChecked():
            snu = SystemsOfNonlinearEquations(self.snu_luneEdit_y.text(),
                                              self.snu_lineEdit_x.text(),
                                              self.snu_dspinBox_x_start.value(),
                                              self.snu_dspinBox_y_start.value(),
                                              self.snu_dspinBox_precision.value())
        else:
            snu = SystemsOfNonlinearEquations(self.snu_luneEdit_y.text(),
                                              self.snu_lineEdit_x.text(),
                                              self.snu_dspinBox_x_start.value(),
                                              self.snu_dspinBox_y_start.value(),
                                              self.snu_dspinBox_precision.value(),
                                              self.snu_lineEdit_y_x.text(),
                                              self.snu_lineEdit_y_y.text(),
                                              self.snu_lineEdit_x_x.text(),
                                              self.snu_lineEdit_x_y.text())
        try:
            self.snu_label_result.setText(str(snu.calc()))
        except Exception:
            self.snu_label_result.setText("Ошибка")


    def slau_calc(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
