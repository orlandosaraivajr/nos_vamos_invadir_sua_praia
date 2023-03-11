# -*- coding: utf-8 -*-

from abc import abstractmethod, ABC

class PraiaError(Exception):
    pass

class StrategyAgendamento(ABC):
    @abstractmethod
    def agendar(self, nome_cliente, dia_semana, hora_inicio=9, duracao=1):
        pass


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


class StrategyAgendamentoQuarta(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=2, hora_inicio=9, duracao=1):
        _hora_termino = hora_inicio + duracao
        if 10 <= hora_inicio <= 22:
            if 10 <= _hora_termino <= 22:
                return ((nome_cliente, hora_inicio, _hora_termino))
        raise PraiaError('Agendamento inválido para quarta-feira')


class StrategyAgendamentoQuinta(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=3, hora_inicio=9, duracao=1):
        _hora_termino = hora_inicio + duracao
        if 10 <= hora_inicio <= 22:
            if 10 <= _hora_termino <= 22:
                return ((nome_cliente, hora_inicio, _hora_termino))
        raise PraiaError('Agendamento inválido para quinta-feira')


class StrategyAgendamentoSexta(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=4, hora_inicio=9, duracao=1):
        _hora_termino = hora_inicio + duracao
        if 10 <= hora_inicio <= 22:
            if 10 <= _hora_termino <= 22:
                return ((nome_cliente, hora_inicio, _hora_termino))
        raise PraiaError('Agendamento inválido para sexta-feira')


class StrategyAgendamentoSabado(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=5, hora_inicio=9, duracao=1):
        _hora_termino = hora_inicio + duracao
        if 10 <= hora_inicio <= 22:
            if 10 <= _hora_termino <= 22:
                return ((nome_cliente, hora_inicio, _hora_termino))
        raise PraiaError('Agendamento inválido para sábado')


class StrategyAgendamentoDomingo(StrategyAgendamento):
    def agendar(self, nome_cliente, dia_semana=6, hora_inicio=9, duracao=1):
        _hora_termino = hora_inicio + duracao
        if 10 <= hora_inicio <= 18:
            if 10 <= _hora_termino <= 18:
                return ((nome_cliente, hora_inicio, _hora_termino))
        raise PraiaError('Agendamento inválido para domingo')

class DadosCliente:
    def __init__(self,nome_cliente, dia_semana,hora_inicio=9, duracao=1):
        self.nome_cliente = nome_cliente
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.duracao = duracao

        
class Agendamento:
    def __init__(self):
        self.agendamentos = []
    
    def agendar(self, dados_cliente , estrategia=None):
        if isinstance(estrategia, StrategyAgendamento):
            _inner_strategy = estrategia
            self.agendamentos.append(_inner_strategy.agendar(dados_cliente.nome_cliente, dados_cliente.dia_semana, dados_cliente.hora_inicio, dados_cliente.duracao))
            return True
        raise PraiaError('Estratégia inválida')

    def __str__(self):
        return "Agendamento"
    
    def __repr__(self):
        return str(self)


mapeamento_estrategias = {}
mapeamento_estrategias[0] = StrategyAgendamentoSegunda() 
mapeamento_estrategias[1] = StrategyAgendamentoTerca()
mapeamento_estrategias[2] = StrategyAgendamentoQuarta()
mapeamento_estrategias[3] = StrategyAgendamentoQuinta()
mapeamento_estrategias[4] = StrategyAgendamentoSexta()
mapeamento_estrategias[5] = StrategyAgendamentoSabado()
mapeamento_estrategias[6] = StrategyAgendamentoDomingo()