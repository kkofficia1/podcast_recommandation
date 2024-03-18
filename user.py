class User():
    def __init__(self, name="user", age=0) -> None:
      self.name = name
      self.age = age
      self.known_podcasts = []
      self.languages = []
    
    def get_name(self):
      print("Your name is currently {0}".format(self.name))
      change_name = input("Do you want to change that? y/n ")
      if change_name == "y":
         self.name = input("What is your name? ")
         return self.name
      else:
         return self.name


    def get_languages(self):
      new_language = True
      while True:
         language_spoken = input("Which language do you speak? Please name one. ")
         language_to_append = language_spoken.lower()
         self.languages.append(language_to_append)
         another_one = input("Do you speak another language? y/n ")
         if another_one =="y":
            continue
         else:
            new_language = False
         return self.languages