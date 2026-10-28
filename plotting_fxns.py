# function definitions for plotting

#build dictionary: needs string as input
def build_dict(words):
    d = dict()
    for char in words:
        d[char] = d.get(char,0) + 1
    return d

def plot_hist(data):

# We can set the number of bins with the *bins* keyword argument. 

    plt.hist(data,bins=7)

    plt.ylabel('Counts')
    plt.title('Frequency of letters') 

    plt.show()

def plot_bar(d, plot_title):
    plt.bar(list(d.keys()), d.values())
    plt.ylabel('Counts')
    plt.title(plot_title) 
    plt.show()
