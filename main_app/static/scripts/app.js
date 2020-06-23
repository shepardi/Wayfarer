let orange = $('#city-name');
let posts= $('.posts');
let btnPrev=$('#prev')
let btnNext=$('#next')
let paginationNumber=0


if (orange.val() == 'London') {
  $('#london').addClass("current")
};
if (orange.val() == 'San Francisco') {
  $('#sanfrancisco').addClass("current")
};
if (orange.val() == 'Sydney') {
  $('#sydney').addClass("current")
};
if (orange.val() == 'Seattle') {
  $('#seattle').addClass("current")
};


function pagination(number){
   console.log(posts.length)
if(number==0){
  btnPrev.css('visibility' , 'hidden')
}
else{
  btnPrev.css('visibility' , 'visible')
}
if(number+4>=posts.length){
  btnNext.css('visibility' , 'hidden')
}
else{
  btnNext.css('visibility' , 'visible')
}
let temp=number
for( let i=0 ; i<posts.length ; i++  ){
  posts.eq(i).eq(0).css('display' , 'none')
}
for( number ; number<temp+4 ; number++  ){
    posts.eq(number).eq(0).css('display' , 'block')
}

}

pagination(paginationNumber)


btnPrev.on('click',function(){
  paginationNumber-=4
  pagination(paginationNumber)
})

btnNext.on('click',function(){
  paginationNumber+=4
  pagination(paginationNumber)
})