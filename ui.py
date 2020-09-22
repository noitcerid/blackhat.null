

import npyscreen


class MainMenu(npyscreen.Form):
    def afterEditing(self):
        if self.command.value == 'Login':
            self.parentApp.setNextForm(LoginMenu)
        elif self.command.value == 'Settings':
            self.parentApp.setNextForm(None)  # TODO: Change to 'SettingsMenu' once implemented
        # else:
        #     self.parentApp.setNextForm(None)

    def create(self):
        self.command = self.add(
            npyscreen.TitleSelectOne,
            max_height=3,
            name='Command',
            values=['Login', 'Settings', 'Exit'],
            scroll_exit=True
        )


class LoginMenu(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(PlayMenu)

    def create(self):
        self.username = self.add(npyscreen.TitleText, name='Username')
        self.password = self.add(npyscreen.TitlePassword, name='Password')


class PlayMenu(npyscreen.Form):
    def afterEditing(self):
        # TODO: Write additional branch logic for play menu
        self.parentApp.setNextForm(MainMenu)

    def create(self):
        self.command = self.add(
            npyscreen.TitleSelectOne,
            name='Command',
            values=['Jobs Board', 'Banking', 'Shop', 'Terminal', 'Logout'],
            scroll_exit=True
        )
        # self.command = self.add(
        #     npyscreen.TextCommandBox()
        # )


class SettingsMenu(npyscreen.ActionForm):
    def afterEditing(self):
        self.parentApp.setNextForm(MainMenu)


class GameApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainMenu, name='Main Menu')
        self.addForm('LOGIN', LoginMenu, name='Login Menu')
        self.addForm('PLAY', PlayMenu, name='Play Menu')
        self.addForm('SETTINGS', SettingsMenu, name='Settings Menu')


if __name__ == '__main__':
    app = GameApplication().run()
