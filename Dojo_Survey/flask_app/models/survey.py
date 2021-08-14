from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Survey(): 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.locaiton = data['location']
        self.comment = data['comment']
        self.weekend = data['weekend']
        self.dessert = data['dessert']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_information(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, weekend, dessert, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, %(weekend)s, %(dessert)s, NOW(), NOW());"
        print(data)
        modified_data = {
            'name': data['name'],
            'location': data['location'],
            'language': data['language'],
            'comment': data['comment'],
            'weekend': data['day'],
        }
        desserts = ''
        for dessert in data.getlist('dessert'):
            desserts = desserts + ',' + dessert
        modified_data['dessert'] = desserts


        

        connection = connectToMySQL('dojos_survey_schema')
        results = connection.query_db(query, modified_data)

        return results


    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 5:
            flash('Name must be at least 5 characters')
            is_valid = False
        if len(survey['language']) < 1:
            flash('Language must be seleceted')
            is_valid = False
        if len(survey['location']) <1:
            flash('Location must be selected')
            is_valid = False
        if len(survey['day'])< 1:
            flash('Favorite day must be selected')
            is_valid = False
        if len(survey['dessert']) < 1:
            flash('At least one dessert must be selected')
            is_valid = False
        return is_valid
