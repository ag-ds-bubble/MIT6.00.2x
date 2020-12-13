import locale
locale.setlocale(locale.LC_MONETARY, 'en_IN')
import matplotlib.pyplot as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base+=[i]
        savings += [savings[-1]*(1+mRate)+monthly]
    return base, savings


def displayRettireM(monthlies, rates, terms):
    plt.figure('Retire Month')
    plt.clf()
    plt.xlim(terms-10, terms)
    monthly_color = ['k', 'r', 'g', 'b']
    rate_style = ['^-', '-', 'o-']
    for emidx, emonth in enumerate(monthlies):
        for eridx, erate in enumerate(rates):
            xvals, yvals = retire(emonth, erate, terms)
            accum_val = str(locale.currency(int(round(yvals[-1])), grouping=True)).replace('?','₹')
            _style = monthly_color[emidx%len(monthly_color)] + rate_style[eridx%len(rate_style)]
            plt.plot(xvals, yvals, _style, label=f'Retire @ {emonth} pm, Accumulated upto {accum_val}')
            plt.legend(loc='upper left')
    plt.grid()
    plt.show()

total_months = 36*12
displayRettireM(list(range(1000, 21_000, 5000)), [0.05, 0.06, 0.07, 0.08], total_months)
