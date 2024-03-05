let solveBtn = document.querySelector('.solveBtn');
let inputCalc = document.querySelector('.inputCalc');
let clear = document.querySelector('.clear');
let calcBtn = document.querySelectorAll('.calcBtn');
let result_calc_history = document.querySelectorAll('.result_calc_history');
let expression_history = document.querySelectorAll('.expression_history');

solveBtn.addEventListener( 'click', function(event) {
    event.preventDefault();
    const equation = inputCalc.value;
    let copyEquation = equation;
    if (equation === ''){
        alert('Please enter an expression!')
    } else {
        let result = eval(equation);
        inputCalc.value = result;
        var xhr = new XMLHttpRequest();
        xhr.open("GET","/?data="+encodeURIComponent(copyEquation),true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send();
    }
} );

for (let index = 0; index < result_calc_history.length; index++) {
    result_calc_history[index].innerHTML = eval(expression_history[index].innerHTML)
    
}

clear.addEventListener('click', ()=>{
   inputCalc.value='';  
});

calcBtn.forEach((btn) => {
  btn.addEventListener("click", function(){
      let currentVal = inputCalc.value;
      inputCalc.value += btn.innerHTML;
  });
});

