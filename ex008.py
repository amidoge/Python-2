GIZMO_WEIGHT = 112
WIDGET_WEIGHT = 75
widgets = input('\nHow many widgets do you want to order? \n')
gizmos = input('\nHow many gizmos do you want to order? \n')
gizmos = int(gizmos)
widgets = int(widgets)
gizmo_grams = gizmos * GIZMO_WEIGHT
widget_grams = widgets * WIDGET_WEIGHT
total = gizmo_grams + widget_grams
print(f'\nFor {widgets} widgets and {gizmos} gizmos, the total weight would be {total} grams.\n')