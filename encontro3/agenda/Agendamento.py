# -*- coding: utf-8 -*-

class PraiaError(Exception):
    pass


class Agendamento:
    def __init__(self):
        self.agendamentos = []
    
    def agendar(self, nome_cliente, dia_semana, hora_inicio=9, duracao=1):
        if dia_semana == 0:
            raise PraiaError('Segunda-feira não possui agendamentos')
        if dia_semana == 1:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    self.agendamentos.append((nome_cliente, hora_inicio, _hora_termino))
                    return
            raise PraiaError('Agendamento inválido para terça-feira')
        if dia_semana == 2:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    self.agendamentos.append((nome_cliente, hora_inicio, _hora_termino))
                    return
            raise PraiaError('Agendamento inválido para quarta-feira')
        if dia_semana == 3:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    self.agendamentos.append((nome_cliente, hora_inicio, _hora_termino))
                    return
            raise PraiaError('Agendamento inválido para quinta-feira')
        if dia_semana == 4:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    self.agendamentos.append((nome_cliente, hora_inicio, _hora_termino))
                    return
            raise PraiaError('Agendamento inválido para sexta-feira')
        if dia_semana == 5:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    self.agendamentos.append((nome_cliente, hora_inicio, _hora_termino))
                    return
            raise PraiaError('Agendamento inválido para sábado')
        if dia_semana == 6:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 18:
                if 10 <= _hora_termino <= 18:
                    self.agendamentos.append((nome_cliente, hora_inicio, _hora_termino))
                    return
            raise PraiaError('Agendamento inválido para domingo')




    def __str__(self):
        return "Agendamento"
    
    def __repr__(self):
        return str(self)