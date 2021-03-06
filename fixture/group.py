class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0:
            return
        wd.find_element_by_link_text('groups').click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name('new').click()
        self.fill_group_form(group)
        wd.find_element_by_name('submit').click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field('group_name', group.name)
        self.change_field('group_header', group.header)
        self.change_field('group_footer', group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # delete first group
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('group page').click()
