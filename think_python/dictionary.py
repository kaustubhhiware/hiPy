
def invert_dict(d):
	inverse = dict()
	for key in d:

		val = d[key]

		if val not in inverse:
			inverse[val] = key
		else:
			inverse[val].append(key)
	return inverse

def invert_dict_imp(d):
	inverse = {}
	
	for key, val in d.iteritems():
		inverse.setdefault(val, []).append(key)#just like histogram from wordabulary
	
	return inverse



#moved here from Wordabulary as not dictionary ready
def reverse_lookup(d,val):
	"""
		build a list of k's
		search k s.t d[k] = val
	"""
	listed = []
	for k in d:
		if d[k]==val:
			listed.append(k)

	return listed

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

duply = eng2sp
print 'inverting dicts : ',invert_dict_imp(duply)
