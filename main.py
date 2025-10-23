import customtkinter as ctk
from encoders import farfallese, morse, cesare

# Configurazione tema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class TextCoderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Codificatore")
        self.geometry("600x540")

        # Titolo principale
        self.title_label = ctk.CTkLabel(self, text="🔤 Text Coder", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # Input testo
        self.input_label = ctk.CTkLabel(self, text="Inserisci il testo:")
        self.input_label.pack(pady=(10, 0))
        self.input_text = ctk.CTkTextbox(self, height=100)
        self.input_text.pack(padx=20, pady=5, fill="both")

        # --- Selettore modalità (Encode / Decode) ---
        self.mode_var = "encode"

        self.mode_frame = ctk.CTkFrame(self)
        self.mode_frame.pack(pady=10)

        self.encode_button = ctk.CTkButton(
            self.mode_frame, text="🔒 Codifica", width=130,
            command=lambda: self.set_mode("encode")
        )
        self.encode_button.grid(row=0, column=0, padx=8)

        self.decode_button = ctk.CTkButton(
            self.mode_frame, text="🔓 Decodifica", width=130,
            command=lambda: self.set_mode("decode")
        )
        self.decode_button.grid(row=0, column=1, padx=8)

        self.set_mode("encode")

        # --- Selettore linguaggio ---
        self.lang_label = ctk.CTkLabel(self, text="Seleziona il tipo di codice:")
        self.lang_label.pack(pady=(10, 0))

        self.lang_option = ctk.CTkOptionMenu(
            self,
            values=["Morse", "Cesare", "Reverse", "Farfallese"],
            command=self.on_lang_change
        )
        self.lang_option.pack(pady=5)

        # --- Campo extra per "Cesare" ---
        self.shift_frame = ctk.CTkFrame(self) # <-- Crea il frame
        self.shift_label = ctk.CTkLabel(self.shift_frame, text="Spostamento lettere:")
        self.shift_entry = ctk.CTkEntry(self.shift_frame, width=100, placeholder_text="3")
        
        # Ora che il frame esiste, possiamo chiamare la funzione di aggiornamento
        self.on_lang_change(self.lang_option.get())

        # inizialmente nascosto
        self.shift_frame.pack_forget()

        # Ora che il frame esiste, possiamo chiamare la funzione di aggiornamento
        self.on_lang_change(self.lang_option.get())

        # --- Bottone esecuzione ---
        self.translate_button = ctk.CTkButton(
            self, text="⚙️ Esegui", command=self.translate_text, width=180, height=40
        )
        self.translate_button.pack(pady=15)

        # --- Output ---
        self.output_label = ctk.CTkLabel(self, text="Risultato:")
        self.output_label.pack(pady=(10, 0))
        self.output_text = ctk.CTkTextbox(self, height=100)
        self.output_text.pack(padx=20, pady=5, fill="both")

    def set_mode(self, mode: str):
        self.mode_var = mode
        if mode == "encode":
            self.encode_button.configure(fg_color="#1f6aa5")
            self.decode_button.configure(fg_color="gray30")
        else:
            self.decode_button.configure(fg_color="#1f6aa5")
            self.encode_button.configure(fg_color="gray30")

    def on_lang_change(self, choice=None):
        current = (choice or "").strip().lower()

        if current == "cesare":
            # ... (grid interni come prima)
            self.shift_label.grid(row=0, column=0, padx=(0, 10))
            self.shift_entry.grid(row=0, column=1)

            # 💡 USA place() invece di pack()
            # Posiziona il frame al centro della finestra, al di sotto del menu
            self.shift_frame.place(relx=0.5, rely=0.6, anchor=ctk.CENTER) 
            
            self.update() # Forziamo l'aggiornamento
            
            # ... (inserimento "3.0" come prima)

        else:
            if self.shift_frame.winfo_manager() == "place":
                # 💡 USA place_forget() invece di pack_forget()
                self.shift_frame.place_forget()
                self.update()

    def translate_text(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        lang = self.lang_option.get()
        mode = self.mode_var

        if not text:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "⚠️ Inserisci un testo prima di procedere!")
            return

        try:
            if lang == "Farfallese":
                translated = farfallese.encode(text) if mode == "encode" else farfallese.decode(text)
            elif lang == "Morse":
                translated = morse.encode(text) if mode == "encode" else morse.decode(text)
            elif lang == "Reverse":
                translated = text[::-1]
            elif lang == "Cesare":
                shift_value = self.shift_entry.get().strip()
                shift = int(shift_value) if shift_value else 3
                if mode == "encode":
                    translated = cesare.encode(text, shift)
                else:
                    translated = cesare.decode(text, shift)
            else:
                translated = f"[{lang}] → non implementato"
        except Exception as e:
            translated = f"❌ Errore: {e}"

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translated)


if __name__ == "__main__":
    app = TextCoderApp()
    app.mainloop()
