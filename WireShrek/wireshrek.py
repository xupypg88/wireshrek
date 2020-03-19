import sublime
import sublime_plugin
import sys
import os
#from LogLib import *
#Job.Backup_Job_For_restore.Backup.log Job.CPM_Backup__SUK__-_Daily.Backup.log



# 
buff=''

#close naher window
class ClosenahuiCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.active_view().set_scratch(True)
		self.window.active_view().close()



class NewwinCommand(sublime_plugin.WindowCommand):
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

class PutnewwinCommand(sublime_plugin.WindowCommand):
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