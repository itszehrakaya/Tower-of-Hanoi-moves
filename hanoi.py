def hanoi(n, source, auxiliary, target):
    """
    Recursive function to solve Tower of Hanoi puzzle and list all the moves.

        n (int): Number of disks.
        source (str): Source peg.
        auxiliary (str): Auxiliary peg.
        target (str): Target peg.


    """
    if n > 0:
        # Move n-1 disks from source peg to auxiliary peg
        hanoi(n-1, source, target, auxiliary)
        
        # Print the move
        print(f"Move disk {n} from {source} to {target}")
        
        # Move n-1 disks from auxiliary peg to target peg
        hanoi(n-1, auxiliary, source, target)


if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    print(f"Moves to solve Tower of Hanoi with {n} disks:")
    hanoi(n, "A", "B", "C")
