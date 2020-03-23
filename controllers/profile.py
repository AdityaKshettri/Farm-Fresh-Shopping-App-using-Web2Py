def index(): 
    return dict(message="hello from profile.py")

@auth.requires_login()
def save():
    profilerows = db(db.profile.created_by==session.auth.user.id).select(orderby=~db.profile.id)
    for x in profilerows:
        db.profile.farm_name.default = x.farm_name
        db.profile.farm_address.default = x.farm_address
        db.profile.farm_website.default = x.farm_website
        break
    form = SQLFORM(db.profile).process()
    return locals()