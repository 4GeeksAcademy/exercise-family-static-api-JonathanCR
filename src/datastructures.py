"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [

            {
                "first_name": "John Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },

            {
                "first_name": "Jane Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },

            {
                "first_name": "Jimmy Jackson",
                "age": 5,
                "lucky_numbers": 1
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
        index_to_delete = 0
        index = 0
        for member in self._members:
            member_id = member.get("id", None)
            if member_id == id:
                index_to_delete = index
                break
            index += 1
        
        del self._members[index_to_delete] 

    def get_member(self, id):
        found_member = None
        for member in self._members:
            member_id = member.get("id", None)
            if member_id == id:
                found_member = member
                break

        return found_member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members