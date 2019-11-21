# -*- coding: utf-8 -*-

import pyqrcode
import os

def Data_to_QR(url, index, px=250):
    if (url == ' '):
        return url
    QR_VER = 3
    QR_WIDTH = [21.0, 25.0, 29.0, 33.0, 37.0, 41.0]
    QR_ERROR = 'M'

    scale = float(px) / QR_WIDTH[QR_VER - 1]
    qr_name = 'qr_'+ str(index) + '.svg'
    qr_create = pyqrcode.create(url, error=QR_ERROR, version=QR_VER, mode='binary')
    
    cur_dir = os.getcwd()
    os.chdir('html/resources/qr')
    qr_create.svg(qr_name, scale=scale, quiet_zone=0, background='white')
    os.chdir(cur_dir)
    
    return 'resources/qr/' + qr_name