var womans = document.getElementsByClassName('woman')
var mans = document.getElementsByClassName('man')
var childs = document.getElementsByClassName('child')
const openMan = () => {
    for(var i=0; i<mans.length; i++)mans[i].style.display='flex';
    for(var i=0; i<womans.length; i++)womans[i].style.display='none';
    for(var i=0; i<childs.length; i++)childs[i].style.display='none';

}

const openWoman = () => {
    for(var i=0; i<womans.length; i++)womans[i].style.display='flex';
    for(var i=0; i<mans.length; i++)mans[i].style.display='none';
    for(var i=0; i<childs.length; i++)childs[i].style.display='none';

}

const openChild = () => {
    for(var i=0; i<childs.length; i++)childs[i].style.display='flex';
    for(var i=0; i<womans.length; i++)womans[i].style.display='none';
    for(var i=0; i<mans.length; i++)mans[i].style.display='none';

}

