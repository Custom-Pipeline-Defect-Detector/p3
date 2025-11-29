# *_*coding:utf-8 *_*
# @Author : zyc
import jpype                                                                                               # type: ignore
import os

def startjvm():
    jvmPath = r'jdk1.8.0_351\jre_1\bin\server\jvm.dll'
    ext_classpath = os.getcwd()
    jar_path = r'./jar/drools_reasoning.jar'
    dependency = os.path.join(os.path.abspath('.'), r'jar/drools_reasoning_jar')
    jpype.startJVM(jvmPath, "-ea", '-Djava.class.path={}\\{}'.format(ext_classpath, jar_path),
                   "-Djava.ext.dirs=%s" % dependency,"-Dfile.encoding=UTF-8")
def jpype_run_drools(filepath,save_dir):
    jClass = jpype.JClass("runall")
    jclass = jClass()  
    pipe_str=jclass.excel_pipe_drools(filepath)
    print(pipe_str)
    with open(str(save_dir)+"/drools.txt","w",encoding='UTF-8') as f:
        f.write(str(pipe_str))
    f.close()



