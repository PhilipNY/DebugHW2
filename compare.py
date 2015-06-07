#!/usr/bin/python

import sys
import math

filename_list ={}

f_w = open('exec_wrong', 'r')
f_r = open('exec_lines', 'r')
f_output = open('out', 'w')
    
NS = 1
NF = 1

for line in f_w:
    split_line = line.split(':')
    line_num = int(split_line[1])
    filename = split_line[0]
    if filename not in filename_list:
        filename_list[filename] = "exist"
        filename_list[filename+"_NCF"] = [0]*5000
        filename_list[filename+"_NUF"] = [0]*5000
        filename_list[filename+"_NCS"] = [0]*5000
        filename_list[filename+"_NUS"] = [0]*5000
        filename_list[filename+"_NC"] = [0]*5000
        #filename_list[filename+"_NU"] = [0]*5000

    filename_list[filename+"_NCF"][line_num] += 1
    filename_list[filename+"_NC"][line_num] += 1

for line in f_r:
    split_line = line.split(':')
    line_num = int(split_line[1])
    filename = split_line[0]
    if filename not in filename_list:
        filename_list[filename] = "exist"
        filename_list[filename+"_NCF"] = [0]*5000
        filename_list[filename+"_NUF"] = [0]*5000
        filename_list[filename+"_NCS"] = [0]*5000
        filename_list[filename+"_NUS"] = [0]*5000
        filename_list[filename+"_NC"] = [0]*5000
        #filename_list[filename+"_NU"] = [0]*5000

    filename_list[filename+"_NCS"][line_num] += 1
    filename_list[filename+"_NC"][line_num] += 1


for i in range(0, 4999, 1):
    if filename_list[filename+"_NCF"][i] == 0:
        filename_list[filename+"_NUF"][i] += 1

#print filename_list

output_line = "filename "+" Tarantula "+" Ochiai "+" Ochiai_2 "+" DStar "+" brightness "+" hue "+'\n'
f_output.write(output_line)

for key in filename_list:
    if filename_list[key] == "exist":
        for i in range(0, 4999, 1):
            NCF = (float)(filename_list[key+"_NCF"][i])
            NUF = (float)(filename_list[key+"_NUF"][i])
            NCS = (float)(filename_list[key+"_NCS"][i])
            NUS = (float)(filename_list[key+"_NUS"][i])
            NC = (float)(filename_list[key+"_NC"][i])

            if NCF/NF + NCS/NS != 0:
                susp_Tarantula = (NCF/NF)/(NCF/NF + NCS/NS)
            else:
                susp_Tarantula = "Zero"

            if math.sqrt(NF*(NCF + NCS)) != 0:
                susp_Ochiai = NCF/math.sqrt(NF*(NCF + NCS))
            else:
                susp_Ochiai = "Zero"

            susp_Ochiai_2 = (NCF - NCS/(NS + 1))

            if NUF + NCS != 0:      
                susp_DStar = math.pow(NCF, 1)/(NUF + NCS)
            else:
                susp_DStar = "Zero"

            brightness = (NCS+NCF)/(NC+NF)
            
            if NCS + NCF != 0:
                hue = NCS/(NCS+NCF)*0.33
            else:
                hue = "Zero"

            output_line = key+":"+`i`+" "+`susp_Tarantula`+" "+`susp_Ochiai`+" "+`susp_Ochiai_2`+" "+`susp_DStar`+" "+`brightness`+" "+`hue`+'\n'
            #print output_line
            f_output.write(output_line)

        
    

