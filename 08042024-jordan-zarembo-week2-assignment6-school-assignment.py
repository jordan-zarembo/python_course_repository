########################################################
#
# 08022024 Currency conversion calculator
# Please note: USD/EUR conversion rates are as of
# August 2nd, 2024 at 2:30 pm, per xe.com
#
# $1 USD = €0.916421
# €1 = $1.09127 USD
#
#This program will ask for conversion both from
#USD ---> EUR and EUR ---> USD
#
#######################################################
#
#
usd = float(input('Enter a value in USD: $ '))
eur_value=(usd * 0.916421)
x = "{:.2f}".format(eur_value)
print('The USD value in EUR is:', x)
#

eur = float(input('Enter a value in EUR: € '))
usd_value=(eur * 1.09127)
y = "{:.2f}".format(usd_value)
print('The EUR value in USD is:', y)
#
#
