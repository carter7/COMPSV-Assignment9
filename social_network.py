# social_network.py
# Author: Christian Carter
# Description: Models a social network using a graph data structure.

class Person:
    """Represents a person in the social network."""
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """Adds a friend to this person's friend list if not already a friend."""
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"{friend.name} is already friends with {self.name}.")


class SocialNetwork:
    """Represents a social network using an adjacency list (graph)."""
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """Adds a new person to the network."""
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        """Creates a bidirectional friendship between two people."""
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people do not exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        """Prints the network showing each person and their friends."""
        for name, person in self.people.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends_names)}")


# -------------------- Testing Section --------------------
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Create friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # non-existent
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()


# -------------------- Design Memo --------------------
"""
Design Memo: Why a Graph is the Right Choice
--------------------------------------------
A graph is the ideal data structure for modeling a social network because relationships between users are dynamic and bidirectional. Each person (node) can have multiple connections (edges) to others, and friendships can form or dissolve independently. Unlike lists or trees, graphs allow flexible many-to-many connections without a strict hierarchy.

A list could only store sequential data, making it inefficient for finding mutual friends or connecting users across the network. A tree, while useful for hierarchical data (like family trees or file systems), cannot represent circular or reciprocal relationships. For example, if Alex and Jordan are friends, both must reference each other—something that would violate a tree’s one-parent rule.

Using an adjacency list in the SocialNetwork class makes adding and finding friendships efficient and intuitive. The dictionary provides quick access (O(1) lookup) to each person, while each Person’s list of friends models their direct connections. One trade-off is that as the network grows, printing all connections or searching across multiple degrees of friendship can become slower (O(n + e)), but this is acceptable for most social applications. Overall, graphs provide the flexibility, clarity, and scalability required for a real-world social network system.
"""