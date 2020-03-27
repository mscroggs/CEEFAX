from ceefax import config
from math import floor


def intf(n):
    return int(floor(n))


def plot(self, xs, ys, y=0, x=0, axis="w", bg="-", line="y",
         point="W", width=config.WIDTH, height=config.HEIGHT - 3,
         xtitle="", ytitle="", xmin=None, xmax=None, ymin=None,
         ymax=None, xlabels=None, ylabels=None):
    import numpy as np
    if xmin is None:
        xmin = min(xs)
    if xmax is None:
        xmax = max(xs)
    if ymin is None:
        ymin = min(ys)
    if ymax is None:
        ymax = max(ys)

    if xmin == xmax:
        xmax += 1
    if ymin == ymax:
        ymax += 1

    xtick = (xmax - xmin) / (width - 3)
    ytick = (ymax - ymin) / (height * 2 - 4)

    def get_canvas_pos(posx, posy):
        canx = 2 + intf((posx - xmin) / xtick)
        cany = height * 2 - 3 - intf((posy - ymin) / ytick)

        return canx, cany

    canvas = [[bg for j in range(width)] for i in range(2 * height)]
    for i in range(1, 2 * height - 2):
        canvas[i][2] = axis
    for i in range(2, width):
        canvas[-3][i] = axis

    if line is not None:
        ticks = max(width, height * 2)
        for x1, x2, y1, y2 in zip(xs[:-1], xs[1:], ys[:-1], ys[1:]):
            for i in range(ticks + 1):
                px = x1 + (x2 - x1) * i / ticks
                py = y1 + (y2 - y1) * i / ticks
                canx, cany = get_canvas_pos(px, py)
                canvas[cany][canx] = line

    if point is not None:
        for px, py in zip(xs, ys):
            canx, cany = get_canvas_pos(px, py)
            if 0 <= cany < len(canvas):
                if 0 <= canx < len(canvas[cany]):
                    canvas[cany][canx] = point
            if 0 <= cany + 1 < len(canvas):
                if 0 <= canx + 1 < len(canvas[cany + 1]):
                    canvas[cany + 1][canx + 1] = point
                if 0 <= canx - 1 < len(canvas[cany + 1]):
                    canvas[cany + 1][canx - 1] = point
            if 0 <= cany - 1 < len(canvas):
                if 0 <= canx + 1 < len(canvas[cany - 1]):
                    canvas[cany - 1][canx + 1] = point
                if 0 <= canx - 1 < len(canvas[cany - 1]):
                    canvas[cany - 1][canx - 1] = point

    self.print_image("\n".join("".join(i for i in j) for j in canvas), y, x)

    if xlabels is None:
        if xmax - xmin >= 8:
            step = intf((xmax - xmin) / 4)
        else:
            step = (xmax - xmin) / 4
        for xlabel in list(np.arange(xmin, xmax, step)):
            canx, _ = get_canvas_pos(xlabel, 0)
            self.move_cursor(x=x + canx, y=y + height - 1)
            self.add_text(str(xlabel))
    else:
        for xval, label in xlabels:
            canx, _ = get_canvas_pos(xval, 0)
            self.move_cursor(x=x + canx, y=y + height - 1)
            self.add_text(str(label))

    if ylabels is None:
        if ymax - ymin >= 8:
            step = intf((ymax - ymin) / 4)
        else:
            step = (ymax - ymin) / 4
        for ylabel in list(np.arange(ymin, ymax, step)):
            _, cany = get_canvas_pos(0, ylabel)
            cany //= 2
            self.move_cursor(x=0, y=y + cany)
            self.add_text("{:.2f}".format(ylabel))
    else:
        for yval, label in ylabels:
            _, cany = get_canvas_pos(yval, 0)
            cany //= 2
            self.move_cursor(x=0, y=y + cany)
            self.add_text(str(label))

    self.move_cursor(y=y, x=0)
    self.add_text(ytitle, fg=axis)
    self.move_cursor(y=y + height - 1, x=width - len(xtitle))
    self.add_text(xtitle, fg=axis)
