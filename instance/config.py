# import os 
class Config():
	debug = False

class DevelopmentConfig(Config):
	debug= True

class TestingConfig(Config):
    '''Testing app configurations'''
    TESTING = True
    DEBUG = True

app_configuration={
	"development" : DevelopmentConfig,
	"testing": TestingConfig,
}