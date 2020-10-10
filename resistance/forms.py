from django import forms


class form1(forms.Form):
    AreaOfthesteel = forms.IntegerField( label='AREA OF THE STEEL',widget=forms.TextInput(attrs={'placeholder' : 'AST'}) )
    Charectresticstrengthofsteel = forms.IntegerField(label='Charectrestic strength of steel',widget=forms.TextInput(attrs={'placeholder' : 'FY'}))
    Charectresticstrengthofconcrete = forms.IntegerField(label='Charectrestic strength of concrete',widget=forms.TextInput(attrs={'placeholder' : 'FCK'}))
    WidthoftheBeam = forms.IntegerField(label='Width of the Beam',widget=forms.TextInput(attrs={'placeholder' : 'B'}))
    EffectiveDepthoftheBeam = forms.IntegerField(label='Effective Depth of the Beam',widget=forms.TextInput(attrs={'placeholder' : 'D'}))

    