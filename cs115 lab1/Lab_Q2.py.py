team=input('enter name of team:')
won=int(input('enter number of games won:'))
lost=int(input('enter number of games lost:'))
p=(won*100)/(won+lost)
print('{} won {:.1f}% of their games'.format(team,p))