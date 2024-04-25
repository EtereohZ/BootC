var h1 = document.getElementById("h1");
var h2 = document.getElementById("h2");
var h3 = document.getElementById("h3");
var hpromedio = document.getElementById("hpromedio");


nota1h = Number(prompt("Ingrese su nota 1 de la unidad HTML"));
h1.innerHTML = nota1h
nota2h = Number(prompt("Ahora ingrese su nota 2 {HTML}"));
h2.innerHTML = nota2h
nota3h = Number(prompt("Por último, su nota 3 {HTML}"));
h3.innerHTML = nota3h
hpromedio.innerHTML = (nota1h + nota2h + nota3h) /3


var c1 = document.getElementById("c1");
var c2 = document.getElementById("c2");
var c3 = document.getElementById("c3");
var salario = document.getElementById("salario");

nota1c = Number(prompt("Ingrese su nota 1 de la unidad CSS"));
c1.innerHTML = nota1c
nota2c = Number(prompt("Ahora ingrese su nota 2 {CSS}"));
c2.innerHTML = nota2c
nota3c = Number(prompt("Por último, ingrese su nota 3 {CSS}"));
c3.innerHTML = nota3c
cpromedio.innerHTML = (nota1c + nota2c + nota3c) /3

var j1 = document.getElementById("j1");
var j2 = document.getElementById("j2");
var j3 = document.getElementById("j3");
var salario = document.getElementById("salario");

nota1j = Number(prompt("Ingrese su nota 1 de la unidad Js"));
j1.innerHTML = nota1j
nota2j = Number(prompt("Ahora ingrese su nota 3 {Js}"));
j2.innerHTML = nota2j
nota3j = Number(prompt("Por último, ingrese su nota 3 {Js}"));
j3.innerHTML = nota3j
jpromedio.innerHTML = (nota1j + nota2j + nota3j) /3