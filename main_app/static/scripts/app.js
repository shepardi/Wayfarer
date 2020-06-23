let orange = $('#city-name');
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






