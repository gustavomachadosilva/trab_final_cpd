import customtkinter
from tkinter import ttk
from controller.structureBuilder import *
from model.basic.movie import *
from model.basic.user import *
from model.basic.rating import *


class App(customtkinter.CTk):
    
    def __init__(self, structureBuilder,fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.structureBuilder: StructureBuilder = structureBuilder

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

        self.button = customtkinter.CTkButton(self.frame, text="my button", command=self.button_firstResearch)
        self.button.pack(padx=20, pady=20)

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
        

    def button_callbck(self):
        print("button clicked")
        for i in range(100):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(f"Dado {i}", f"Dado {i+1}"), tags=(tag,))
    
    def button_action(self):
        
        x = 0

        for i in self.structureBuilder.hashMovie.linkedLists:
            current = i.head

            while (current != None):
                movie: Movie = current.value
                rating = movie.getGlobalRating()
                tag = "evenrow" if x % 2 == 0 else "oddrow"
                x += 1
                self.tree.insert("", "end", values=(movie.id, movie.title, movie.genres, movie.year, f"{rating:.6f}", movie.ratingsCounter), tags=(tag,))
                current = current.next
    
    def button_firstResearch(self):
        x = 0
        moviesList = []
        for id in self.structureBuilder.trieMovies.search_prefix("America"):
            movie: Movie = self.structureBuilder.hashMovie.findById(id)
            if movie:
                moviesList.append(movie)

        selection_sort_movies_by_global_rating(moviesList)

        for movie in moviesList:
            tag = "evenrow" if x % 2 == 0 else "oddrow"
            x += 1
            self.tree.insert("", "end", values=(movie.id, movie.title, movie.genres, movie.year, format(movie.getGlobalRating(), ".6f"), movie.ratingsCounter, '-'), tags=(tag,))
                
    def button_secondResearch(self):
        x = 0
        moviesList = []

        user: User = self.structureBuilder.hashUser.findById(54766)
        if user is None:
            print("Usuário não encontrado!")
            return

        for rating in user.ratings:
            movie: Movie = self.structureBuilder.hashMovie.findById(rating.movieId)
            if movie:
                moviesList.append((movie, rating.value))

        selection_sort_by_rating_then_global(moviesList)     
        moviesList = moviesList[:20]

        for movie, userRating in moviesList:
            tag = "evenrow" if x % 2 == 0 else "oddrow"
            x += 1
            self.tree.insert("", "end", values=(movie.id, movie.title, movie.genres, movie.year, format(movie.getGlobalRating(), ".6f"), movie.ratingsCounter, userRating), tags=(tag,))

    def button_fourthResearch(self):
        x = 0
        moviesList = []

        stringTagSearch = "'feel good' 'predictable'"
        parts = stringTagSearch.split("'")
        tagTerms = [part for i, part in enumerate(parts) if i % 2 == 1]

        idsList = self.structureBuilder.trieTags.search_string(tagTerms.pop())
        for term in tagTerms:
            idsList = list(set(idsList) & set(self.structureBuilder.trieTags.search_string(term)))


        for id in idsList:
            movie: Movie = self.structureBuilder.hashMovie.findById(id)
            if movie:
                moviesList.append(movie)

        selection_sort_movies_by_global_rating(moviesList)

        for movie in moviesList:
            tag = "evenrow" if x % 2 == 0 else "oddrow"
            x += 1
            self.tree.insert("", "end", values=(movie.id, movie.title, movie.genres, movie.year, format(movie.getGlobalRating(), ".6f"), movie.ratingsCounter, '-'), tags=(tag,))


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

    