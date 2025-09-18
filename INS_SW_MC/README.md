# Dataset Description

Each directory, corresponding to a compound in the [`Compounds`](./Compounds) directory, contains the following files and information:

1. **Structure file (VESTA format)**  
   - Can be visualized using [VESTA](https://jp-minerals.org/vesta/en/).  
   - Nearest neighbors for exchange interactions are indicated by red bars.  

2. **Structure image (`.jpeg`)**  
   - Illustrates the crystal structure and exchange interactions.  
   - Exchange paths are labeled (e.g., *J₁, J₂, …*).  

3. **README.md**  
   - Contains:  
     - Exchange interactions (in **meV**)  
     - Experimental transition temperature (**K**)  
     - Monte Carlo transition temperature and corrected Monte Carlo transition temperature (**K**)  
     - Spin values for the magnetic moments in the structure (e.g., 1/2, 1, 3/2, 2, …)  
     - References for experimental transition temperatures and exchange interactions obtained from inelastic neutron scattering  

4. **Transition temperature file (`T.txt`)**  
   - Contains:  
     - Experimental transition temperature (*T_exp*)  
     - Monte Carlo transition temperature (*T_MC*)  
     - Corrected transition temperature (*T_MC* = (S+1)/S × T_MC)  
     - Spin value (*S*) for the magnetic moment  
   - All temperatures are given in **Kelvin**.  

5. **Detailed exchange interactions (`detailed_Jij.json`)**  
   - A structured JSON file including:  
     - Exchange interactions *J(i,j)*  
     - Fractional coordinates of sites *i* and *j*  
     - Elements of sites *i* and *j*  
     - Interatomic distance  

6. **MC directory**  
   - Contains input and output files from [ESpinS](https://github.com/nafiserb/ESpinS) used for Monte Carlo simulations.  

