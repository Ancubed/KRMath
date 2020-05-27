from PyQt5 import QtWidgets, uic
from NU import NonlinearEquation
from SNU import SystemsOfNonlinearEquations
from SLAU import SystemsOfLinearAlgebraicEquations
from ODU import OrdinaryDifferentialEquation
from IF import InterpolatingFunctions
from CHI import NumericalIntegration
from CHD import NumericalDifferentiation


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        uic.loadUi('math_kr.ui', self)
        self.buttons_action_init()

    def buttons_action_init(self):
        self.nu_btn_calc.clicked.connect(self.nu_calc)
        self.snu_btn_calc.clicked.connect(self.snu_calc)
        self.slau_btn_calc.clicked.connect(self.slau_calc)
        self.odu_btn_calc.clicked.connect(self.odu_calc)
        self.if_btn_calc.clicked.connect(self.if_calc)
        self.chi_btn_calc.clicked.connect(self.chi_calc)
        self.chd_btn_calc.clicked.connect(self.chd_calc)

    def nu_calc(self):
        nu = NonlinearEquation(self.nu_lineEdit_eq.text(),
                               self.nu_lineEdit_deq.text(),
                               self.nu_lineEdit_ddeq.text(),
                               self.nu_dspinBox_interval_from.value(),
                               self.nu_dspinBox_interval_to.value(),
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
        try:
            if self.snu_rb_iteration.isChecked():
                snu = SystemsOfNonlinearEquations(self.snu_luneEdit_y.text(),
                                                  self.snu_lineEdit_x.text(),
                                                  self.snu_dspinBox_x_start.value(),
                                                  self.snu_dspinBox_y_start.value(),
                                                  self.snu_dspinBox_precision.value())
                self.snu_label_result.setText(str(snu.calc()))
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
                self.snu_label_result.setText(str(snu.calc()))
        except Exception:
            self.snu_label_result.setText("Ошибка")

    def slau_calc(self):
        try:
            slau = SystemsOfLinearAlgebraicEquations([[self.slau_dspinBox_00.value(),
                                                       self.slau_dspinBox_01.value(),
                                                       self.slau_dspinBox_02.value(),
                                                       self.slau_dspinBox_03.value()],
                                                      [self.slau_dspinBox_10.value(),
                                                       self.slau_dspinBox_11.value(),
                                                       self.slau_dspinBox_12.value(),
                                                       self.slau_dspinBox_13.value()],
                                                      [self.slau_dspinBox_20.value(),
                                                       self.slau_dspinBox_21.value(),
                                                       self.slau_dspinBox_22.value(),
                                                       self.slau_dspinBox_23.value()]],
                                                     self.slau_dspinBox_precision.value())
            self.slau_label_result_gauss.setText(str(slau.gaussian_method()))
            slau.diagonal_prevalence()
            self.slau_label_result_iteration.setText(str(slau.iteration_method()))
            self.slau_label_result_seidel.setText(str(slau.seidels_method()))
        except Exception:
            self.slau_label_result_gauss.setText("Ошибка")
            self.slau_label_result_iteration.setText("Ошибка")
            self.slau_label_result_seidel.setText("Ошибка")

    def odu_calc(self):
        try:
            odu = OrdinaryDifferentialEquation(self.odu_lineEdit_eq.text(),
                                               self.odu_dspinBox_y0.value(),
                                               self.odu_dspinBox_interval_from.value(),
                                               self.odu_dspinBox_interval_to.value(),
                                               self.odu_dspinBox_h.value())
            answer = odu.calc()
            for x in answer[0]:
                self.odu_listWidget_answer_x.addItem(str(x))
            for y in answer[1]:
                self.odu_listWidget_answer_ye.addItem(str(y))
            for y in answer[2]:
                self.odu_listWidget_answer_yr.addItem(str(y))
        except Exception:
            self.odu_listWidget_answer_x.addItem("Ошибка")
            self.odu_listWidget_answer_ye.addItem("Ошибка")
            self.odu_listWidget_answer_yr.addItem("Ошибка")

    def if_calc(self):
        try:
            if self.if_rb_lagrange.isChecked() or self.if_rb_newton.isChecked():
                if_o = InterpolatingFunctions([self.if_dspinBox_x1.value(),
                                               self.if_dspinBox_x2.value(),
                                               self.if_dspinBox_x3.value()],
                                              [self.if_dspinBox_fx1.value(),
                                               self.if_dspinBox_fx2.value(),
                                               self.if_dspinBox_fx3.value()],
                                              [self.if_dspinBox_xn.value()])
                self.if_label_result.setText(str(if_o.lagrange_polynomial()
                                                 if self.if_rb_lagrange.isChecked()
                                                 else if_o.newton_polynomial()))
            else:
                if_o = InterpolatingFunctions([self.if_dspinBox_x1.value(),
                                               self.if_dspinBox_x2.value(),
                                               self.if_dspinBox_x3.value(),
                                               self.if_dspinBox_x4.value()],
                                              [self.if_dspinBox_fx1.value(),
                                               self.if_dspinBox_fx2.value(),
                                               self.if_dspinBox_fx3.value(),
                                               self.if_dspinBox_fx4.value()],
                                              [self.if_dspinBox_xn.value()])
                self.if_label_result.setText(str(if_o.cubic_spline()))
        except Exception:
            self.if_label_result.setText("Ошибка")

    def chi_calc(self):
        try:
            chi = NumericalIntegration(self.chi_lineEdit_eq.text(),
                                       self.chi_dspinBox_from.value(),
                                       self.chi_dspinBox_to.value(),
                                       self.chi_spinBox_n.value())
            self.chi_label_result_rectangle.setText(str(chi.method_of_rectangles()))
            self.chi_label_result_trapeze.setText(str(chi.method_of_trapezes()))
            self.chi_label_result_simpson.setText(str(chi.method_of_simpson()))
        except Exception:
            self.chi_label_result_rectangle.setText("Ошибка")
            self.chi_label_result_trapeze.setText("Ошибка")
            self.chi_label_result_simpson.setText("Ошибка")

    def chd_calc(self):
        try:
            chd = NumericalDifferentiation([self.chd_dspinBox_x1.value(),
                                            self.chd_dspinBox_x2.value(),
                                            self.chd_dspinBox_x3.value(),
                                            self.chd_dspinBox_x4.value()],
                                           [self.chd_dspinBox_fx1.value(),
                                            self.chd_dspinBox_fx2.value(),
                                            self.chd_dspinBox_fx3.value(),
                                            self.chd_dspinBox_fx4.value()],
                                           [self.chd_dspinBox_xn.value()])
            self.chd_label_result.setText(str(chd.numerical_diff()))
        except Exception:
            self.chd_label_result.setText("Ошибка")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
