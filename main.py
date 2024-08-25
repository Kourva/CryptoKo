#!/usr/bin/env python3


# GitHub: https://github.com/Kourva/CryptoKo
# Author: Kourva


# Imports
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from cryptography.fernet import Fernet
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious


# KV config
with open("main.kv", "r") as kv:
    Builder.load_string(kv.read())


# StartMenu screen
class StartMenuScreen(Screen):
    # Path to fonts
    KremlinMenshevik = "Aldo.ttf"
    SourceCodePro = "SourceCodeProBold.ttf"
    Squic = "squic.ttf"
    Squid = "squid.ttf"

    # Path to assets
    background = "background.jpg"

    # Encryption method
    def encrypt(self, textinput):

        # Generates key for encryption and decryption
        key = Fernet.generate_key()
        farnet = Fernet(key)

        try:
            # Check message is empty or not
            if textinput.text != "":
                message = textinput.text
            else:
                raise

            # Encrypt message
            encMessage = farnet.encrypt(message.encode())

            # Get result and copy it to clipboard
            result = f"Encrypted Message: \n{encMessage.decode('utf-8')}\n\nDecryption Key: \n{key.decode('utf-8')}"
            Clipboard.copy(result)

            # Show success popup
            popup = Factory.SuccessPopup()
            popup.open()

        # If any error -> Show error popup
        except Exception:
            popup = Factory.EncryptionErrorPopup()
            popup.open()

    # Decryption method
    def decrypt(self, textinput, passwordinput):

        # Get key for encryption and decryption
        key = bytes(passwordinput.text, encoding="utf8")
        msg = bytes(textinput.text, encoding="utf8")

        try:
            # Check key is empty or not
            if key != "":
                farnet = Fernet(key)
            else:
                raise

            # Decrypt message
            decMessage = farnet.decrypt(msg).decode()

            # Get result and copy it to clipboard
            result = f"Decrypted Message: \n{decMessage}"
            Clipboard.copy(result)

            # Show success popup
            popup = Factory.SuccessPopup()
            popup.open()

        # If any error -> Show error popup
        except Exception:
            popup = Factory.DecryptionErrorPopup()
            popup.open()


# Main class
class CryptoKo(App):

    # Build method
    def build(self):

        # Root screen
        root = ScreenManager()

        # Main menu screen
        self.StartMenuScreen = StartMenuScreen(name="StartMenu")
        root.add_widget(self.StartMenuScreen)

        # Set current screen to main menu and return root
        root.current = "StartMenu"
        return root


# Run App
CryptoKo().run()

# End of file
