import yaml, os
import  pymysql.cursors

with open(os.path.dirname(os.path.realpath(__file__)) + "/config.yml", 'r') as ymlfile:
    config = yaml.full_load(ymlfile)
    
#metodo para conecão com o banco


def getConnection():
    db = config['database']['database']
    return pymysql.connect(
                host=config['database']['host'],
                user=config['database']['user'],
                password=config['database']['password'],
                database=db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

def getLogging():
	