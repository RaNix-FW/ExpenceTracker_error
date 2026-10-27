# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(795, 689)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(Dialog)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 12, 12, 12)
        self.le_current_balance = QLabel(self.balance_frame)
        self.le_current_balance.setObjectName(u"le_current_balance")
        self.le_current_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.le_current_balance)

        self.label_balance = QLabel(self.balance_frame)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_up_arrow = QLabel(self.balance_frame)
        self.icon_up_arrow.setObjectName(u"icon_up_arrow")
        self.icon_up_arrow.setMaximumSize(QSize(24, 16777215))
        self.icon_up_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_up_arrow.setPixmap(QPixmap(u":/icons/icons/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.icon_up_arrow)

        self.label_income = QLabel(self.balance_frame)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.income_balance = QLabel(self.balance_frame)
        self.income_balance.setObjectName(u"income_balance")
        self.income_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.income_balance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_down_arrow = QLabel(self.balance_frame)
        self.icon_down_arrow.setObjectName(u"icon_down_arrow")
        self.icon_down_arrow.setMaximumSize(QSize(24, 16777215))
        self.icon_down_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_down_arrow.setPixmap(QPixmap(u":/icons/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.icon_down_arrow)

        self.label_outcome = QLabel(self.balance_frame)
        self.label_outcome.setObjectName(u"label_outcome")
        self.label_outcome.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.outcome_balance = QLabel(self.balance_frame)
        self.outcome_balance.setObjectName(u"outcome_balance")
        self.outcome_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.outcome_balance)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(Dialog)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_expanse_tracker = QLabel(self.categories_frame)
        self.label_expanse_tracker.setObjectName(u"label_expanse_tracker")
        self.label_expanse_tracker.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_expanse_tracker)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ico_groc = QLabel(self.categories_frame)
        self.ico_groc.setObjectName(u"ico_groc")
        self.ico_groc.setMaximumSize(QSize(24, 16777215))
        self.ico_groc.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.ico_groc.setPixmap(QPixmap(u":/icons/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.ico_groc)

        self.label_groc = QLabel(self.categories_frame)
        self.label_groc.setObjectName(u"label_groc")
        self.label_groc.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_groc)

        self.balance_groc = QLabel(self.categories_frame)
        self.balance_groc.setObjectName(u"balance_groc")
        self.balance_groc.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.balance_groc)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_ent = QLabel(self.categories_frame)
        self.icon_ent.setObjectName(u"icon_ent")
        self.icon_ent.setMaximumSize(QSize(24, 16777215))
        self.icon_ent.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_ent.setPixmap(QPixmap(u":/icons/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.icon_ent)

        self.label_ent = QLabel(self.categories_frame)
        self.label_ent.setObjectName(u"label_ent")
        self.label_ent.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_ent)

        self.balance_ent = QLabel(self.categories_frame)
        self.balance_ent.setObjectName(u"balance_ent")
        self.balance_ent.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.balance_ent)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_auto = QLabel(self.categories_frame)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(24, 16777215))
        self.icon_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icons/icons/directions_car_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icon_auto)

        self.label_auto = QLabel(self.categories_frame)
        self.label_auto.setObjectName(u"label_auto")
        self.label_auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_auto)

        self.balance_auto = QLabel(self.categories_frame)
        self.balance_auto.setObjectName(u"balance_auto")
        self.balance_auto.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.balance_auto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_other = QLabel(self.categories_frame)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(24, 16777215))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icons/icons/list_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icon_other)

        self.label_other = QLabel(self.categories_frame)
        self.label_other.setObjectName(u"label_other")
        self.label_other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.label_other)

        self.balance_other = QLabel(self.categories_frame)
        self.balance_other.setObjectName(u"balance_other")
        self.balance_other.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.balance_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_new_trans = QPushButton(Dialog)
        self.btn_new_trans.setObjectName(u"btn_new_trans")
        self.btn_new_trans.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_new_trans.setIcon(icon)
        self.btn_new_trans.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_new_trans)

        self.btn_edit_trans = QPushButton(Dialog)
        self.btn_edit_trans.setObjectName(u"btn_edit_trans")
        self.btn_edit_trans.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_trans.setIcon(icon1)
        self.btn_edit_trans.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_trans)

        self.btn_delete_trans = QPushButton(Dialog)
        self.btn_delete_trans.setObjectName(u"btn_delete_trans")
        self.btn_delete_trans.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_trans.setIcon(icon2)
        self.btn_delete_trans.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_delete_trans)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"    background-color: rgba(53, 53, 53);\n"
"    color: white;\n"
"    border: none;\n"
"	height: 50px;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    border: none;\n"
"    color: rgba(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Expense tracker", None))
        self.le_current_balance.setText(QCoreApplication.translate("Dialog", u"Current Balance", None))
        self.label_balance.setText(QCoreApplication.translate("Dialog", u"$1200", None))
        self.icon_up_arrow.setText("")
        self.label_income.setText(QCoreApplication.translate("Dialog", u"income", None))
        self.income_balance.setText(QCoreApplication.translate("Dialog", u"$1200", None))
        self.icon_down_arrow.setText("")
        self.label_outcome.setText(QCoreApplication.translate("Dialog", u"outcome", None))
        self.outcome_balance.setText(QCoreApplication.translate("Dialog", u"$1200", None))
        self.label_expanse_tracker.setText(QCoreApplication.translate("Dialog", u"Expense categories", None))
        self.ico_groc.setText("")
        self.label_groc.setText(QCoreApplication.translate("Dialog", u"Groceries", None))
        self.balance_groc.setText(QCoreApplication.translate("Dialog", u"$1000", None))
        self.icon_ent.setText("")
        self.label_ent.setText(QCoreApplication.translate("Dialog", u"Entartaiment", None))
        self.balance_ent.setText(QCoreApplication.translate("Dialog", u"$1000", None))
        self.icon_auto.setText("")
        self.label_auto.setText(QCoreApplication.translate("Dialog", u"Auto", None))
        self.balance_auto.setText(QCoreApplication.translate("Dialog", u"$1000", None))
        self.icon_other.setText("")
        self.label_other.setText(QCoreApplication.translate("Dialog", u"Other", None))
        self.balance_other.setText(QCoreApplication.translate("Dialog", u"$1000", None))
        self.btn_new_trans.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.btn_edit_trans.setText(QCoreApplication.translate("Dialog", u"Edit transaction", None))
        self.btn_delete_trans.setText(QCoreApplication.translate("Dialog", u"Delete transaction", None))
    # retranslateUi

