class ComboBoxWithMultiSelect:
    def __init__(self, c_b, it):
        self.combo_box = c_b
        self.items = it
        self.combo_box.addItems(self.items)
        self.combo_box.currentTextChanged.connect(self.select)

    def select(self):
        if self.combo_box.currentText() not in {'select', ''}:
            if ' (selected)' in self.combo_box.currentText():
                self.items[self.combo_box.currentIndex()] = \
                    self.items[self.combo_box.currentIndex()].split(' (selected)')[0]
            else:
                self.items[self.combo_box.currentIndex()] += ' (selected)'
            self.combo_box.clear()
            self.combo_box.addItems(self.items)
            self.combo_box.showPopup()