from subprocess import check_output, CalledProcessError
from tempfile import NamedTemporaryFile
import glob,sys,os
import ConfigParser
import json

import subprocess
import StringIO
import re
import uuid
import shutil
import tempfile

def cfrm(input_dict):

    # First we write settings file into temporary files.
    #temporary_settings = NamedTemporaryFile(suffix='.s', delete=False)
    #settings = input_dict['settings']
    #if settings is None:
    #    settings = ''
    #temporary_settings.write(settings)
    #temporary_settings.close()

    ##TEST: simulate settings
    #st = ConfigParser.RawConfigParser()
    #st.optionxform = str
    #st.read('/Users/tlipic/Downloads/RM_main/SettingsEx.set')
    #settings_buffer = StringIO.StringIO()
    #st.write(settings_buffer)
    #settings = settings_buffer.getvalue()    
    #temporary_settings = NamedTemporaryFile(suffix='.s', delete=False)
    #temporary_settings.write(settings)
    #temporary_settings.close()
    #print temporary_settings.name

    ## TEST

    out_dir = tempfile.mkdtemp() #os.path.join(os.path.abspath(os.path.dirname(__file__)), str(uuid.uuid1()))

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        file = open(os.path.join(out_dir, 'distances.csv'), 'w+')
        file.close()
    else:
        print "*******Wrong assumption!"

    #temporary_settings = NamedTemporaryFile(suffix='.s', dir=out_dir, delete=False)
    temporary_settings = open(os.path.join(out_dir, 'Settings.set'), 'w+')
    settings = input_dict['settings']
    if settings is None:
        settings = ''
    temporary_settings.write(settings)
    temporary_settings.close()

    s = ConfigParser.RawConfigParser()
    s.optionxform = str
    s.read(temporary_settings.name)
    s.set("HardSetup", "OutputFolder", out_dir)
    s.set("HardSetup", "OutputFileName", "redescriptionsGuidedExperimentalIterativeTSMJ.rr")
    settings_buffer = StringIO.StringIO()
    s.write(settings_buffer)
    temporary_settings = open(os.path.join(out_dir, 'Settings.set'), 'w+')
    temporary_settings.write(settings_buffer.getvalue())
    temporary_settings.close()

    log_filename = 'rm_run.log'
    log_fp = os.path.join(out_dir, log_filename)

    ## run rediscription
    rm_jar_fp = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'bin', \
        'Redescription_mining_MW_Constrained.jar')

    cmd = "java -jar {rm_jar_fp} {set_fp} 2>&1 | tee {log_fp}"
    cmd = cmd.format(rm_jar_fp=rm_jar_fp, set_fp=temporary_settings.name, log_fp=log_fp)

    print cmd
    print "Starting Redescription_mining_MW_Constrained.jar: "
    #print cmd
    process = subprocess.Popen(cmd, shell=True, cwd=out_dir)
    print process.pid

    if process.returncode != 0 and process.returncode is not None:
        raise Exception("There was an error when running CLUS: " + str(process.stderr.read()) + " (Error code: " + str(
            process.returncode) + ")")

    stdout, stderr = process.communicate()

	#create file paths for all sets created by optimization by extraction
    opt_type = s.get("General", "optimizationType");
    #parameters = s.get("Rules","parameters");
    os.chdir(out_dir)
    outputs_all=[];
    for file in glob.glob("*.rr"):
          print(file)
          out_fp=file
          try:

                with open(out_fp) as f:
                     output_content = f.read()
                     outputs_all.append(output_content)
          except Exception as e:
                 print "UNEXPECTED ERROR"
                 print out_fp
                 print sys.exc_info()[0]
                 raise
    #print "All outputs joined in one!"				 
    #print outputs_all;
    #if opt_type == "extraction":
     #    os.chdir(out_dir)
      #   for file in glob.glob("*.rr"):
       #        print(file)
         #out_name  = s.get("HardSetup", "OutputFileName")
         #out_fp = os.path.join(out_dir, ''.join([out_name, '1.rr']))
         #print out_fp
	#handle_setting("optimizationType", input_dict, "General", settings)
	#else:
    #correct this in jar file
    #out_name  = s.get("HardSetup", "OutputFileName")
    #out_fp = os.path.join(out_dir, ''.join([out_name, '1.rr']))
    #print out_fp

    #output_content = 'Invalid result'

    #try:

     #   with open(out_fp) as f:
     #       output_content = f.read()

   # except Exception as e:
    #    print "UNEXPECTED ERROR"
     #   print out_fp
      #  print sys.exc_info()[0]
       # raise

    # remove all temporary files.
    os.unlink(temporary_settings.name)

    #clean up
    shutil.rmtree(out_dir)

    return {
       # 'output': output_content,
         'output': outputs_all,
        #'settings': input_dict['settings']
        # 'error:': error
    } 

# Generate RM settings

def handle_setting(name, input_dict, section, settings, checkbox=False):
    if not checkbox and input_dict.get(name, None) is not None \
            and input_dict.get(name, "").strip() != "" \
            and input_dict.get(name, "") != "null":
        if not settings.has_section(section):
            settings.add_section(section)
        settings.set(section, name, input_dict[name])
    if checkbox:
        if input_dict.get(name, None) is not None \
                and input_dict.get(name, "").strip() != "" \
                and input_dict.get(name, "") != "null":
            if not settings.has_section(section):
                settings.add_section(section)
            settings.set(section, name, "Yes")
        else:
            if not settings.has_section(section):
                settings.add_section(section)
            settings.set(section, name, "No")

def cfrm_generate_settings(input_dict):
    settings = ConfigParser.RawConfigParser()
    settings.optionxform = str
    settings_buffer = StringIO.StringIO()

    #TODO: put this in 
    settings.add_section("HardSetup")
    settings.set("HardSetup", "System", "linux")
    settings.set("HardSetup", "JavaPath", "java")

    clus_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'bin','lib', 'CLUSNHMC.jar')
    settings.set("HardSetup", "ClusPath", clus_path)

    handle_setting("Input1", input_dict, "Files", settings)
    handle_setting("Input2", input_dict, "Files", settings)
    handle_setting("preferenceFilePath", input_dict, "Files", settings)
    handle_setting("initClusteringFileName", input_dict, "Files", settings)

    handle_setting("numIterations", input_dict, "General", settings)
    handle_setting("numRandomRestarts", input_dict, "General", settings)
    handle_setting("clusteringMemory", input_dict, "General", settings)
    handle_setting("jsType", input_dict, "General", settings)
    handle_setting("optimizationType", input_dict, "General", settings)

    #handle_setting("numTrees", input_dict, "Trees", settings)
    handle_setting("ATreeDepth", input_dict, "Trees", settings)
    handle_setting("NumTarget", input_dict, "Trees", settings)
    handle_setting("W1SideTrees", input_dict, "Trees", settings)
    handle_setting("W2SideTrees", input_dict, "Trees", settings)
    handle_setting("numSupplementTrees", input_dict, "Trees", settings)
    settings.set("Trees", "numTrees" , 1);

    handle_setting("numNewAttr", input_dict, "Rules", settings)
    handle_setting("numRetRed", input_dict, "Rules", settings)
    handle_setting("redesSetSizeType", input_dict, "Rules", settings)
    handle_setting("minimizeRules", input_dict, "Rules", settings, checkbox=True)
    handle_setting("ruleSizeNormalization", input_dict, "Rules", settings)	
    handle_setting("joiningProcedure", input_dict, "Rules", settings, checkbox=True)
    handle_setting("unguidedExpansion", input_dict, "Rules", settings, checkbox=True)
    handle_setting("allowSERed", input_dict, "Rules", settings, checkbox=True)
    handle_setting("MinSupport", input_dict, "Rules", settings)
    handle_setting("MaxSupport", input_dict, "Rules", settings)
    handle_setting("minJS", input_dict, "Rules", settings)
    handle_setting("minAddRedJS", input_dict, "Rules", settings)
    handle_setting("maxPval", input_dict, "Rules", settings)
    handle_setting("parameters", input_dict, "Rules", settings)	
    handle_setting("attributeImportanceW1", input_dict, "Rules", settings)	
    handle_setting("attributeImportanceW2", input_dict, "Rules", settings)	
    handle_setting("importantAttributesW1", input_dict, "Rules", settings)	
    handle_setting("importantAttributesW2", input_dict, "Rules", settings)	

    handle_setting("allowLeftNeg", input_dict, "Rules", settings)
    handle_setting("allowRightNeg", input_dict, "Rules", settings)
    handle_setting("allowLeftDisj", input_dict, "Rules", settings)
    handle_setting("allowRightDisj", input_dict, "Rules", settings)


    #handle_setting("JSImp", input_dict, "Rules", settings)
    #handle_setting("PValImp", input_dict, "Rules", settings)
    #handle_setting("AttDivImp", input_dict, "Rules", settings)
    #handle_setting("ElemDivImp", input_dict, "Rules", settings)
    #handle_setting("RuleSizeImp", input_dict, "Rules", settings)

    settings.write(settings_buffer)

    return {
        'settings': settings_buffer.getvalue()
    }


def cfrm_display_rrfile(input_dict):
    return {}




