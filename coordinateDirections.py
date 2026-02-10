directions = []
print('Please enter coordinates, i.e n,s,e,w or N,S, E ,W')

while True:
    coords = input().upper()
    if coords == "":
        break
    if coords in ['N', 'S', 'W', 'E']:
        directions.append(coords)
    else:
        print('Invalid input! please enter a valid input')
def get_end_coordinates(directions):
    results = [0,0]
    
    for i in directions :
        if i == 'E':
            results[0] += 1
        elif i == 'W':
            results[0] -= 1
        elif i == 'N':
            results[1] += 1
        elif i == 'S':
            results[1] -= 1
        
    return results
    
print(get_end_coordinates(directions))

    
