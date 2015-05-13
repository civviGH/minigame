import Tkinter as Tk
import math

root = Tk.Tk()
root.resizable(0,0)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.configure(width = screen_width, height = screen_height)
root.config(cursor="none")
root.state("zoomed")
Canvas = Tk.Canvas(root, bg = "#00ffff", width = screen_width, height = screen_height)
Canvas.pack()
LineSegments = []
scale = 50
segment_length = 20
tmp_color = [255,0,0]
compl_color = [0,255,255]

for i in range(1,screen_width/scale):
	for j in range(1,screen_height/scale):
		tmp = [i*scale,j*scale]
		LineSegments.append(tmp)
del LineSegments[len(LineSegments)/2]

def draw_circle(canvas,x,y,r, color):
	canvas.create_oval(x-r,y-r,x+r,y+r, fill=color)
	return 0
	
def draw_line_to_center(Canvas, point, color):
	vektor = [0,0]
	center = [screen_width/2,screen_height/2]
	vektor[0] = center[0]-point[0]
	vektor[1] = center[1]-point[1]
	Canvas.create_line(point[0],point[1],center[0], center[1], fill = color)

def draw_line_to_point(Canvas, inputPoint, targetPoint, color):
	vektor = [0,0]
	vektor[0] = targetPoint[0]-inputPoint[0]
	vektor[1] = targetPoint[1]-inputPoint[1]
	vektor_length = math.sqrt(vektor[0]*vektor[0]+vektor[1]*vektor[1])
	if vektor_length != 0:
		vektor[0] = (vektor[0]/vektor_length)*segment_length
		vektor[1] = (vektor[1]/vektor_length)*segment_length
		Canvas.create_line(inputPoint[0],inputPoint[1],inputPoint[0]+vektor[0], inputPoint[1]+vektor[1], fill = color, width = 2)

def redraw(event):
	if tmp_color[0] == 255 and tmp_color[1] < 255 and tmp_color[2] == 0:
		tmp_color[1] += 1
	elif tmp_color[0] > 0 and tmp_color[1] == 255 and tmp_color[2] == 0:
		tmp_color[0] -= 1
	elif tmp_color[0] == 0 and tmp_color[1] == 255 and tmp_color[2] < 255:
		tmp_color[2] += 1
	elif tmp_color[0] == 0 and tmp_color[1] > 0 and tmp_color[2] == 255:
		tmp_color[1] -= 1
	elif tmp_color[0] < 255 and tmp_color[1] == 0 and tmp_color[2] == 255:
		tmp_color[0] += 1
	elif tmp_color[0] == 255 and tmp_color[1] == 0 and tmp_color[2] > 0:
		tmp_color[2] -= 1
	for i in range(0,3):
		compl_color[i] = 255 - tmp_color[i]
	color = "#%02x%02x%02x" % (compl_color[0], compl_color[1], compl_color[2])
	Canvas.configure(bg = color)
	color = "#%02x%02x%02x" % (tmp_color[0], tmp_color[1], tmp_color[2])
	Canvas.delete("all")
	for el in LineSegments:
		draw_line_to_point(Canvas, el, [event.x, event.y], color)
	draw_circle(Canvas, event.x, event.y, 5, "yellow")
	
def initialDraw():
	Canvas.delete("all")
	for el in LineSegments:
		draw_line_to_point(Canvas, el, [screen_width/2, screen_height/2], "#ff0000")
	
def debug(event):
	print "click"
	
Canvas.bind("<Motion>", redraw)
Canvas.bind("<Button-1>", debug)
initialDraw()

print LineSegments

def printsth():
	print "HELLO"

root.mainloop()