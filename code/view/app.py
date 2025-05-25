import customtkinter
from tkinter import ttk

class App(customtkinter.CTk):
    
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        customtkinter.set_appearance_mode("dark")

        self.title("my app")
        self.geometry("1400x800")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsew")

        self.frame2 = customtkinter.CTkFrame(self)
        self.frame2.grid(row=0, column=1, padx=(0,10), pady=(10,10),sticky="nsew")

        self.button = customtkinter.CTkButton(self.frame, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

        self.style = ttk.Style()
        self.configure_treeview_style()

        self.tree = ttk.Treeview(self.frame2, columns=("col1", "col2"), show="headings", style="Custom.Treeview", selectmode="browse")
        self.tree.heading("col1", text="Column 1")
        self.tree.heading("col2", text="Column 2")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Inserir linhas com tags alternadas
        for i in range(100):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(f"Dado {i}", f"Dado {i+1}"), tags=(tag,))

        

        # Aplicar estilos às tags
        self.tree.tag_configure("evenrow", background=self.row_color_even, foreground=self.fg_color)
        self.tree.tag_configure("oddrow", background=self.row_color_odd, foreground=self.fg_color)
        

    def button_callbck(self):
        print("button clicked")
    
    def configure_treeview_style(self):
        mode = customtkinter.get_appearance_mode()

        if mode == "Dark":
            self.bg_color = "#2b2b2b"
            self.fg_color = "white"
            self.row_color_even = "#2f2f2f"
            self.row_color_odd = "#242424"
            header_bg = "#3a3a3a"
        else:
            self.bg_color = "white"
            self.fg_color = "black"
            self.row_color_even = "#f5f5f5"
            self.row_color_odd = "#e9e9e9"
            header_bg = "#dcdcdc"

        self.style.theme_use("default")

        self.style.configure("Custom.Treeview",
                             background=self.bg_color,
                             foreground=self.fg_color,
                             fieldbackground=self.bg_color,
                             rowheight=30,
                             font=("Arial", 12),
                             borderwidth=0)

        self.style.configure("Custom.Treeview.Heading",
                             background=header_bg,
                             foreground=self.fg_color,
                             font=("Arial", 13, "bold"),
                             borderwidth=0)

        self.style.map("Custom.Treeview",
                       background=[("selected", "#1f6aa5")],
                       foreground=[("selected", "white")])

    