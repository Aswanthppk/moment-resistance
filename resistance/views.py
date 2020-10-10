from django.shortcuts import render
from .forms import form1
from django.http import HttpRequest


# Create your views here.

def function1(request):
	form=form1(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			
			print(form)
			
			ast=form.cleaned_data.get("AreaOfthesteel")
			fy=form.cleaned_data.get ('Charectresticstrengthofsteel')
			fck=form.cleaned_data.get('Charectresticstrengthofconcrete')
			b=form.cleaned_data.get('WidthoftheBeam')
			d=form.cleaned_data.get('EffectiveDepthoftheBeam')
			
			if fy==415:
		
				Namax=.48
			elif fy==500:
				Namax=.46
	
			else:
				Namax=.53
			
			
			
			Na=(.87*ast*fy)/(.36*fck*b*d)
			
			
			ans=float("%0.4f"%Na)
			
			
			if ans > Namax :
				
				mulimit= (.36*fck*Namax)*(1-(.416*Namax))*(b*d*d)
		
				
				Ast=(.36*fck*b*d)*(Namax)/(.87*fy)
				
				if Ast > 1000:
					print('Take 18 mm steel')
				else:
					print('Take 16mm steel')
				context={'mulimit':mulimit,'Namax':Namax,'ans':ans,'Ast':Ast}
				return render(request, 'result.html',context)
			elif ans == Namax:
				print('balanced section')
			else :
				
				mu=(.87*fy*ast*d)*(1-((fy*ast)/(fck*b*d)))
				
				
				context={'Namax':Namax,'ans':ans,'mu':mu}
				return render(request,'result.html',context)
	return render(request,'index.html',{'form':form})

	  
			

 