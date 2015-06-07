#!/usr/bin/env python

import os
import sys

f = open('exec_wrong', 'w+')

filename_list ={}

def tracer(frame, event, arg):
    if event == "line":

        code = frame.f_code
        function = code.co_name
        filename = code.co_filename
        line = frame.f_lineno

        if not filename.startswith(call_dir):
            return tracer

        filename = filename[len(call_dir):]
        output_line = filename + ":" + `line`
        #output_line = filename + ":" + `line` + ":" + function + "():" + event + " " + str(arg) + '\n'  

        if filename in filename_list and filename_list[filename][line] == 1:
            return tracer
        
        if filename not in filename_list:
            filename_list[filename] = [0]*5000
            
        filename_list[filename][line] = 1
        f.write(output_line+'\n')
    
    return tracer

call_dir = os.path.abspath(sys.path[0]) #normalize path
if call_dir[-1] != os.sep:
    call_dir = call_dir + os.sep

program_to_analyze = "xpcmd.py"

#sys.path[0] = os.path.abspath(os.path.dirname(program_to_analyze))

import __main__    
sys.settrace(tracer)

execfile(os.path.abspath(program_to_analyze), __main__.__dict__) 
	
