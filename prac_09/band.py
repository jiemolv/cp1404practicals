class Band:
    """Band class for storing details of a band."""
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        member_details = ','.join(str(member) for member in self.members)
        return f"{self.name} ({member_details}"

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def paly(self):
        """Show the musicians playing their instruments."""
        for member in self.members:
            print(member.play())