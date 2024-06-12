class ContactList:
    def __init__(self, list_name, contacts):
        self._list_name = list_name
        self._contacts = contacts

        self._contact_list = sorted(contacts, key = lambda x: x['name'])

    @property
    def get_contacts(self):
        return self._contact_list
    
    def add_contact(self, new_contacts):
        self._contact_list.append(new_contacts)
        self._contact_list = sorted(self._contact_list, key = lambda x: x['name'])
        
    def remove_contact(self, remove):
        remove = remove.title()
        self._contact_list = [contact for contact in self._contact_list if contact['name'] != remove]

    @get_contacts.setter
    def set_contacts(self, l):
        self._contact_list = l

    @property
    def get_name(self):
        name = self._contact_list[0]['name']
        return name

    @get_name.setter
    def set_name(self, name):
        new_contact = {'name': name}
        self._contact_list.append(new_contact)
    
    def find_shared_contacts(self, dict_list):
        dict_list = dict_list.get_contacts
        shared_contacts = []
        for contact1 in dict_list:
            for contact2 in self._contact_list:
                if contact1['name'] == contact2['name'] and contact1['number'] == contact2['number']:
                    shared_contacts.append(contact1)
        return shared_contacts

