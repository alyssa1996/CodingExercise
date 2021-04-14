def solution(dirs):
    answer=0
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    directions=['U','D','R','L']
    current=(0,0)
    path=[]
    for i in range(len(dirs)):
        index=directions.index(dirs[i])
        nx=current[0]+dx[index]
        ny=current[1]+dy[index]
        if -5<=nx<=5 and -5<=ny<=5:
            right_path=(current[0],current[1],nx,ny)
            op_path=(nx,ny,current[0],current[1])
            if right_path not in path and op_path not in path:
                path.append(right_path)
                path.append(op_path)
            current=(nx,ny)
    return len(path)//2
