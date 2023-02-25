# -*- coding: utf-8 -*-

class PraiaError(Exception):
    pass

class StrategyAgendamento:
    def agendar(self, nome_cliente, dia_semana, hora_inicio=9, duracao=1):
        if dia_semana == 2:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    return ((nome_cliente, hora_inicio, _hora_termino))
            raise PraiaError('Agendamento inválido para quarta-feira')
        if dia_semana == 3:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    return ((nome_cliente, hora_inicio, _hora_termino))
            raise PraiaError('Agendamento inválido para quinta-feira')
        if dia_semana == 4:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    return ((nome_cliente, hora_inicio, _hora_termino))
            raise PraiaError('Agendamento inválido para sexta-feira')
        if dia_semana == 5:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 22:
                if 10 <= _hora_termino <= 22:
                    return ((nome_cliente, hora_inicio, _hora_termino))
            raise PraiaError('Agendamento inválido para sábado')
        if dia_semana == 6:
            _hora_termino = hora_inicio + duracao
            if 10 <= hora_inicio <= 18:
                if 10 <= _hora_termino <= 18:
                   return ((nome_cliente, hora_inicio, _hora_termino))
            raise PraiaError('Agendamento inválido para domingo')


class StrategyAgendamentoSegunda(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=0, hora_inicio=9, duracao=1):
        raise PraiaError('Segunda-feira não possui agendamentos')

class StrategyAgendamentoTerca(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=1, hora_inicio=9, duracao=1):
        _hora_termino = hora_inicio + duracao
        if 10 <= hora_inicio <= 22:
            if 10 <= _hora_termino <= 22:
                return ((nome_cliente, hora_inicio, _hora_termino))
        raise PraiaError('Agendamento inválido para terça-feira')

class DadosCliente:
    def __init__(self,nome_cliente, dia_semana,hora_inicio=9, duracao=1):
        self.nome_cliente = nome_cliente
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.duracao = duracao

        
class Agendamento:
    def __init__(self):
        self.agendamentos = []
    
    def agendar(self, dados_cliente , estrategia=StrategyAgendamento()):
        _inner_strategy = estrategia
        self.agendamentos.append(_inner_strategy.agendar(dados_cliente.nome_cliente, dados_cliente.dia_semana, dados_cliente.hora_inicio, dados_cliente.duracao))
        return True

    def __str__(self):
        return "Agendamento"
    
    def __repr__(self):
        return str(self)