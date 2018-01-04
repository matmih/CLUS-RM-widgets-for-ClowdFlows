from django.shortcuts import render
import os
import random

def cfrm_display_rrfile(request,input_dict,output_dict,widget):
    from mothra.settings import MEDIA_ROOT
    from workflows.helpers import ensure_dir
      
    output_content_all = input_dict['redescriptions']
    files = []
    count=1
    for output_content in output_content_all: 
           
          if output_content is None:
             output_content = 'Results missing :('
          filename = os.path.join(str(request.user.id),'redescriptions_{w_id}_{itCount}.rr'.format(w_id = widget.id,itCount=count))
          count=count+1
          files.append(filename)
          destination_rr = os.path.join(MEDIA_ROOT, filename)
          ensure_dir(destination_rr)
          with open(destination_rr, 'w') as f:
               f.write(output_content)
     
    #print 'filenames'
    #print files

    return render(request, 'visualizations/cfrm_display_rrfile.html',
              {'files': files, 
               #'content': "<br />".join(output_content.split("\n")),
               'contents': output_content_all,
               'random': int(random.random() * 10000000),
               'widget': widget,
               'input_dict': input_dict})

