class movie:
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print("movie name: ",self.title)
        print("hero name: ",self.hero)
        print("heroine name: ",self.heroine)
        
list_of_movies=[]
while True:
    title=input("Enter the title name: ")
    hero=input("Enter the title name: ")
    heroine=input("Enter the title name: ")
    m=movie(title,hero,heroine)
    list_of_movies.append(m)
    print("movies are updated to the list")
    option=input("do you want to add another movie[Yes/no]")
    if option.lower()=='no':
        break
for movie in list_of_movies:
    movie.info()
    print()
        
        
    
    
    