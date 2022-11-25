from datetime import datetime
import os

DAYS_IN_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31)

def is_leap_year(y) -> bool:
    return abs(y - 2020) % 4 == 0


def del_str_zero(str) -> str:
    if str:
        if str[0] == '0':
            return str[1]
        else:
            return str
    else:
        return str

class DecodeDMYHM:
    d: int
    m: int
    y: int
    h: int
    mi: int

    def __init__(self):
        self.d = 0
        self.m = 0
        self.y = 0
        self.h = 0
        self.mi = 0

    def __str__(self):
        return str(self.d) + '.' + str(self.m) + '.' + str(self.y) + ' ' + str(self.h)  + ':' + str(self.mi)


def calc_orig_price(price, discount: int = 0) -> float:
    if price:
        if not discount:
            discount = 0
        orig_price = round(price / (1 - discount / 100), 2)
        return orig_price
    else:
        return 0

class Dt_HM:
    h: int
    m: int

    def __init__(self):
        self.h = 0
        self.m = 0

    def __str__(self):
        return str(self.h)  + ':' + str(self.m)

def decode_dt(dt) -> DecodeDMYHM:
    s: str = '{0:%d}_{0:%m}_{0:%Y}_{0:%H}_{0:%M}'.format(dt)
    #print(s)
    sep = s.split("_")
    #print(str(sep))
    res = DecodeDMYHM()
    res.d = int(del_str_zero(sep[0]))
    res.m = int(del_str_zero(sep[1]))
    res.y = int(del_str_zero(sep[2]))
    res.h = int(del_str_zero(sep[3]))
    res.mi = int(del_str_zero(sep[4]))
    return res

def date_to_str_dmy(dt) -> str:
    s: str = '{0:%d}_{0:%m}_{0:%Y}_{0:%H}_{0:%M}'.format(dt)
    sep = s.split("_")
    return sep[0] + "." + sep[1] + "." + sep[2]

def calc_diff_dt_in_HM(beg_dt, end_dt) -> Dt_HM:
    bt = decode_dt(beg_dt)
    et = decode_dt(end_dt)
    if is_leap_year(et.y):
        d_count = 366
    else:
        d_count = 365
    d_dif = et.d - bt.d
    m_dif = et.m - bt.m
    y_dif = et.y - bt.y
    h_dif = et.h - bt.h
    mi_dif = et.mi - bt.mi

    if d_dif < 0:
        m_dif = m_dif - 1
        d_dif = DAYS_IN_MONTHS[et.m-1] + d_dif

    if m_dif < 0:
        y_dif = y_dif - 1
        m_dif = 12 + m_dif

    if et.m > 2 and is_leap_year(et.y):
        d_dif = d_dif + 1

    if h_dif < 0:
        d_dif = d_dif - 1
        h_dif = 24 + h_dif

    if mi_dif < 0:
        h_dif = h_dif -1
        mi_dif = 60 + mi_dif

    if m_dif == 0:
        d_count = DAYS_IN_MONTHS[bt.m-1] - bt.d + et.d

    print("d_count=", str(d_count))

    print("y_dif=", str(y_dif), "m_dif=", str(m_dif), "d_dif=", str(d_dif), "h_dif=", str(h_dif), "mi_dif=", str(mi_dif))
    res = Dt_HM()
    res.h = d_dif*24 + h_dif
    res.m = mi_dif
    print("res h=", str(res.h), "m=", str(res.m))
    return res

