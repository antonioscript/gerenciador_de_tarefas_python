import PySimpleGUI as sg

def criar_janela():
	sg.theme('DarkBlue4')
	linha = [
		[sg.Checkbox(''), sg.Input('')]
	]
	
	layout = [
		[sg.Frame('Tarefas', layout = linha, key = 'container')],
		[sg.Button('Nova Tarefa'), sg.Button('Resetar')]
	]

	return sg.Window('Gerenciador de Tarefas', layout = layout, finalize = True)
	
#Criar a Janela
janela = criar_janela()

while True:
	event, values = janela.read()
	if event == sg.WIN_CLOSED:
		break
	elif event == 'Nova Tarefa':
		janela.extend_layout(janela['container'],[[sg.Checkbox(''), sg.Input('')]])
	elif event == 'Resetar':
		janela.close()
		janela = criar_janela()
