#global flag
#flag=0
global score1
score1=0
global score2
score2=0
global p1gw
p1=0
global p2gw
p2=0
global p1gw
global p2gw
p1gw=0
p2gw=0
global p2sw
global p2sw
p1sw=0
p2sw=0
class tennis:
	def __init__(self,score1,score2,strng,p1gw,p2gw,p1sw,p2sw):
		self.score1=score1
		self.score2=score2
		self.strng=strng
		self.p1gw=p1gw
		self.p2gw=p2gw
		self.p1sw=p1sw
		self.p2sw=p2sw
	def p1s(self,score1,score2,p1gw):
		if self.score1==0 or self.score1==15:
			self.score1+=15
		elif self.score1==30:
			self.score1+=10
		elif self.score1==40 and self.score2!=40:
			flag=0
			self.p1gw+=1
			if self.p1gw==7:
				self.p1sw=1
			if self.score1==40 or a1==1:# or self.strng=="Fault":
				flag=0
				a1=0
				return 0
		return self.score1
	def p2s(self,score1,score2,p2gw):
		if self.score2==0 or self.score2==15:
			self.score2+=15
		elif self.score2==30:
			self.score2+=10
		elif self.score2==40 and self.score1!=40:
			flag=1
			self.p2gw+=1
			if self.p2gw==7:
				self.p2sw=1
			if self.score2==40 or a2==1:# or self.strng=="Fault":
				flag=0
				a2=0
				return 0
		return self.score2
	def out1(self):
		print "Player1 : ",self.strng
		print "P1 Score : ",self.score1
		print "P2 Score : ",self.score2
		print "P1 Game Win Count : ",self.p1gw
		print "P2 Game Win Count : ",self.p2gw
		print "P1 Set Win Count : ",self.p1sw
		print "P2 Set Win Count : ",self.p2sw
		print
	def out2(self):
		print "Player2 : ",self.strng
		print "P1 Score : ",self.score1
		print "P2 Score : ",self.score2
		print "P1 Game Win Count : ",self.p1gw
		print "P2 Game Win Count : ",self.p2gw
		print "P1 Set Win Count : ",self.p1sw
		print "P2 Set Win Count : ",self.p2sw
		print
	def dyuus(self,n,s1,s2):
		print "Player",((n%2)+1)," : ",self.strng
		print "P1 Score : ",s1
		print "P2 Score : ",s2
		print "P1 Game Win Count : ",self.p1gw
		print "P2 Game Win Count : ",self.p2gw
		print "P1 Set Win Count : ",self.p1sw
		print "P2 Set Win Count : ",self.p2sw
		print
b=3
n=0
flag=0
a1=0
a2=0
import sys
file= sys.argv[1]
f=open(file,'r')
for line in f:
	words=line.split(' ')
	b=words[1].rstrip('\n')
	c=0
	d=0
	f=0
	e=0
	g=tennis(score1,score2,b,p1gw,p2gw,p1sw,p2sw)
	if b=="Serve":
		if (p1gw+p2gw)%2==0:
			if flag==0:
				g.out1()
			elif a2==1:
				g.dyuus(n,"","Advantage")
			elif flag==1 and a2==0:
				g.dyuus(n,"Duece","Duece")
			if a1==1 and a2!=0:
				g.dyuus(n,"Advantage","")
			elif flag==1 and a1==0:
				g.dyuus(n,"Duece","Duece")
				
		else:
			if flag==0:
				g.out2()
			elif a2==1:
				g.dyuus(n,"","Advantage")
			elif flag==1 and a2==0:
				g.dyuus(n,"Duece","Duece")
			if a1==1 and a2!=0:
				g.dyuus(n,"Advantage","")
			elif flag==1 and a1==0:
				g.dyuus(n,"Duece","Duece")
			
		n=0
	if b=="Backhand" or b=="Forehand":
		if (n+p1gw+p2gw)%2==1:
			g.out2()
		else:
			g.out1()
	if b=="Fault":
		if (p1gw+p2gw)%2==0:
			score2=g.p2s(score1,score2,p2gw)
			if a2==1:
				g.dyuus(n,"","Advanced")
				flag=1
			if (score1==40 and score2==40) or a1==1:
				flag=1
				g.dyuus(n,"Duece","Duece")
				if a1==1:
					a2=0
					a1=0
				else:
					a2=1
					a1=0
			elif score2==0:# and score1!=0:
				p2gw+=1
			if flag==0:
				g.out1()
		else:
			score1=g.p1s(score1,score2,p1gw)
			if a1==1:
				g.dyuus(n,"Advantage","")
				flag=1
			if (score1==40 and score2==40) or a2==1:
				flag=1
				g.dyuus(n,"Duece","Duece")
				if a2==1:
					a2=0
					a1=0
				else:
					a2=0
					a1=1
			elif score1==0:# and score2!=0:
				p1gw+=1
			if flag==0:
				g.out2()
	if b=="PointLost-Out" or b=="PointLost-CouldNotReach" or b=="PointLost-SameSide":
		if (n+p1gw+p2gw)%2==1:
			score1=g.p1s(score1,score2,p1gw)
			if a1==1:
				g.dyuus(n,"Advantage","")
				flag=1
			elif (score1==40 and score2==40) or a2==1:
				flag=1
				g.dyuus(n,"Duece","Duece")
				if a2==1:
					a2=0
					a1=0
				else:
					a2=0
					a1=1
			elif score1==0: #and score2!=40:
				p1gw+=1
			if flag==0:
				g.out2()
		else:
			score2=g.p2s(score1,score2,p2gw)
			if a2==1:
				g.dyuus(n,"","Advantage")
				flag=1
			elif (score1==40 and score2==40) or a1==1:
				flag=1
				g.dyuus(n,"Duece","Duece")
				if a1==1:
					a2=0
					a1=0
				else:
					a2=1
					a1=0
			elif score2==0:# and score1!=40:
				p2gw+=1
			if flag==0:
				g.out1()
	n+=1
