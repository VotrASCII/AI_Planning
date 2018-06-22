import os
from multiprocessing import Process
import time

runfile = "./run_search.py"
compiler = ['python']

#time limited subprocess
def run_script(i, program, search):             
    print("Running {} compiler on program {} using search strategy {}...".format(i,program+1,search+1))
    os.system('{} {} -p {} -s {} >> planning_output.txt'.format(i,runfile,program+1,search+1))


def script_driver(max_time):
    for i in compiler:
        for program in range(3):
            for search in range(10):
                script = Process(target=run_script, args=(i,program,search))
                script.start()
                run_time = 0
                sleep_time = 10
                while 1:
                    time.sleep(sleep_time)
                    run_time += sleep_time
                    if not script.is_alive():
                        break

                    if run_time > max_time:
                        script.terminate()
                        print("...")
                        os.system('echo "Air Cargo Problem {} using search strategy {}, run time exceeded {} seconds." >> planning_output.txt'.format(program+1, search+1, max_time))
                        break

def main():
    script_driver(600)  #max runtime 10 minutes.

if __name__ == "__main__":
    main()
