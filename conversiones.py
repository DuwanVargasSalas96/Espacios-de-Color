# -*- coding: UTF-8 -*-

# Conversión YIQ a rva
def YIQ_a_rva(y, i, q):
    # Operar
    r = y + 0.955 * i + 0.618 * q
    v = y - 0.271 * i - 0.645 * q
    a = y - 1.11 * i + 1.7 * q

    # Retorno
    return r, v, a


# Conversión rva a YIQ
def rva_a_YIQ(r, v, a):
    # Operar
    y = 0.299 * r + 0.587 * v + 0.114 * a
    i = 0.596 * r - 0.275 * v - 0.321 * a
    q = 0.212 * r - 0.528 * v + 0.311 * a

    # Retorno
    return y, i, q


# Conversión rva a YCbCr
def rva_a_YCbCr(r, v, a):
    # Operar
    y = 0.299 * r + 0.587 * v + 0.114 * a
    cb = 0.1687 * r - 0.3313 * v - 0.5 * a
    cr = 0.5 * r - 0.418 * v + 0.0813 * a

    # Retorno
    return y, cb, cr


# Conversión YCbCr a rva
def YCbCr_a_rva(y, cb, cr):
    # Operar
    r = y + 1.402 * cr
    v = y + 0.344 * cb - 0.714 * cr
    a = y + 1.772 * cb

    # Retorno
    return r, v, a