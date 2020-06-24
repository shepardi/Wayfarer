let orange = $('#city-name');
let posts = $('.posts');
let btnPrev = $('#prev');
let btnNext = $('#next');
let paginationNumber = 0
let form = $('#delete-form');
let no = $('#no');
let deleteBtn = $('#delete-btn');

let mainPic = $('#main-pic');


if (orange.val() == 'London') {
  $('#london').addClass("current");
  mainPic.attr('src', '../static/images/bigben.jpg');
};

if (orange.val() == 'San Francisco') {
  $('#sanfrancisco').addClass("current");
  mainPic.attr('src', '../static/images/goldengate.jpg');
};

if (orange.val() == 'Sydney') {
  $('#sydney').addClass("current");
  mainPic.attr('src', '../static/images/syd-beach.jpg');
};

if (orange.val() == 'Seattle') {
  $('#seattle').addClass("current");
  mainPic.attr('src', '../static/images/spaceneedle.jpg');
};

// Pagination
function pagination(number) {
  console.log(posts.length)
  if (number == 0) {
    btnPrev.css('visibility', 'hidden')
  }
  else {
    btnPrev.css('visibility', 'visible')
  }
  if (number + 3 >= posts.length) {
    btnNext.css('visibility', 'hidden')
  }
  else {
    btnNext.css('visibility', 'visible')
  }
  let temp = number
  for (let i = 0; i < posts.length; i++) {
    posts.eq(i).eq(0).css('display', 'none')
  }
  for (number; number < temp + 3; number++) {
    posts.eq(number).eq(0).css('display', 'block')
  }

}

pagination(paginationNumber)


btnPrev.on('click', function () {
  paginationNumber -= 3
  pagination(paginationNumber)
})

btnNext.on('click', function () {
  paginationNumber += 3
  pagination(paginationNumber)
})

no.on('click', function () {
  form.css('display', 'none')
})

deleteBtn.on('click', function () {
  form.css('display', 'block')
})