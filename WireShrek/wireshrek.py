import sublime
import sublime_plugin
import sys
import os
#from LogLib import *
#Job.Backup_Job_For_restore.Backup.log Job.CPM_Backup__SUK__-_Daily.Backup.log


#close naher window
class ClosenahuiCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.active_view().set_scratch(True)
		self.window.active_view().close()

class TestexecCommand(sublime_plugin.TextCommand):
	def run(self, edit, lines):
		currvw = self.view
		texta=''
		for line in lines:
			texta += line
		self.view.insert(edit, self.view.size(), texta)

class Find2tabCommand(sublime_plugin.WindowCommand):
	def run(self):

		v = self.window.active_view()

		regs=[]
		for pattern in v.sel():
			for ln in v.find_all(v.substr(pattern),sublime.LITERAL):
				if v.full_line(ln) not in regs:
					regs.append(v.full_line(ln))

		regs.sort()

		buffa=[]		
		for ln in regs:
			buffa.append(v.substr(ln))

		
		self.window.new_file()
		viewv = self.window.active_view()
		viewv.run_command('testexec', { "lines" : buffa })
		viewv.set_syntax_file('Packages/WireShrek/wireshrek.tmLanguage')

class Put2tabCommand(sublime_plugin.WindowCommand):
	def run(self):
		v = self.window.active_view()

		for viewitem in self.window.views():
			if viewitem.name() == 'dumper':
				viewv = viewitem

		if 'viewv' not in locals():
			self.window.new_file()
			viewv = self.window.active_view()

			viewv.set_name('dumper')


		lines = [str(v.substr(line)) for line in v.sel() if line is not ""]
		lines.insert(0, str(v.file_name()) + '\n\n')
		lines.append('\n---   ---   ---\n')

		for l in range(0, len(lines)):
			if '\n' not in lines[l]:
				lines[l] += '\n'

		viewv.run_command('testexec', { "lines" : lines })
		viewv.set_syntax_file('Packages/WireShrek/wireshrek.tmLanguage')

class ShowsobrCommand(sublime_plugin.WindowCommand):
	def run(self):
		#only one must be uncommented
		#self.choosing_run()
		self.first_run()

	def choosing_run(self):

		v = self.window.active_view()

		
		for viewitem in self.window.views():
			if viewitem.name() == 'testo':
				viewv = viewitem

		if 'viewv' not in locals():
			self.window.new_file()
			viewv = self.window.active_view()

			viewv.set_name('testo')

		#find the 0 symbols region point - cursor point in chars from the beginning
		pnt = v.sel()[0].begin()
		#find the line number (starts from 0)
		(xpos, ypos ) = v.rowcol(pnt)

		#select the correct log run

		lines = [ str(xpos)] 
		lines.insert(0, 'Test:\n')
		lines.append('\n---   ---   ---\n')
		viewv.run_command('testexec', { "lines" : lines })

	def first_run(self):
		#self.window.active_view().show_popup("<a href='README.md'>It's not implmented yet. =(</a>",on_navigate=self.browserok)
		with open(self.window.active_view().file_name(), 'r') as fh:
			self.fhcontents = fh.readlines()	
		
		dates = self.search_lines(self.fhcontents, 'UTC Time: ')

		for date in dates:
			print(self.fhcontents[date].split('[')[1].split(']')[0])

		return

	def browserok(self,href):
		self.window.open_file(str(href))
		print('starting...')
		return

	def search_lines(self, array, keyword):
		result = []
		for i in range(0, len(array)):
			if keyword in array[i]:
				result.append(i)
		return result