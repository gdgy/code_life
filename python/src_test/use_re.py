#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 17:36
# @Author  : shaoyong_li
# @Site    : 
# @File    : use_re.py
import re
pattern = re.compile('公司')
a = pattern.findall("""　公司是指全部资本由股东出资构成，以营利为目的而依法设立的一种企业组织形式；公司是具有民事权利能力和行为能力，股东以其出资额或所持股份为限对公司承担责任，公司以其全部资产对公司的债务承担责任，依照公司法成立的企业法人。

　　公司的这一定义，主要对以下几个方面的问题进行了强调：

　　1．公司依法设立

　　所谓公司依法成立有三个含义，意思是说：

　　⑴ 公司成立应依据专门的法律，即公司法和其他有关的特别法律、行政法规； 如依本法成立的，有限责任公司和股份有限公司。依其他法设立。比如，经营烟草制品批发的公司，要依《烟草专卖法》，取得许可证才行。

　　⑵ 公司成立应符合公司法规定的实质要件；

　　⑶ 公司成立须遵循公司法规定的程序，履行规定的申请和审批登记手续。

　　2．公司以营利为目的

　　所谓营利，就是获取经济上的利益。以营利为目的是公司与机关、事业单位和社会团体法人的主要区别所在。也就是说，公司是一个营业实体：

　　首先，公司拥有营业财产，即人们为营利目的而通过投资、借贷、积累等方式形成的属于公司的有组织财产；

　　其次，公司从事营业活动，即公司以营利为目的而运用营业财产所从事的各种生产经营活动。

　　3．公司是法人

　　⑴ 公司的法人属性使公司财产与公司成员的个人财产完全区别开来，从而使公司能够以自己的名义独立地从事民事活动、享受民事权利和承担民事义务。

　　⑵ 公司有自己独立的组织机构，公司的主体身份是法人，法人是法律上拟制的人格；主体需要一定的人格才能享有民事权利能力和民事行为能力。

　　⑶ 公司的财产是公司拥有信用的基础，也是公司对外承担民事责任的基础。所以，公司可以用自己的资产对外承担责任。

　　⑷ 由于公司在人格上和财产上的独立性，股东不必对公司债务承担连带责任和无限责任。

　　⑸公司法人的民事权利能力由其法定代表人和授权代表人代为行使，根据公司法的规定，公司的法定代表人是董事长，公司的授权代表人是由公司的董事会和董事长授权的公司职员。法定代表人和授权代表人的行为就构成了公司的行为，由此产生的一切后果均由公司承受，也就是公司职员的任何职务行为均由公司的资产对外承担民事责任。""")
if a:
    print ','.join(a)
