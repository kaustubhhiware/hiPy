eng2sp = dict()
print 'Empty dictionary : ',eng2sp

eng2sp['one']='uno'
print '\nSingle element : ',eng2sp


eng2sp = {'one':'uno','two':'dos','three':'tres'}
print '\neng2sp = {\'one\':\'uno\',\'two\':\'dos\',\'three\':\'tres\'}'
print eng2sp
print 'Arranged arbitrarily ,each time in #table'

print '\nlength of dict : ',len(eng2sp)

print 'searching key : '
print 'one in eng2sp :','one' in eng2sp 
print 'uno in eng2sp : ','uno' in eng2sp

print '\nsearching value : '
vals = eng2sp.values()
print 'one in eng2sp :','one' in vals 
print 'uno in eng2sp : ','uno' in vals



