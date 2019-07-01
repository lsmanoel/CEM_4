# Exemplo:
teams = list()
planes = list()


#---------------------------------------------------------------------------------------------------------------------------------------
# Lucas e João:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20%20plane_bottom_24_MHz.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20plane_top_24_MHz.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20plane_bottom_500_KHz.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20plane_top_500_KHz.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20mag_plane_bottom_24_MHz.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20mag_plane_top_24_MHz.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Lucas', 'João'],
    board_number=2,
    planes=planes
))

#---------------------------------------------------------------------------------------------------------------------------------------
# Botelho:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/botelho/5%20-%2015M_Alta_Impedancia_Plano.csv',
    signal_frequency='15 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/botelho/5%20-%2015M_Alta_Impedancia_Trilha.csv',
    signal_frequency='15 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/botelho/5%20-%20200k_Alta_Impedancia_Plano.csv',
    signal_frequency='200 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/botelho/5%20-%20200k_Alta_Impedancia_Trilha.csv',
    signal_frequency='200 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/botelho/5%20-%2015M_H_Field_Plano.csv',
    signal_frequency='15 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/botelho/5%20-%2015M_H_Field_Trilha.csv',
    signal_frequency='15 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Botelho', ' '],
    board_number=2,
    planes=planes
))

#---------------------------------------------------------------------------------------------------------------------------------------
# Federico e Gustavo:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_Alta_Impedancia_Referencia.csv',
    signal_frequency='15 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_Alta_Impedancia_Trilha.csv',
    signal_frequency='15 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/200k_Alta_Impedancia_Referencia.csv',
    signal_frequency='200 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/200k_Alta_Impedancia_Trilha.csv',
    signal_frequency='200 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_H_Field_Referencia.csv',
    signal_frequency='15 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_H_Field_Trilha.csv',
    signal_frequency='15 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Botelho'],
    board_number=2,
    planes=planes
))

#---------------------------------------------------------------------------------------------------------------------------------------
# Federico e Gustavo:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_Alta_Impedancia_Referencia.csv',
    signal_frequency='15 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_Alta_Impedancia_Trilha.csv',
    signal_frequency='15 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/200k_Alta_Impedancia_Referencia.csv',
    signal_frequency='200 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/200k_Alta_Impedancia_Trilha.csv',
    signal_frequency='200 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_H_Field_Referencia.csv',
    signal_frequency='15 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/federico_gustavo/15M_H_Field_Trilha.csv',
    signal_frequency='15 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Federico', 'Gustavo'],
    board_number=2,
    planes=planes
))

#---------------------------------------------------------------------------------------------------------------------------------------
# Ian e Cleisson:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_baixo_Z.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_cima_Z.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%20500k_baixo_Z.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%20500k_cima_Z.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_cima_H.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_baixo_H.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Iam', 'Cleisson'],
    board_number=2,
    planes=planes
))

plot(teams, 'ELC')

#---------------------------------------------------------------------------------------------------------------------------------------
# Ian e Cleisson:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_baixo_Z.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_cima_Z.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%20500k_baixo_Z.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%20500k_cima_Z.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_cima_H.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/ian_cleissom/1%20-%2024M_baixo_H.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Iam', 'Cleisson'],
    board_number=2,
    planes=planes
))

#---------------------------------------------------------------------------------------------------------------------------------------
# Luiz e Matheus:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/luiz_matheus/medicao_placa_L_Med_plan_cima_24m.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/luiz_matheus/medicao_placa_L_Med_plan_cima_24m.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/luiz_matheus/medicao_placa_L_Med_plan_cima_500k.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/luiz_matheus/medicao_placa_L_Med_plan_cima_500k.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/luiz_matheus/medicao_placa_L_Med_variando_trilha_cima_24m.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/luiz_matheus/medicao_placa_L_Med_variando_trilha_cima_24m.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Iam', 'Cleisson'],
    board_number=2,
    planes=planes
))

#---------------------------------------------------------------------------------------------------------------------------------------
# Wellington e Gabriel:
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/wellington_gabriel/PLACA_03_campo_eletrico_ref_24MHz.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/wellington_gabriel/PLACA_03_campo_eletrico_trilha_L_24MHz.csv',
    signal_frequency='24 MHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/wellington_gabriel/PLACA_03_campo_eletrico_ref_500kHz.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/wellington_gabriel/PLACA_03_campo_eletrico_trilha_L_500kHz.csv',
    signal_frequency='500 KHz',
    probe_type='ELC',
    pcb_side='top'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/wellington_gabriel/PLACA_03_campo_mag_ref_24MHz.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='bottom'
))
planes.append(plane(
    url_of_csv_file='https://raw.githubusercontent.com/lsmanoel/CEM_4/master/CEM_4_2019_1/wellington_gabriel/PLACA_03_campo_mag_trilha_L_24MHz.csv',
    signal_frequency='24 MHz',
    probe_type='MAG',
    pcb_side='top'
))

teams.append(team(
    team_members=['Wellington', 'Gabriel'],
    board_number=2,
    planes=planes
))

plot(teams, 'ELC')