import numpy as np
import pandas as pd

# Define number of SNPs and individuals
num_snps = 100
num_individuals = 10

# Generate SNP data
snp_data = np.random.randint(0, 3, size=(num_snps, num_individuals))
# Generate chromosomes
chromosome = np.sort(np.random.randint(1, 20, size=num_snps))
# Generate  SNP positions
snp_positions = np.sort(np.random.randint(1, 1000000, size=num_snps))

snp_df = pd.DataFrame(snp_data, columns=['Individual'+str(i) for i in range(1, num_individuals+1)], index=['SNP'+str(i) for i in range(1, num_snps+1)])

snp_df['Position'] = snp_positions
snp_df['Chr'] = chromosome
# Save the SNP dataframe to CSV file
snp_df.to_csv('random_snp.csv')
