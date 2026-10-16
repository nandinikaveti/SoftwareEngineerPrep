def conversions(n):
    km_m = 0
    m_cm = 0
    cm_mm =0
    if n >0:
        km_m = n * 1000
        m_cm = km_m * 100
        cm_mm = m_cm * 10
        return km_m, m_cm, cm_mm

print(conversions(42.195))



def conv_km_m(n):
    return n * 1000

def conv_m_cm(n):
    return n * 100

def cm_mm(n):
    return n * 10


meters = conv_km_m(42.195)
centimeters = conv_m_cm(meters)
millimeters = cm_mm(centimeters)

print(meters, centimeters, millimeters)