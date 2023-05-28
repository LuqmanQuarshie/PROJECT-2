import PySimpleGUI as pg
import qrcode
import os


layout = [
    [pg.Text('Enter text:'), pg.InputText(key='text')],
    [pg.Text('Select QR code size:'), pg.Slider(range=(1, 20), orientation='h', default_value=5, key='size')],
    [pg.Text('Select QR code color:')],
    [pg.Radio('Black', "COLOR", default=True, key='color_black'), pg.Radio('Red', "COLOR", key='color_red')],
    [pg.Text('Select background color:')],
    [pg.Radio('White', "BG_COLOR", default=True, key='bg_color_white'), pg.Radio('Blue', "BG_COLOR", key='bg_color_blue')],
    [pg.Button('Generate QR Code')],
    [pg.Image(key='image')]
]


window = pg.Window('QR Code Generator', layout)


while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break

    if event == 'Generate QR Code':
      
        qr = qrcode.QRCode(version=1, box_size=values['size'], border=4)
        qr.add_data(values['text'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='black' if values['color_black'] else 'red',
                            back_color='white' if values['bg_color_white'] else 'blue')

       
        img_file = 'qrcode.png'
        path = os.path.join(os.getcwd(), img_file)
        img.save(path)

       
        window['image'].update(filename=path)


window.close() 



