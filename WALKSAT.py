# importing Libraries
import random


# Check if clause is satisfied or not
def check_satisfied_clause(clause, assignment):
  
   return any ( assignment[symbol] for symbol in clause )


# Count the no. of clauses satisfied if the symbol is flipped.
def count_satisfied_clauses(symbol, unsatisfied_clauses, assignment):
    
    assignment[symbol] = not assignment[symbol]
    n = sum(check_satisfied_clause(clause, assignment) for clause in unsatisfied_clauses)
    assignment[symbol] = not assignment[symbol]
    return n



def WalkSat ( clauses , probability , n_flips ):
    
    symbols = set()
    for clause in clauses:
     symbols.update(clause)
    symbols = list(symbols)
    assignment = { symbol : random.choice ([ True , False ]) for symbol in symbols }
    for i in range ( n_flips ):
        satisfied_clauses = [ clause for clause in clauses if check_satisfied_clause ( clause , assignment )]
        if len ( satisfied_clauses ) == len ( clauses ):
            return assignment
        unsatisfied_clauses = [ clause for clause in clauses if not check_satisfied_clause ( clause , assignment )]
        unsatisfied_clause = random.choice ( unsatisfied_clauses )
        if random.random () < probability:
            symbol = random.choice(unsatisfied_clause)
        else :
            symbol = max(symbols , key = lambda symbol : count_satisfied_clauses(symbol, unsatisfied_clauses, assignment))
        assignment[symbol] = not assignment[symbol]
    return None




def main():
    
    for i in range(10):
        
        # Generate random 3-CNF sentences
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        clauses = []
        for j in range(m):
            clause = []
            for k in range(3):
                clause.append(random.randint(1, n))
            clauses.append(clause)
        print("---------------------------------------------------------------------------------------------")
        print("\nITERATION: ",i+1,"\n\nClauses: ", clauses)
        
        assignment = WalkSat(clauses, 0.5, 100)
        if assignment is None:
            print("# No solution")
        else:
            print("\nFinal Assignment: ", assignment)
            print("Satisfied clauses: \n", [clause for clause in clauses if check_satisfied_clause(clause, assignment)])



main()
