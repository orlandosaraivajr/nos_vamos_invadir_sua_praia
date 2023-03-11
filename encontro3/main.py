# -*- coding: utf-8 -*-

from agenda.Agendamento import Agendamento, DadosCliente
from agenda.Agendamento import StrategyAgendamentoSegunda, StrategyAgendamentoTerca
from agenda.Agendamento import StrategyAgendamentoQuarta, StrategyAgendamentoQuinta
from agenda.Agendamento import StrategyAgendamentoSexta, StrategyAgendamentoSabado
from agenda.Agendamento import StrategyAgendamentoDomingo
from agenda.Agendamento import mapeamento_estrategias

agendamento = Agendamento()
cliente1 = DadosCliente('Cliente1' ,5 ,11 ,1 )
cliente2 = DadosCliente('Cliente2' ,5 ,13 ,3 )

agendamento.agendar(cliente1, StrategyAgendamentoSabado())
agendamento.agendar(cliente2, StrategyAgendamentoSabado())

agendamento.agendar(cliente1, mapeamento_estrategias[cliente1.dia_semana])