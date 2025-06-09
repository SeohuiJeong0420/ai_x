function sumAll(){
    //매개변수가 없으면 -999return
    //매개변수가 있으면 매개변수들의 합을 return
    let result=0;
    if(arguments.length==0){
        result= -999
    }else if(arguments.length>=1){
        for(var data of arguments){
            result += data;
        }
    }
    return result;
}
//test
//console.log(sumAll());
//console.log(sumAll(1, 2));
//console.log(sumAll(1, 2, 3, 4, 5));