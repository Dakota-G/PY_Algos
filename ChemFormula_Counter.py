# Create a funciton that takes in a chemical formula and returns a dict with a count of the elements
# Challenge: Solve without using regex or imported tools (ie only for/while loops/conditionals/built-in methods)

compound_formula='Ce25H3K3Fe129CAuQ'
# Ought to output {'Ce': '25', 'H': '3', 'K': '3', 'Fe': '129', 'C': '0', 'Au': '0' 'Q': '0'}
chem_d={}
z = 0
while z < len(compound_formula):
    a = 1
    num = ''
# Check to see if the pointer is on a capital letter (start of an element)
    if compound_formula[z].isupper():
# Make sure that the element isn't a single letter at the end of the compound
        if z+1 < len(compound_formula):
# If the element has two letters in the abbreviation, this is true
# We then check everything that comes after it, anything that is a number is added to num
# Finally, num is the key to the element in the dict
# It is important to make sure that we aren't exceeding the length of the str, or else we will get an error
            if compound_formula[z+1].isalpha() == True and compound_formula[z+1].isupper() == False: 
                if z+1+a < len(compound_formula) and compound_formula[z+1+a].isnumeric():
                        while compound_formula[z+1+a].isnumeric():
                            num += compound_formula[z+1+a]
                            if(z + 1 + a + 1 < len(compound_formula)):
                                a += 1
                            else:
                                break
# If there is no number after both letters, we set num to 0
                else:
                    num = '0'
                chem_d[compound_formula[z]+compound_formula[z+1]] = num
# Same as above, but for a single-letter element abbr.
            else:
                if compound_formula[z+a].isnumeric():
                    while compound_formula[z+a].isnumeric():
                        num += compound_formula[z+a]
                        if(z + a + 1 < len(compound_formula)):
                            a += 1
                        else:
                            break
                else: 
                    num = '0'
                chem_d[compound_formula[z]] = num
# If a single letter ends the compound, record it with 0 
        else:
            chem_d[compound_formula[z]] = '0'
    z += 1
    print(z)

print(chem_d)