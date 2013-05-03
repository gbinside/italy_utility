#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 
# (c) Roberto Gambuzzi
# Creato:          17/12/2012 10:00:21
# Ultima Modifica: 17/12/2012 10:03:21
# 
# v 0.0.1.0
# 
# file: C:\Dropbox\rgambuzzi(at)webgriffe.com\coding dojo\iso3166\province_italiane.py
# auth: Roberto Gambuzzi <gambuzzi@gmail.com>
# desc: 
# 
# $Id: province_italiane.py 17/12/2012 10:03:21 Roberto $
# --------------

t_province = (
    ('AG' , 'Agrigento'),
    ('AL' , 'Alessandria'),
    ('AN' , 'Ancona'),
    ('AO' , 'Aosta'),
    ('AR' , 'Arezzo'),
    ('AP' , 'Ascoli Piceno'),
    ('AT' , 'Asti'),
    ('AV' , 'Avellino'),
    ('BA' , 'Bari'),
    ('BT' , 'Barletta-Andria-Trani'),
    ('BL' , 'Belluno'),
    ('BN' , 'Benevento'),
    ('BG' , 'Bergamo'),
    ('BI' , 'Biella'),
    ('BO' , 'Bologna'),
    ('BZ' , 'Bolzano'),
    ('BS' , 'Brescia'),
    ('BR' , 'Brindisi'),
    ('CA' , 'Cagliari'),
    ('CL' , 'Caltanissetta'),
    ('CB' , 'Campobasso'),
    ('CI' , 'Carbonia-Iglesias'),
    ('CE' , 'Caserta'),
    ('CT' , 'Catania'),
    ('CZ' , 'Catanzaro'),
    ('CH' , 'Chieti'),
    ('CO' , 'Como'),
    ('CS' , 'Cosenza'),
    ('CR' , 'Cremona'),
    ('KR' , 'Crotone'),
    ('CN' , 'Cuneo'),
    ('EN' , 'Enna'),
    ('FM' , 'Fermo'),
    ('FE' , 'Ferrara'),
    ('FI' , 'Firenze'),
    ('FG' , 'Foggia'),
    ('FC' , 'Forlì-Cesena'),
    ('FR' , 'Frosinone'),
    ('GE' , 'Genova'),
    ('GO' , 'Gorizia'),
    ('GR' , 'Grosseto'),
    ('IM' , 'Imperia'),
    ('IS' , 'Isernia'),
    ('SP' , 'La Spezia'),
    ('AQ' , 'L\'Aquila'),
    ('LT' , 'Latina'),
    ('LE' , 'Lecce'),
    ('LC' , 'Lecco'),
    ('LI' , 'Livorno'),
    ('LO' , 'Lodi'),
    ('LU' , 'Lucca'),
    ('MC' , 'Macerata'),
    ('MN' , 'Mantova'),
    ('MS' , 'Massa-Carrara'),
    ('MT' , 'Matera'),
    ('ME' , 'Messina'),
    ('MI' , 'Milano'),
    ('MO' , 'Modena'),
    ('MB' , 'Monza e della Brianza'),
    ('NA' , 'Napoli'),
    ('NO' , 'Novara'),
    ('NU' , 'Nuoro'),
    ('OT' , 'Olbia-Tempio'),
    ('OR' , 'Oristano'),
    ('PD' , 'Padova'),
    ('PA' , 'Palermo'),
    ('PR' , 'Parma'),
    ('PV' , 'Pavia'),
    ('PG' , 'Perugia'),
    ('PU' , 'Pesaro e Urbino'),
    ('PE' , 'Pescara'),
    ('PC' , 'Piacenza'),
    ('PI' , 'Pisa'),
    ('PT' , 'Pistoia'),
    ('PN' , 'Pordenone'),
    ('PZ' , 'Potenza'),
    ('PO' , 'Prato'),
    ('RG' , 'Ragusa'),
    ('RA' , 'Ravenna'),
    ('RC' , 'Reggio Calabria'),
    ('RE' , 'Reggio Emilia'),
    ('RI' , 'Rieti'),
    ('RN' , 'Rimini'),
    ('RM' , 'Roma'),
    ('RO' , 'Rovigo'),
    ('SA' , 'Salerno'),
    ('VS' , 'Medio Campidano'),
    ('SS' , 'Sassari'),
    ('SV' , 'Savona'),
    ('SI' , 'Siena'),
    ('SR' , 'Siracusa'),
    ('SO' , 'Sondrio'),
    ('TA' , 'Taranto'),
    ('TE' , 'Teramo'),
    ('TR' , 'Terni'),
    ('TO' , 'Torino'),
    ('OG' , 'Ogliastra'),
    ('TP' , 'Trapani'),
    ('TN' , 'Trento'),
    ('TV' , 'Treviso'),
    ('TS' , 'Trieste'),
    ('UD' , 'Udine'),
    ('VA' , 'Varese'),
    ('VE' , 'Venezia'),
    ('VB' , 'Verbano-Cusio-Ossola'),
    ('VC' , 'Vercelli'),
    ('VR' , 'Verona'),
    ('VV' , 'Vibo Valentia'),
    ('VI' , 'Vicenza'),
    ('VT' , 'Viterbo'),
)
rt_province = [x[::-1] for x in t_province] 

d_provincie = dict(t_province)
rd_provincie = dict(rt_province)

def test():
    from pprint import pprint
    pprint(t_province)
    pprint(rt_province)
    pprint(d_provincie)
    pprint(rd_provincie)
    print "\n"
    print repr(rd_provincie)
    
if __name__=="__main__":
    test()
    