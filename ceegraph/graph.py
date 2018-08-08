import config
from math import floor

def intf(n):
    return int(floor(n))


def plot(self, xs, ys, y=0, x=0, axis="w", bg="-", line="y", point="y", width=config.WIDTH, height=config.HEIGHT,
         xtitle="", ytitle="", xmin=None, xmax=None, ymin=None, ymax=None, drawline=True):
    if xmin is None:
        xmin = min(xs)
    if xmax is None:
        xmax = max(xs)
    if ymin is None:
        ymin = min(ys)
    if ymax is None:
        ymax = max(ys)

    xtick = (xmax-xmin)/(width-3)
    ytick = (ymax-ymin)/(height*2-4)

    def get_canvas_pos(posx, posy):
        canx = 2+intf((posx-xmin)/xtick)
        cany = height*2-3-intf((posy-ymin)/ytick)

        return canx,cany

    canvas = [[bg for j in range(width)] for i in range(2*height)]
    for i in range(1,2*height-2):
        canvas[i][2] = axis
    for i in range(2,width):
        canvas[-3][i] = axis

    ticks = max(width,height*2)
    for x1,x2,y1,y2 in zip(xs[:-1],xs[1:],ys[:-1],ys[1:]):
        for i in range(ticks+1):
            px = x1+(x2-x1)*i/ticks
            py = y1+(y2-y1)*i/ticks
            canx,cany = get_canvas_pos(px,py)
            canvas[cany][canx] = line

    for px, py in zip(xs,ys):
        canx,cany = get_canvas_pos(px,py)
        canvas[cany][canx] = point

    self.print_image("\n".join("".join(i for i in j) for j in canvas),y,x)

    for xlabel in range(xmin,xmax,intf((xmax-xmin)/4)):
        canx,_ = get_canvas_pos(xlabel,0)
        self.move_cursor(x=x+canx,y=y+height-1)
        self.add_text(str(xlabel))

    for ylabel in range(ymin,ymax,intf((ymax-ymin)/4)):
        _,cany = get_canvas_pos(0,ylabel)
        cany //= 2
        self.move_cursor(x=0,y=y+cany)
        self.add_text(str(ylabel))

    self.move_cursor(y=y,x=0)
    self.add_text(ytitle,fg=axis)
    self.move_cursor(y=y+height-1,x=width-len(xtitle))
    self.add_text(xtitle,fg=axis)
