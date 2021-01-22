function solution(skill, skill_trees) {
    var answer = 0;
    var skill_array=skill.split("");
    skill_trees.forEach(element=>{
        var item=element.split("");
        var nextCheck=0;
        var checkFine=true;
        for(const [index,value] of item.entries()){
            if(skill_array.indexOf(value)===-1){
                continue;
            }else{
                if(value===skill_array[nextCheck]){
                    nextCheck=nextCheck+1
                }
                else{
                    checkFine=false;
                    break
                }
            }
        }
        if(checkFine){
                answer+=1;
        }
    })
    return answer;
}