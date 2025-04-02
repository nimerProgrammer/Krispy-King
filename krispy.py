from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

c_Name = None
c_user = None
c_pass = None

KV = '''
ScreenManager:
    LoginScreen:
    DashboardScreen:
    SignupScreen:

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        md_bg_color: 0.82, 0.13, 0.17, 1

        ScrollView:
            do_scroll_x: False
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(20)
                size_hint_y: None
                height: self.minimum_height
                md_bg_color: 0.82, 0.13, 0.17, 1

                Image:
                    source: 'krispy.png'
                    size_hint: None, None
                    size: dp(200), dp(200)
                    pos_hint: {"center_x": 0.5}

                MDCard:
                    elevation: 0
                    radius: dp(15)
                    padding: dp(20)
                    size_hint: None, None
                    size: dp(280), dp(400)
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 1, 1, 1, 0.2

                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: dp(10)
                        adaptive_height: True

                        MDTextField:
                            id: email
                            hint_text: "Username"
                            icon_right: "account"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDTextField:
                            id: password
                            hint_text: "Password"
                            password: True
                            icon_right: "eye-off"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDRaisedButton:
                            text: "Login"
                            md_bg_color: 0, 0.6, 0, 1
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1
                            on_release: app.login()

                        MDLabel:
                            text: "Forgot Password?"
                            theme_text_color: "Custom"
                            text_color: 0,0, 1, 1 
                            halign: "center"
                            size_hint_y: None
                            height: dp(30)

                        MDLabel:
                            text: "[ref=signup]Sign Up[/ref]"
                            markup: True  
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "center"
                            size_hint_y: None
                            height: dp(30)
                            on_ref_press: app.go_to_signup()

                        MDFillRoundFlatIconButton:
                            text: "Login with Google"
                            icon: "google"
                            md_bg_color: 1, 1, 1, 1
                            text_color: 0, 0, 0, 1
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1
                            icon_color: 0,0, 1, 1  

                        MDFillRoundFlatIconButton:
                            text: "Login with Facebook"
                            icon: "facebook"
                            md_bg_color: 0, 0, 1, 1  # Blue background
                            text_color: 1, 1, 1, 1   # White text color
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1

<SignupScreen>:
    name: 'signup'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        md_bg_color: 0.82, 0.13, 0.17, 1

        ScrollView:
            do_scroll_x: False
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(20)
                size_hint_y: None
                height: self.minimum_height
                md_bg_color: 0.82, 0.13, 0.17, 1

                Image:
                    source: 'krispy.png'
                    size_hint: None, None
                    size: dp(200), dp(200)
                    pos_hint: {"center_x": 0.5}

                MDCard:
                    elevation: 0
                    radius: dp(15)
                    padding: dp(20)
                    size_hint: None, None
                    size: dp(280), dp(470)
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 1, 1, 1, 0.2

                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: dp(10)
                        adaptive_height: True

                        MDTextField:
                            id: fullname
                            hint_text: "Full Name"
                            icon_right: "account"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDTextField:
                            id: username
                            hint_text: "Username"
                            icon_right: "account"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}
                            
                        MDTextField:
                            id: email
                            hint_text: "Email"
                            icon_right: "email"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDTextField:
                            id: password
                            hint_text: "Password"
                            password: True
                            icon_right: "eye-off"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDTextField:
                            id: confirm_password
                            hint_text: "Confirm Password"
                            password: True
                            icon_right: "eye-off"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDRaisedButton:
                            text: "Sign Up"
                            md_bg_color: 0, 0.6, 0, 1
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1
                            on_release: app.signup()

                        MDLabel:
                            text: "Already have an account? [ref=login]Login[/ref]"
                            markup: True  
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "center"
                            size_hint_y: None
                            height: dp(30)
                            on_ref_press: app.go_to_login()

            
<DashboardScreen>:
    name: 'dashboard'

    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        id: top_bar
                        title: "Home"
                        elevation: 4
                        md_bg_color: 0.82, 0.13, 0.17, 1

                    MDBottomNavigation:
                        id: bottom_nav

                        MDBottomNavigationItem:
                            name: 'home'
                            text: 'Home'
                            icon: 'home'
                            on_tab_press: app.update_title("Home")

                            ScrollView:
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    padding: dp(20)
                                    adaptive_height: True
                                    
                                    MDLabel:
                                        id: welcome_label
                                        text: "Welcome!"
                                        font_style: "H5"
                                        halign: "center"
                                        theme_text_color: "Custom"
                                        text_color: 0, 0, 0, 1

                                    

                        MDBottomNavigationItem:
                            name: 'profile'
                            text: 'Profile'
                            icon: 'account'
                            on_tab_press: app.update_title("Home/profile")

                            ScrollView:
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: dp(20)
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    pos_hint: {'center_x': 0.5}

                                    MDCard:
                                        size_hint: None, None
                                        size: "300dp", "300dp"
                                        pos_hint: {"center_x": 0.5}
                                        elevation: 4
                                        padding: dp(20)
                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: dp(10)
                                            halign: "center"
                                            valign: "center"

                                            MDIcon:
                                                icon: "account"
                                                pos_hint: {"center_x": 0.5}
                                                theme_text_color: "Custom"
                                                text_color: app.theme_cls.primary_color
                                                font_size: "200sp"

                                            MDLabel:
                                                text: 'Nimer, Gerald M.'
                                                halign: 'center'
                                                theme_text_color: "Custom"
                                                text_color: (0, 0, 0, 1)

                                            MDLabel:
                                                text: 'BSIT - 3B'
                                                halign: 'center'
                                                theme_text_color: "Custom"
                                                text_color: (0, 0, 0, 1)

                        MDBottomNavigationItem:
                            name: 'logout'
                            text: 'Logout'
                            icon: 'logout'
                            on_tab_press:
                                app.logout()
'''

class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class DashboardScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        
        return Builder.load_string(KV)

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
            self.root.current = 'dashboard'
            self.update_title("Home")
            welcome_label = self.root.get_screen('dashboard').ids.welcome_label
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
        top_bar = self.root.get_screen('dashboard').ids.top_bar
        top_bar.title = new_title

    def reset_tab(self):
        bottom_nav = self.root.get_screen('dashboard').ids.bottom_nav
        bottom_nav.switch_tab('home')

MainApp().run()
