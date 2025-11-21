# different ways to code print statement
# formatted printing
pi = 22/7
print(f'the value of PI is = {pi}')
print('the value of PI is = {0}'.format(pi))
print('the value of PI is = %f' % (pi))


# uing (format specifier) like .2f,.3f to explicitly get only 2values after decimal
print(f'the value of PI is = {pi:.2f}')
print('the value of PI is = {0:.3f}'.format(pi))
print('the value of PI is = %.4f' % (pi))

