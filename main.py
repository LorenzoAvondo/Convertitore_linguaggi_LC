import customtkinter as ctk
from encoders import farfallese
# Configurazione tema
ctk.set_appearance_mode("System")  # "Dark" o "Light"
ctk.set_default_color_theme("blue")

class TextCoderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Text Coder App")
        self.geometry("600x400")

        # Titolo
        self.title_label = ctk.CTkLabel(self, text="🔤 Text Coder", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # Input testo
        self.input_label = ctk.CTkLabel(self, text="Inserisci il testo:")
        self.input_label.pack(pady=(10, 0))
        self.input_text = ctk.CTkTextbox(self, height=100)
        self.input_text.pack(padx=20, pady=5, fill="both")

        # Scelta linguaggio
        self.lang_label = ctk.CTkLabel(self, text="Seleziona il linguaggio in codice:")
        self.lang_label.pack(pady=(10, 0))
        self.lang_option = ctk.CTkOptionMenu(self, values=["Morse", "Cesare", "Reverse", "Farfallese"])
        self.lang_option.pack(pady=5)

        # Bottone per tradurre
        self.translate_button = ctk.CTkButton(self, text="Traduci", command=self.translate_text)
        self.translate_button.pack(pady=10)

        # Output
        self.output_label = ctk.CTkLabel(self, text="Risultato:")
        self.output_label.pack(pady=(10, 0))
        self.output_text = ctk.CTkTextbox(self, height=100)
        self.output_text.pack(padx=20, pady=5, fill="both")

    def translate_text(self):
        text = self.input_text.get("1.0", "end-1c")
        lang = self.lang_option.get()

        if not text.strip():
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "⚠️ Inserisci un testo prima di tradurre!")
            return

        # Logica di traduzione per i linguaggi
        if lang == "Farfallese":
            translated = farfallese.encode(text)
        elif lang == "Reverse":
            translated = text[::-1]
        else:
            translated = f"[{lang}] → (non ancora implementato)"

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translated)

if __name__ == "__main__":
    app = TextCoderApp()
    app.mainloop()
