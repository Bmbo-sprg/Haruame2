init python:
    class Sin(object):
        def __init__(self, freq, amp, duration=0):
            if not isinstance(freq, tuple):
                freq = (freq, freq)
            self.x_freq, self.y_freq = freq
            if not isinstance(amp, tuple):
                amp = (amp, amp)
            self.x_amp, self.y_amp = amp
            self.duration = duration

        def __call__(self, tran, st, at):
            from math import sin, pi
            if self.duration and st >= self.duration:
                return
            tran.xoffset = self.x_amp*sin(2*pi*self.x_freq*st)
            tran.yoffset = self.y_amp*sin(2*pi*self.y_freq*st)
            return 1./60
 
    class Wiggle(object):
        def __init__(self, freq, amp, duration=0, octaves=1, ampMulti=.5, time=0):
            from random import random
            #予めランダムな値を生成しておく
            self.randoms = [(1+random(), 1+random()) for i in range(0, 100)]
            if not isinstance(freq, tuple):
                freq = (freq, freq)
            self.x_freq, self.y_freq = freq
            if not isinstance(amp, tuple):
                amp = (amp, amp)
            self.x_amp, self.y_amp = amp
            self.octaves = octaves
            self.ampMulti = ampMulti
            self.duration = duration
            self.time = time

        def __call__(self, tran, st, at):
            if self.duration and st >= self.duration:
                return
            from math import sin, pi, ceil
            rx1, rx2 = self.randoms[int(ceil(st*self.x_freq)%100)]
            ry1, ry2 = self.randoms[int(ceil(st*self.y_freq)%100)]
            tran.xoffset = rx1*self.x_amp*sin(2*pi*self.x_freq*st) + rx2*self.x_amp*self.ampMulti*sin(2*pi*self.x_freq*2*self.octaves*(st+self.time))
            tran.yoffset = ry1*self.y_amp*sin(2*pi*self.y_freq*st) + ry2*self.y_amp*self.ampMulti*sin(2*pi*self.y_freq*2*self.octaves*(st+self.time))
            return 1./60