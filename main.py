import tkinter as tk
import customtkinter as ctk

# Инициализация библиотеки CustomTkinter
ctk.set_appearance_mode("dark")  # Установка темного режима
ctk.set_default_color_theme("green")  # Установка цветовой темы

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройка основного окна
        self.title("Dolphin")
        self.configure(bg="#1C1C1C")  # Установка цвета фона для окна
        self.attributes("-alpha", 1.0)  # Установка полной непрозрачности окна

        # Размеры экрана и окна
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 1280
        window_height = 720

        # Рассчет положения окна по центру экрана
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Установка геометрии окна
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Создание фреймов для сайдбара и основного контента
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#2A2A2A")
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")

        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#1C1C1C")
        self.main_frame.grid(row=0, column=1, sticky="nswe")

        # Настройка ресайза сетки
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Создание шрифтов Arial Black с помощью CTkFont
        custom_font = ctk.CTkFont(family='Arial Black', size=12)
        custom_font_big = ctk.CTkFont(family='Arial Black', size=30)

        # Создание метки для содержимого в основном фрейме
        self.content_label = ctk.CTkLabel(self.main_frame, text="", font=custom_font_big)
        self.content_label.grid(row=0, column=0, padx=20, pady=20)

        # Добавление раздела "О нас"
        self.about_us_label = ctk.CTkLabel(self.main_frame, text="О нас:\n\nЯ ЕБЛАНZZZZZZZZZZZ ZOV ZOV",
                                          font=custom_font)
        self.about_us_label.grid(row=0, column=0, padx=20, pady=20)
        self.about_us_label.grid_remove()  # Скрыть блок "О нас" по умолчанию

        # Добавление кнопок в сайдбар
        self.home_button = ctk.CTkButton(self.sidebar_frame, text="Home", font=custom_font, command=self.home_button_event)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        self.search_button = ctk.CTkButton(self.sidebar_frame, text="Library", font=custom_font, command=self.search_button_event)
        self.search_button.grid(row=2, column=0, padx=20, pady=10)

        self.settings_button = ctk.CTkButton(self.sidebar_frame, text="Settings", font=custom_font, command=self.settings_button_event)
        self.settings_button.grid(row=4, column=0, padx=20, pady=10)

        # Создание кнопки Toggle Transparency, но не отображать её сразу
        self.transparency_button = ctk.CTkButton(self.main_frame, text="Trans+", font=custom_font, command=self.toggle_transparency)
        self.transparency_button.grid(row=1, column=0, padx=20, pady=10)
        self.transparency_button.grid_remove()  # Скрыть кнопку по умолчанию

        # Метка для отображения состояния кнопки
        self.transparency_status_label = ctk.CTkLabel(self.main_frame, text="", font=custom_font)
        self.transparency_status_label.grid(row=2, column=0, padx=20, pady=10)

    def home_button_event(self):
        self.content_label.configure(text="Home")
        self.hide_transparency_button()
        self.hide_about_us()  # Скрыть раздел "О нас"

    def search_button_event(self):
        self.content_label.configure(text="Library")
        self.hide_transparency_button()
        self.hide_about_us()  # Скрыть раздел "О нас"

    def settings_button_event(self):
        self.content_label.configure(text="Settings")
        self.show_transparency_button()
        self.hide_about_us()  # Скрыть раздел "О нас"

    def toggle_transparency(self):
        current_alpha = float(self.attributes("-alpha"))
        new_alpha = 0.95 if current_alpha == 1.0 else 1.0
        self.attributes("-alpha", new_alpha)
        self.update_transparency_status()

    def show_transparency_button(self):
        self.transparency_button.configure(text="+")
        self.transparency_button.grid()
        self.update_transparency_status()

    def hide_transparency_button(self):
        self.transparency_button.grid_remove()

    def update_transparency_status(self):
        current_alpha = float(self.attributes("-alpha"))
        if current_alpha == 1.0:
            self.transparency_button.configure(text="Trans+")
        else:
            self.transparency_button.configure(text="Trans-")

    def show_about_us(self):
        self.about_us_label.grid()

    def hide_about_us(self):
        self.about_us_label.grid_remove()

if __name__ == "__main__":
    app = App()
    app.mainloop()
