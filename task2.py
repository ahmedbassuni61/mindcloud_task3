class Voting():
    def __init__(self,Type_of_election):
        self.__Type_of_election=Type_of_election
        self.__canditates={}
    def add_candidate(self,new_name):
        if new_name not in self.__canditates:
            self.__canditates[new_name]=0
            print(f"Canditate {new_name} added")
        else:
            print("Already exists")

    def remove_candidate(self,removed_name):
        if removed_name in self.__canditates:
            self.__canditates.pop(removed_name)
            print(f"Canditate {removed_name} removed")
        else:
            print(f"Removed canditate {removed_name} Doesn't exist")

    def vote_to_candidate(self,voted_name):
        if voted_name in self.__canditates:
            self.__canditates[voted_name]+=1
            print(f"voted {voted_name}")
        else:
            print("Not found")

    def display_the_Winner(self):
        max_item = max(self.__canditates.items(), key=lambda item: item[1])
        print(f"{max_item[0]} Won With {max_item[1]} Votes")
voting_system=Voting("Cat Election")
voting_system.add_candidate("Misho")
voting_system.add_candidate("Misho")
voting_system.add_candidate("bsbs")
voting_system.remove_candidate("rex")
voting_system.vote_to_candidate("Misho")
voting_system.vote_to_candidate("Misho")
voting_system.vote_to_candidate("bsbs")
voting_system.vote_to_candidate("rex")
voting_system.display_the_Winner()