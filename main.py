from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

c_Name = None
c_user = None
c_pass = None


class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class HomeScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        
        Builder.load_file('design/login.kv')
        Builder.load_file('design/signup.kv')
        Builder.load_file('design/main.kv')  
        return Builder.load_file('design/screenManager.kv')
    
         

    def go_to_signup(self):
        self.root.current = 'signup'
        
    def go_to_login(self):
        self.root.current = 'login'
        
    def signup(self):
        global c_Name 
        global c_user 
        global c_pass 

        c_Name = self.root.get_screen('signup').ids.fullname.text
        c_user = self.root.get_screen('signup').ids.username.text
        c_pass = self.root.get_screen('signup').ids.password.text

        self.root.current = 'login'
        
    def login(self):
        email = self.root.get_screen('login').ids.email.text
        password = self.root.get_screen('login').ids.password.text

        if email == c_user and password == c_pass:  # Missing colon added
            self.root.current = 'home'
            self.update_title("Home")
            welcome_label = self.root.get_screen('home').ids.welcome_label
            welcome_label.text = f"Welcome, {c_Name}!"  # Set the full name here
    
            self.reset_tab()
        else:
            self.show_login_failed_dialog()

    def show_login_failed_dialog(self):
        if not hasattr(self, 'dialog'):
            self.dialog = MDDialog(
                title="Login Failed",
                text="Invalid email or password.",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()

    def logout(self):
        if not hasattr(self, 'logout_dialog'):
            self.logout_dialog = MDDialog(
                title="Confirm Logout",
                text="Are you sure you want to logout?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=lambda x: self.logout_dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="LOGOUT",
                        on_release=self.confirm_logout
                    ),
                ],
            )
        self.logout_dialog.open()

    def confirm_logout(self, *args):
        self.logout_dialog.dismiss()
        self.root.current = 'login'
        self.update_title("Home")
        self.reset_tab()

    def update_title(self, new_title):
        top_bar = self.root.get_screen('home').ids.top_bar
        top_bar.title = new_title

    def reset_tab(self):
        bottom_nav = self.root.get_screen('home').ids.bottom_nav
        bottom_nav.switch_tab('home')

MainApp().run()
