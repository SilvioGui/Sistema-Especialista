import yaml, os


with open(os.path.dirname(os.path.realpath(__file__)) + "/config.yml", 'r') as ymlfile:
    config = yaml.full_load(ymlfile)
    

#metodo para conecão com o banco
def getConnection():

#metodo para conecão com o log
def getLogging():
	
