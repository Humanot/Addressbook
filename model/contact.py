from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, photo=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, group=None, address2=None, phone2=None, notes=None, all_home_page_phones=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_home_page_phones = all_home_page_phones

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and (self.id is None or other.id is None or self.id == other.id)

    def max_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize