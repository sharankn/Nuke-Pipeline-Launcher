# -*- coding: utf-8 -*-
import os
import glob
import re
import nuke

from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QMessageBox
)

PROJECT_ROOT = r"D:\Toxic"

class Launcher(QWidget):

    def __init__(self):
        super(Launcher, self).__init__()

        self.setWindowTitle("Toxic Pipeline Launcher")
        self.resize(420, 220)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Project"))
        self.project = QComboBox()
        self.project.addItem("Toxic")
        layout.addWidget(self.project)

        layout.addWidget(QLabel("Sequence"))
        self.sequence = QComboBox()
        for i in range(1,6):
            self.sequence.addItem("Seq%03d" % i)
        layout.addWidget(self.sequence)

        layout.addWidget(QLabel("Shot"))
        self.shot = QComboBox()
        for i in range(1,6):
            self.shot.addItem("Shot%04d" % i)
        layout.addWidget(self.shot)

        btn = QPushButton("New Script")
        btn.clicked.connect(self.newScript)
        layout.addWidget(btn)

        self.setLayout(layout)

    def newScript(self):

        seq = self.sequence.currentText()
        shot = self.shot.currentText()

        shotPath = os.path.join(PROJECT_ROOT, seq, shot)

        plateFolder = os.path.join(shotPath, "plate")
        scriptFolder = os.path.join(shotPath, "script")

        if not os.path.isdir(scriptFolder):
            QMessageBox.warning(self, "Error", "Script folder not found.")
            return

        nkFiles = glob.glob(os.path.join(scriptFolder, "*.nk"))

        version = 1
        for f in nkFiles:
            m = re.search(r'v(\d+)', os.path.basename(f))
            if m:
                version = max(version, int(m.group(1)) + 1)

        filename = "%s_comp_v%03d.nk" % (shot, version)
        savePath = os.path.join(scriptFolder, filename)

        nuke.scriptClear()

        if os.path.isdir(plateFolder):
            exrs = sorted(glob.glob(os.path.join(plateFolder, "*.exr")))
            if exrs:
                read = nuke.nodes.Read()
                # Let Nuke interpret the image sequence
                read["file"].fromUserText(exrs[0])

        nuke.scriptSaveAs(savePath)

        QMessageBox.information(
            self,
            "Success",
            "Created:\n\n%s" % savePath
        )

window = None

def launch():
    global window
    try:
        window.close()
    except:
        pass

    window = Launcher()
    window.show()