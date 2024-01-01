#! /usr/bin/env python3

print(globals())
print(f"__name__ >>> {__name__}")

def sum( ):
    print(f"sum >>>  {12 + 3}")

def square():
    print( f"Square >>> {22 * 88}" )

def main():
    print( "Great! We turn ON main func" )
    sum()
    square()


if __name__ == "__main__":
    print( "Good job, Veronika!!!" )
    main()
else:
    raise SystemExit("it's not a lib") 
    print( f"main >>> {__name__}" )
