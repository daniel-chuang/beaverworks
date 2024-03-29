#!/usr/bin/env python

import time
import sys
import threading
import timeit

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


class MyThread(threading.Thread):

    def run(self):
        # Note: this is important: we have to set the tracing function
        # when the thread is started (we could set threading.settrace
        # before starting this thread to do this externally)
        sys.settrace(do_nothing_trace_function)
        try:
            while True:
                sys.stderr.write("*whistling* Doing nothing but waiting for interrupt...\n");
                time.sleep(3)
        except SigFinish:
            sys.stderr.write('Caught interrupt signal! Finishing thread cleanly.\n')


thread = MyThread()
thread.start()
time.sleep(.5)  # Wait a bit just to see it looping.

start = 0

while True:
    ans = raw_input('Interrupt thread? ');
    if not ans:
        continue
    if ans not in ['y', 'Y', 'n', 'N']:
        print 'please enter y or n.'
        continue
    if ans == 'y' or ans == 'Y':
        start = timeit.timeit()
        break
    if ans == 'n' or ans == 'N':
        continue

interrupt_thread(thread)
sys.stderr.write('Joining\n')
thread.join()  # Joining here: if we didn't interrupt the thread before, 
               # we'd be here forever.
end  = timeit.timeit()
sys.stderr.write('Finished '+str(end-start)+" second delay before it ended")