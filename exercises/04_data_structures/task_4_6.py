# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"


ospf1 = ospf_route
ospf1 = ospf1.lstrip()
ospf1= ospf1.split(",")
#print(ospf1)
ospf0 = ospf1[0].split()
ospf3 = str(ospf0[1].strip('[]'))
ospf0.append(ospf3)
ospf0.pop(1)
ospf0.pop(1)

ospf2 =ospf0 + ospf1 [1:]

#print (ospf2)

pref, hop,ad, timr, intf = ospf2


#print("\n",pref, ad,us, hop, timr, intf)

a = "\nPrefix {:>30}\nAD/Metric {:>21} \nNext-Hop {:>25}\nLast update {:>18} \nOutbound Interface {:>21}\n".format (pref, ad,hop, timr, intf)

print (a)