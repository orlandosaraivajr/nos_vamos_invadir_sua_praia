from agenda import Agenda

class TestAgenda:
    def test_class_declared(self):
        objeto = Agenda()
        assert isinstance(objeto, Agenda)
        assert isinstance(objeto.agendamentos, list)

    def test_str_repr(self):
        objeto = Agenda()
        assert 'Agenda' == str(objeto)
        assert 'Agenda' == repr(objeto)