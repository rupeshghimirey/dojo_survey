
from mysqlconnection import connectToMySQL
from flask import flash
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @staticmethod
    def validate_dojo(form_data):
        is_valid = True;
        if len(form_data['name']) < 4:
            flash("Name must be atleast 4 charcaters long")
            is_valid = False;
        if len(form_data['comments']) < 4:
            flash("comments must be atleast 4 characters long.")
            is_valid = False;
        if len(form_data['dojo_location']) <1:
            flash("Please select the location!")
            is_valid = False;
        if len(form_data['dojo_language']) <1:
            flash("Please select the language!")
            is_valid = False;

        return is_valid;
        

    @classmethod
    def get_all_dojos(cls):

        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos(name, location, language, comments, created_at, updated_at) VALUES(%(name)s, %(location)s,%(language)s, %(comments)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey').query_db( query, data )