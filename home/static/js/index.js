x=1;
function add(){
    if(x<3){
        x++;
        document.getElementById("s_img").src="assets/img/indeximg"+x+".png";
    }else{
        x=1;
        document.getElementById("s_img").src="assets/img/indeximg"+x+".png";
    } 
}
function minus(){
    if(x>1){
        x--;
        document.getElementById("s_img").src="assets/img/indeximg"+x+".png";
    }else{
        x=3;
        document.getElementById("s_img").src="assets/img/indeximg"+x+".png";
    } 
}
