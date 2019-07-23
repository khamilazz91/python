from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_click_create(self):
        self.model.create_person(self)

    def on_click_tab_update(self, event):
        self.model.list_person(self)

    def double_click_treeview(self, event):    
        self.model.double_click(self)

    def on_click_btn_update_person(self):
        self.model.update_person(self)

    def on_click_btn_delete_person(self):
        self.model.delete_person(self)

    def on_click_btn_x(self):
        self.model.exit(self)

    def on_click_btn_printing(self):
        self.model.load_id(self)


if __name__ == '__main__':
    app = Controller()
    app.main()


