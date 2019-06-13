#Tongxu Cai
#1996/4/3
#Homework 1
year=input('what year were you born in?')
variable=int(year)
if variable >= 2020:
    year=input('what year were you born in?')
variable=int(year)
print('You are', 2019-variable, 'years old')
print('Your heart has beaten',60*60*24*365*variable/1000000,'millions time.')
print("A blue whale's heart has beaten",8*60*24*365*variable/1000000, 'million times.')
print("A rabbit's heart has beaten",120*60*24*365*variable/1000000,'million times.')
print('I am',variable*0.616,'years old in Venus years.')
print('I am', variable*365,'years old in Neptune years.')
if variable > variable*0.6161:
    print('Your Venus age is', variable-variable*0.6161,'younger than you.')
if variable < variable*365:
    print('Your Neptune age is', variable*365-variable,'older than you.')
if variable%2==0:
    print('You were born in an even year.')
if variable%2!=0:
    print('You were born in an odd year.')
if 2009<variable < 2017: 
    print('Obama was in office.')
if 1974<variable<1988:
    print('Gerald Ford was in office.')
if 1981<variable<1989:
    print('Ronald Reagan was in office.')
if 1993<variable<2001:
    print('William.J.Clinton was in office.')
if 2001<variable<2009:
    print('George W.Bush was in office.')
if variable>2017:
    print('Trump is in office.')
if 1993<variable<2001:
    print('William.J.Clinton was in office.')
else:
    print('I do not know which president was in office.')


#Soma's version
year=input('what year were you born?')
print(year)

age=2019-int(year)
print(age)

heartbeats=age*70*60*24*365
print(heartbeats)

whale_heartbeats=age*8*60*24*365
print("the whale's heart has beaten"+ str(whale_heartbeats)+"times")
print(f"the whale's heart has beaten{whale_heartbeats} times")