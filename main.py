from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from script import insert_user, login_user

Fullname = None
Email = None
Username = None
Password = None


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

        global Fullname 
        global Email 
        global Username 
        global Password 

        Fullname = self.root.get_screen('signup').ids.fullname.text
        Email = self.root.get_screen('signup').ids.email.text
        Username = self.root.get_screen('signup').ids.username.text
        Password = self.root.get_screen('signup').ids.password.text

        success, message = insert_user(Fullname, Email, Username, Password)

        if success:
            
            self.root.current = 'login'  # Navigate back to login screen
            self.message_dialog("Sign Up Successful",message)
        else:
            self.message_dialog("Sign Up Failed", message)


    def message_dialog(self, title, message):
        self.dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    on_release=lambda x: self.dialog.dismiss()
                ),
            ],
        )
        self.dialog.open()


    def login(self):

        username = self.root.get_screen('login').ids.username.text
        password = self.root.get_screen('login').ids.password.text

        success, message = login_user(username, password)

        if success:
            
            self.root.current = 'home'  # Navigate back to login screen

            self.update_title("Home")
            # welcome_label = self.root.get_screen('home').ids.welcome_label
            # welcome_label.text = f"Welcome, {Fullname}!"  # Set the full name here
    
            self.reset_tab()
            self.message_dialog("Log in Successful",message)
        else:
            self.message_dialog("Log in Failed", message)

    

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
