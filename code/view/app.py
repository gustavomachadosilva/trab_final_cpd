import customtkinter
from tkinter import ttk
from controller.structureBuilder import *
from controller.search import *
from model.basic.movie import *
from model.basic.user import *
from model.basic.rating import *


class App(customtkinter.CTk):
    
    def __init__(self, structureBuilder,fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.structureBuilder: StructureBuilder = structureBuilder
        self.search = Search(structureBuilder)

        customtkinter.set_appearance_mode("dark")

        self.title("Movies")
        self.geometry("1400x800")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsew")

        self.frame2 = customtkinter.CTkFrame(self)
        self.frame2.grid(row=0, column=1, padx=(0,10), pady=(10,10),sticky="nsew")

        self.entrySerachByPrefix = customtkinter.CTkEntry(self.frame, placeholder_text="Prefix")
        self.entrySerachByPrefix.pack(padx=10, pady=(20,5))
        self.buttonSerachByPrefix = customtkinter.CTkButton(self.frame, text="Search by prefix", command=self.buttonSearchByPrefixAction)
        self.buttonSerachByPrefix.pack(padx=10, pady=0)

        self.entrySerachByUserId = customtkinter.CTkEntry(self.frame, placeholder_text="User Id")
        self.entrySerachByUserId.pack(padx=10, pady=(40,5))
        self.buttonSerachByUserId = customtkinter.CTkButton(self.frame, text="Search by user id", command=self.buttonSearchByUserIdAction)
        self.buttonSerachByUserId.pack(padx=10, pady=0)

        self.entrySerachByGenreN = customtkinter.CTkEntry(self.frame, placeholder_text="Max")
        self.entrySerachByGenreN.pack(padx=10, pady=(40,5))
        self.entrySerachByGenre = customtkinter.CTkEntry(self.frame, placeholder_text="Genre")
        self.entrySerachByGenre.pack(padx=10, pady=(0,5))
        self.buttonSerachByGenre = customtkinter.CTkButton(self.frame, text="Search by genre", command=self.buttonSearchByGenreAction)
        self.buttonSerachByGenre.pack(padx=10, pady=0)

        self.entrySerachByTags = customtkinter.CTkEntry(self.frame, placeholder_text="'tag1','tag2'...")
        self.entrySerachByTags.pack(padx=10, pady=(40,5))
        self.buttonSerachByTags = customtkinter.CTkButton(self.frame, text="Search by tags", command=self.buttonSearchByTagsAction)
        self.buttonSerachByTags.pack(padx=10, pady=0)

        self.style = ttk.Style()
        self.configure_treeview_style()

        self.tree = ttk.Treeview(self.frame2, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"), show="headings", style="Custom.Treeview", selectmode="browse")
        self.tree.heading("col1", text="movieId")
        self.tree.heading("col2", text="title")
        self.tree.heading("col3", text="genres")
        self.tree.heading("col4", text="year")
        self.tree.heading("col5", text="global_rating")
        self.tree.heading("col6", text="count")
        self.tree.heading("col7", text="rating")

        self.tree.column("col1", width=30, anchor="center")    # movieId
        self.tree.column("col2", width=340, anchor="w")        # title
        self.tree.column("col3", width=290, anchor="w")        # genres
        self.tree.column("col4", width=30, anchor="center")    # year
        self.tree.column("col5", width=60, anchor="center")   # rating
        self.tree.column("col6", width=30, anchor="center")    # count
        self.tree.column("col7", width=30, anchor="center")    # count
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        

        # Aplicar estilos às tags
        self.tree.tag_configure("evenrow", background=self.row_color_even, foreground=self.fg_color)
        self.tree.tag_configure("oddrow", background=self.row_color_odd, foreground=self.fg_color)
    
    
    def buttonSearchByPrefixAction(self):
        prefix = self.entrySerachByPrefix.get()
        moviesList = self.search.searchMoviesByPrefix(prefix)
        self.insertInTable(moviesList)

    def buttonSearchByUserIdAction(self):
        userId = int(self.entrySerachByUserId.get())
        moviesList = self.search.searchByUserId(userId)
        self.insertInTableRatingVersion(moviesList)

    def buttonSearchByGenreAction(self):
        max = int(self.entrySerachByGenreN.get())
        genre = self.entrySerachByGenre.get()
        moviesList = self.search.searchByGenre(max, genre)
        self.insertInTable(moviesList)

    def buttonSearchByTagsAction(self):
        listOfTags = self.entrySerachByTags.get()
        moviesList = self.search.searchByTags(listOfTags)
        self.insertInTable(moviesList)


    def insertInTable(self, moviesList):
        
        x = 0

        self.deleteTableData()

        for movie in moviesList:
            tag = "evenrow" if x % 2 == 0 else "oddrow"
            x += 1
            self.tree.insert("", "end", values=(movie.id, movie.title, movie.genres, movie.year, format(movie.getGlobalRating(), ".6f"), movie.ratingsCounter, '-'), tags=(tag,))
    
    def insertInTableRatingVersion(self, moviesList):

        x = 0

        self.deleteTableData()

        for movie, userRating in moviesList:
            tag = "evenrow" if x % 2 == 0 else "oddrow"
            x += 1
            self.tree.insert("", "end", values=(movie.id, movie.title, movie.genres, movie.year, format(movie.getGlobalRating(), ".6f"), movie.ratingsCounter, userRating), tags=(tag,))

    def deleteTableData(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


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

    