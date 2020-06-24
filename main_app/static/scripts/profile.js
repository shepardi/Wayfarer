
//Related Post Image
let img = $('.post-img')
let input = $('.post-input')

// For
for (let i = 0; i < input.length; i++) {
    if (input.eq(i).val() === "LDN") {
        img.eq(i).attr('src', '../static/images/london-aerial.jpg')
    }
    if (input.eq(i).val() === "SYD") {
        img.eq(i).attr('src', '../static/images/syd-beach.jpg')
    }
    if (input.eq(i).val() === "SFO") {
        img.eq(i).attr('src', '../static/images/sanfran.jpg')
    }
    if (input.eq(i).val() === "SEA") {
        img.eq(i).attr('src', '../static/images/seattle.jpg')
    }
}