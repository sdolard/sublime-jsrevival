import os
import thread
import subprocess
import functools
import time
import sublime
import sys

#if os.getenv('PATH') is not None:
  #os.environ['PATH'] = ':'.join([os.getenv('PATH')])
#print "DEBUG_EXEC: " + str(os.getenv('PATH'))
#print "DEBUG_EXEC: " + str(os.environ)
#print "DEBUG_EXEC: " + str(os.name)
#print "DEBUG_EXEC: " + str(sys.platform)

class AsyncProcess(object):
  def __init__(self, cmd, listener):
    self.cmd = cmd
    self.listener = listener
    self.env = None

    if sys.platform == "darwin":
    	self.env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/git/bin:/usr/X11/bin"}
    	
    #print "DEBUG_EXEC: " + str(self.cmd)
    self.proc = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=self.env)

    if self.proc.stdout:
      thread.start_new_thread(self.read_stdout, ())

    if self.proc.stderr:
      thread.start_new_thread(self.read_stderr, ())

    thread.start_new_thread(self.poll, ())

  def poll(self):
    while True:
      if self.proc.poll() != None:
        sublime.set_timeout(functools.partial(self.listener.proc_terminated, self.proc), 0)
        break
      time.sleep(0.1)

  def read_stdout(self):
    while True:
      data = os.read(self.proc.stdout.fileno(), 2**15)
      if data != "":
        sublime.set_timeout(functools.partial(self.listener.append_data, self.proc, data), 0)
      else:
        self.proc.stdout.close()
        self.listener.is_running = False
        break

  def read_stderr(self):
    while True:
      data = os.read(self.proc.stderr.fileno(), 2**15)
      if data != "":
        sublime.set_timeout(functools.partial(self.listener.append_data, self.proc, data), 0)
      else:
        self.proc.stderr.close()
        self.listener.is_running = False
        break
