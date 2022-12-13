function isIsomorphic(origin, mapped){
    let map = new Map();
    for(let i=0; i<origin.length; i++){
        if (map.has(origin[i]) ){
            if (map.get(origin[i]) == mapped[i])
                continue;
            else
                return false;
        }
        else{
            if(!contains(map.values(), mapped[i]))
                map.set(origin[i], mapped[i])
            else 
                return false
        }
    }
    return true;
}

function contains(list, value){
    for (const element of list){
        if (value == element)
            return true
    }
    return false
}

exports.isIsomorphic = isIsomorphic;
exports.contains = contains;