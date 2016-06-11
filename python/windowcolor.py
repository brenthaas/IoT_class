#!/usr/bin/python
import signal
from gi.repository import Gtk,Gdk, GdkPixbuf,GLib
from array import array

class Point():
    def __init__(self, x, y):
        self.x = (int)(x)
        self.y = (int)(y)

class LedStrip():
    strips = []

    def add_strip(self, start, end, count):
        width = end.x - start.x
        height = end.y - start.y

        deltaX = float(width) / count
        deltaY = float(height) / count

        for i in range(0, count):
            self.strips.append(Point(start.x + i*deltaX, start.y + i*deltaY))

class picker(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect('delete-event', Gtk.main_quit)
        GLib.timeout_add(1000 / 30, self.motion_cb)
        self.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0,0,0,0))
        #self.set_default_size(800,480*2)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #self.zoomwin=Gtk.Image()
        #self.zoomwin.set_default_size(800,480)
        #box.add(self.zoomwin)

        da=Gtk.DrawingArea()
        da.set_size_request (800, 480)
        da.connect('draw', self.draw_leds)
        box.add(da)

        self.add(box)
        self.show_all()

        #self.window=Gdk.get_default_root_window()
        self.display=Gdk.Display.get_default()
        self.screen = Gdk.Display.get_default().get_default_screen()

        self.strip = LedStrip()

        x = 800 / 2
        y = 480 / 2

        scale = y / 7.8;
        pos_0 = Point(x      , y      );

        pos_1 = Point(x + scale *  3.917, y + scale *  1.272);
        pos_2 = Point(x + scale *  0    , y + scale *  4.118);
        pos_3 = Point(x + scale * -3.917, y + scale *  1.272);
        pos_4 = Point(x + scale * -2.421, y + scale * -3.332);
        pos_5 = Point(x + scale *  2.421, y + scale * -3.332);

        pos_6 = Point(x + scale *  4.423, y + scale *  6.088);
        pos_7 = Point(x + scale * -4.423, y + scale *  6.088);
        pos_8 = Point(x + scale * -7.157, y + scale * -2.325);
        pos_9 = Point(x + scale *  0    , y + scale * -7.526);
        pos_A = Point(x + scale *  7.157, y + scale * -2.325);

        self.strip.add_strip(pos_1, pos_0, 70);
        self.strip.add_strip(pos_1, pos_2, 82);
        self.strip.add_strip(pos_1, pos_A, 84);
        self.strip.add_strip(pos_1, pos_6, 84);

        self.strip.add_strip(pos_2, pos_0, 70);
        self.strip.add_strip(pos_2, pos_3, 82);
        self.strip.add_strip(pos_2, pos_7, 84);
        self.strip.add_strip(pos_2, pos_6, 84);


        self.strip.add_strip(pos_3, pos_0, 70);
        self.strip.add_strip(pos_3, pos_4, 82);
        self.strip.add_strip(pos_3, pos_8, 84);
        self.strip.add_strip(pos_3, pos_7, 84);

        self.strip.add_strip(pos_4, pos_0, 70);
        self.strip.add_strip(pos_4, pos_5, 82);
        self.strip.add_strip(pos_4, pos_9, 84);
        self.strip.add_strip(pos_4, pos_8, 84);

        self.strip.add_strip(pos_5, pos_0, 70);
        self.strip.add_strip(pos_5, pos_1, 82);
        self.strip.add_strip(pos_5, pos_9, 84);
        self.strip.add_strip(pos_5, pos_A, 84);

        self.w,self.h=800,480 #self.screen.get_width()/8,self.screen.get_height()/8#120,120

    def get_pixbuf(self):
        #Get a pixbuff image under pointer
        (screen,self.x,self.y,modifier)=self.display.get_pointer()
        return Gdk.pixbuf_get_from_window(Gdk.get_default_root_window(), self.x-int(self.w/2), self.y-int(self.h/2), int(self.w), int(self.h))

    def motion_cb(self):
        self.pixbuf=self.get_pixbuf()#.scale_simple(self.w / 8,self.h / 8,GdkPixbuf.InterpType.TILES)
        #self.zoomwin.set_from_pixbuf(self.pixbuf)
        self.queue_draw()
        return True

    def draw_leds(self, widget, cr):
        #print("%s" % self.pixbuf.get_pixels())
        pixels = array("B", self.pixbuf.get_pixels())
        rowstride = self.pixbuf.get_rowstride()
        channels  = self.pixbuf.get_n_channels()
        pixel_width = 2
        
        for led in self.strip.strips:
            r = pixels[led.y * rowstride + led.x * channels + 0];
            g = pixels[led.y * rowstride + led.x * channels + 1];
            b = pixels[led.y * rowstride + led.x * channels + 2];
            #print("r: %d, g: %d, b: %d" % (r/256.0, g/256.0, b/256.0))
            cr.set_source_rgb(r/256.0,g/256.0, b/256.0)
            cr.rectangle(led.x-pixel_width/2, led.y-pixel_width/2, pixel_width, pixel_width)
            cr.fill()
        return False

if __name__=="__main__":
    win=picker()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()
