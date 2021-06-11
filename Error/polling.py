import time
import sys
import threading

#global var polled for change
keep_running_polled = True

class SigFinish(Exception):
    pass

def throw_signal_function(frame, event, arg):
    raise SigFinish()

def do_nothing_trace_function(frame, event, arg):
    # Note: each function called will actually call this function
    # so, take care, your program will run slower because of that.
    return None

def interrupt_thread(thread):
    for thread_id, frame in sys._current_frames().items():
        if thread_id == thread.ident:  # Python 2.6 or later
            set_trace_for_frame_and_parents(frame, throw_signal_function)

def set_trace_for_frame_and_parents(frame, trace_func):
    # Note: this only really works if there's a tracing function set in this
    # thread (i.e.: sys.settrace or threading.settrace must have set the
    # function before)
    while frame:
        if frame.f_trace is None:
            frame.f_trace = trace_func
        frame = frame.f_back
    del frame


class MyThread_polled(threading.Thread):

    def run(self):
        # Note: this is important: we have to set the tracing function
        # when the thread is started (we could set threading.settrace
        # before starting this thread to do this externally)
        sys.settrace(do_nothing_trace_function)
        global keep_running_polled
        try:
            while keep_running_polled: #each loop it examines the state of this var
                sys.stderr.write("*whistling* Doing nothing but waiting for global var to change...\n");
                time.sleep(3)
        except SigFinish:
            sys.stderr.write('Caught interrupt signal! Finishing thread cleanly.\n')
       
        print("Global Var Changed")


thread = MyThread_polled()
thread.start()
time.sleep(.5)  # Wait a bit just to see it looping.

while True:
    ans = raw_input('Change Global Variable To Break? ');
    if not ans:
        continue
    if ans not in ['y', 'Y', 'n', 'N', 'i']:
        print 'please enter y or n.'
        continue
    if ans == 'y' or ans == 'Y':
        keep_running_polled = False
        start = time.time()
        break
    if ans == 'n' or ans == 'N':
        continue


thread.join()  # Joining here: if we didn't end the thread before,
               # we'd be here forever.
end  = time.time()
sys.stderr.write('Finished '+str(end-start)+" second delay before it ended")