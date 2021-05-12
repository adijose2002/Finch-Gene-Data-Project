"""
CS/BIOS 112 - Program Design I

For this project, I will work with a portion of this gene, known as ALX1, from four species, 5-10 individuals each, of Darwin’s finches + 1 outgroup, L. noctis (the Lesser Antillean Bullfinch).
    Synthesizing Python knowledge: loops, conditions, strings, lists, functions, random functions, modules, plotting.
    DNA vs phenotype.

File: project_02.py

@author:   <Adithya Jose>
UIC NetId: <668871768>
Due Date:  <11/02/2020>
"""

# species named in the data file finches_2020.csv 
finch1 = 'G.conirostris_Espanola'
finch2 = 'G.conirostris_Genovesa'
finch3 = 'G.difficilis'
finch4 = 'G.magnirostris'
outgroup = 'L.noctis'

def read_input(fileName):
    ''' This function is to read the CSV file, assuming the column input format is [species, Individual ID, allele (A or B), gene sequence, beak shape score (i.e., the degree of pointedness), beak type] and creating a list variable for each individual of length 7 with the format [species, Individual ID, alleleA gene, alleleB gene, alleleA beak shape score, alleleB beak shape score, beak type]. '''
    
    import csv
    
    fileref = open(fileName, "r")
    data_reader = csv.reader(fileref)
    row = []
    
    for i in data_reader:
        if(i[2] == 'A'):
            x = i
            del x[2]
        else:
            x.insert(3, i[3])
            x.insert(4, i[5])
            row.append(x)
    
    fileref.close()
    
    return row
   
def allele_dist(gene1, gene2):
    ''' Takes 2 strings as arguments. Returns the Hamming Distance between the two arguments. Assumes both argument strings are of same length. ''' 
    
    x = 0
    
    for i in range(len(gene1)):
        if (gene1[i] != gene2[i]):
            x = x + 1
            
    return x
       
def gene_dist(finch1, finch2):
    '''  Takes 2 arguments: list for an individual finch. Returns average Hamming Distance between the genes of the two individual finches given as arguments. '''
    
    a = allele_dist(finch1[2], finch2[2])
    b = allele_dist(finch1[2], finch2[3])
    c = allele_dist(finch1[3], finch2[2])
    d = allele_dist(finch1[3], finch2[3])
    
    avg = float((a + b + c + d) / 4)
    
    return avg

def beak_dist(finch1, finch2):
    ''' Takes 2 arguments: list for an individual finch. Returns average difference between the beak score of the two individual finches given as arguments. '''
    
    a = abs(finch1[4] - finch2[4])
    b = abs(finch1[4] - finch2[5])
    c = abs(finch1[5] - finch2[4])
    d = abs(finch1[5] - finch2[5])
    
    avg = float((a + b + c + d) / 4)
    
    return avg


def outgroup_distance(finches, speciesName, outgroupName):
    ''' Takes 3 arguments:
            – list of lists returned by read_input( )
            – name of Finch Species on which to collect information
            – name of Outgroup Species
                • used to standard basis for comparing the distance
                • will always be the species: L.noctis
        Returns two lists as a Tuple:
            – list of the gene differences for all individuals in that Finch Species
            – list of the beak differences for all individuals in that Finch Species '''
    
    o = [finch for finch in finches if finch[0] == outgroupName]
    s = [finch for finch in finches if finch[0] == speciesName]
    
    gd_list = []
    bd_list = []
    
    for finch1 in o:
        for finch2 in s:
            gd_list.append(gene_dist(finch1, finch2))
            bd_list.append(beak_dist(finch1, finch2))
            
    return (gd_list, bd_list)
    

def plot_data(file_name, x_column, y_column) :
    ''' Is the primary function that will call the other two functions and call the actual plotting functions. '''
    
    import matplotlib.pyplot as plt
    finch_data = read_input(file_name)
    
    x = outgroup_distance(finch_data, x_column, outgroup)
    y = outgroup_distance(finch_data, y_column, outgroup)
    plt.plot(x,y, "ro", label = "G.conirostris_Espanola")
    
    x = outgroup_distance(finch_data, x_column, outgroup)
    y = outgroup_distance(finch_data, y_column, outgroup)
    plt.plot(x,y, "bo", label = "G.conirostris_Genovesa")
    
    x = outgroup_distance(finch_data, x_column, outgroup)
    y = outgroup_distance(finch_data, y_column, outgroup)
    plt.plot(x,y, "go", label = "G.difficilis")
    
    x = outgroup_distance(finch_data, x_column, outgroup)
    y = outgroup_distance(finch_data, y_column, outgroup)
    plt.plot(x,y, "ko", label = "G.magnirostris")
    
    plt.xlabel('Gene Distance')
    plt.ylabel('Beak Distance')
    plt.legend(shadow=True, loc="upper right")
    plt.title("Beak Distance vs. Gene Distance for Finches")
    
plot_data ("finches.csv", 0, 1)
    

''' 


    This dataset is perhaps the best known database in the pattern recognition literature. 
    One flinch species is linearly separable from the other four, but the other three are not linearly separable from each other.

    G.difficilis is linearly seperate when plotting Beak Distance vs. Gene Distance for Finches. G.conirostris_Espanola, G.conirostris_Genovesa, and G.magnirostris are not linearly separable from each other when plotting Beak Distance vs. Gene Distance for Finches.
    The two species would cluster together if they are indeed different species because they have similar attributes of Finches such as the obvious from the scatterplot, Beak Distance lineraly alligning with Gene Distance.


'''