import multiprocessing
from file_read import read_with_timeout
import tkinter

def start():
    proc.start()

def stop():
    proc.terminate()

if __name__ == '__main__':

    proc = multiprocessing.Process(target=read_with_timeout, args=())

    root = tkinter.Tk()
    root.title("Window")
    root.geometry("200x200")

    app = tkinter.Frame(root)
    app.grid()

    start = tkinter.Button(app, text = "Start", command=start)
    stop = tkinter.Button(app, text="Stop", command=stop)
    start.grid()
    stop.grid()
    root.mainloop()
    proc.join()
