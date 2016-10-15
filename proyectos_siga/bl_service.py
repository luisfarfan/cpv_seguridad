import proyectos_siga.service import App1Service

class App1Business(object):
    @staticmethod
    def do_create_person(param1,param2):
        # call methos
        data = {'dsd':'dssd'}
        return App1Service.do_create_person(params=data)


