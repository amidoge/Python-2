#wavelengths of visible light
wavelength = int(input('What is the wavelength?'))
if wavelength >= 380 and wavelength < 450:
    print('violet')
elif wavelength >= 450 and wavelength < 495:
    print('blue')
elif wavelength >= 495 and wavelength < 570:
    print('green')
elif wavelength >= 570 and wavelength < 590:
    print('yellow')
elif wavelength >= 590 and wavelength < 620:
    print('orange')
elif wavelength >= 620 and wavelength <= 750:
    print('red')
elif wavelength > 750 or wavelength < 380:
    print('Sorry, but there is no such wavelength that matches with a visible light.')