<html>
<head>
<title>Calculadora Cientifica Real</title>
<style>
body { background-color: #222; color: white; font-family: sans-serif; text-align: center; }
.calc { border: 2px solid #555; background: #333; padding: 15px; width: 320px; margin: 20px auto; border-radius: 10px; }
        #pantalla { width: 100%; height: 45px; font-size: 22px; text-align: right; margin-bottom: 15px; background: #111; color: #00ffcc; border: 1px solid #555; padding: 5px; box-sizing: border-box; }
        input[type="button"] { width: 55px; height: 40px; font-size: 14px; margin: 2px; cursor: pointer; background: #444; color: white; border: none; border-radius: 4px; font-weight: bold; }
input[type="button"]:active { background: #666; }
.op { background: #f55 !important; }
.sci { background: #f93 !important; color: black !important; }
.cte { background: #b8f !important; color: black !important; }
.eq { background: #0fc !important; color: black !important; width: 115px !important; }
    </style>
      </head>
        <body>

        <div class="calc">
<input type="text" id="pantalla" value="0" readonly>

<table border="0" align="center" cellpadding="0" cellspacing="0">
<tr>
<td><input type="button" class="op" value="C" onclick="limpiar()"></td>
<td><input type="button" class="sci" value="√" onclick="cientifica('raiz2')"></td>
<td><input type="button" class="sci" value="∛" onclick="cientifica('raiz3')"></td>
<td><input type="button" class="sci" value="x²" onclick="cientifica('cuadrado')"></td>
<td><input type="button" class="op" value="÷" onclick="operar('/')"></td>
</tr>
<tr>
<td><input type="button" class="sci" value="ln" onclick="cientifica('ln')"></td>
<td><input type="button" class="sci" value="log" onclick="cientifica('log')"></td>
<td><input type="button" class="sci" value="xʸ" onclick="operar('potencia')"></td>
<td><input type="button" class="sci" value="x!" onclick="cientifica('factorial')"></td>
<td><input type="button" class="op" value="×" onclick="operar('*')"></td>
</tr>
<tr>
<td><input type="button" class="sci" value="sin" onclick="cientifica('sin')"></td>
<td><input type="button" class="sci" value="cos" onclick="cientifica('cos')"></td>
<td><input type="button" class="sci" value="tan" onclick="cientifica('tan')"></td>
<td><input type="button" class="cte" value="π" onclick="constante('pi')"></td>
<td><input type="button" class="op" value="-" onclick="operar('-')"></td>
</tr>
<tr>
<td><input type="button" value="7" onclick="numero('7')"></td>
<td><input type="button" value="8" onclick="numero('8')"></td>
<td><input type="button" value="9" onclick="numero('9')"></td>
<td><input type="button" class="cte" value="e" onclick="constante('e')"></td>
<td><input type="button" class="op" value="+" onclick="operar('+')"></td>
</tr>
<tr>
<td><input type="button" value="4" onclick="numero('4')"></td>
<td><input type="button" value="5" onclick="numero('5')"></td>
<td><input type="button" value="6" onclick="numero('6')"></td>
<td><input type="button" class="sci" value="1/x" onclick="cientifica('inverso')"></td>
<td><input type="button" class="sci" value="±" onclick="cientifica('signo')"></td>
</tr>
<tr>
<td><input type="button" value="1" onclick="numero('1')"></td>
<td><input type="button" value="2" onclick="numero('2')"></td>
<td><input type="button" value="3" onclick="numero('3')"></td>
<td colspan="2"><input type="button" class="eq" value="=" onclick="total()"></td>
</tr>
<tr>
<td colspan="2"><input type="button" value="0" style="width:115px;" onclick="numero('0')"></td>
<td><input type="button" value="." onclick="numero('.')"></td>
<td colspan="2"></td>
</tr>
</table>
</div>

<script>
var p = document.getElementById('pantalla');
var n1 = 0;
var sig = "";
var borrar = false;

function numero(n) {
if (p.value === "0" || p.value === "Error" || borrar) {
    p.value = n;
borrar = false;
} else {
if (n === "." && p.value.indexOf(".") !== -1) return;
p.value += n;
}
}

function constante(tipo) {
if (tipo === "pi") p.value = Math.PI;
if (tipo === "e") p.value = Math.E;
borrar = false;
}

function limpiar() {
    p.value = "0";
n1 = 0;
sig = "";
borrar = false;
}

function operar(op) {
    n1 = parseFloat(p.value);
sig = op;
borrar = true;
}

function cientifica(tipo) {
    var v = parseFloat(p.value);
if (isNaN(v)) return;
var r = 0;

if (tipo === "sin") r = Math.sin(v * Math.PI / 180);
if (tipo === "cos") r = Math.cos(v * Math.PI / 180);
if (tipo === "tan") r = Math.tan(v * Math.PI / 180);
if (tipo === "cuadrado") r = Math.pow(v, 2);
if (tipo === "inverso") r = 1 / v;

if (tipo === "signo") {
p.value = v * -1;
return;
}
if (tipo === "log") {
if (v <= 0) { p.value = "Error"; return; }
r = Math.log(v) / Math.LN10;
}
if (tipo === "ln") {
if (v <= 0) { p.value = "Error"; return; }
r = Math.log(v);
}
if (tipo === "raiz2") {
if (v < 0) { p.value = "Error"; return; }
r = Math.sqrt(v);
}
if (tipo === "raiz3") {
r = Math.cbrt(v);
}
if (tipo === "factorial") {
if (v < 0 || v % 1 !== 0) { p.value = "Error"; return; }
r = 1;
for (var i = 1; i <= v; i++) { r *= i; }
}

p.value = Number(r.toFixed(8));
borrar = true;
}

function total() {
if (sig === "") return;
var n2 = parseFloat(p.value);
var r = 0;
if (sig === "+") r = n1 + n2;
if (sig === "-") r = n1 - n2;
if (sig === "*") r = n1 * n2;
if (sig === "/") {
if (n2 === 0) { p.value = "Error"; return; }
r = n1 / n2;
}
if (sig === "potencia") r = Math.pow(n1, n2);

p.value = Number(r.toFixed(8));
sig = "";
borrar = true;
}
</script>

</body>
</html><html>
<head>
<title>Calculadora Cientifica Real</title>
<style>
body { background-color: #222; color: white; font-family: sans-serif; text-align: center; }
    .calc { border: 2px solid #555; background: #333; padding: 15px; width: 320px; margin: 20px auto; border-radius: 10px; }
            #pantalla { width: 100%; height: 45px; font-size: 22px; text-align: right; margin-bottom: 15px; background: #111; color: #00ffcc; border: 1px solid #555; padding: 5px; box-sizing: border-box; }
            input[type="button"] { width: 55px; height: 40px; font-size: 14px; margin: 2px; cursor: pointer; background: #444; color: white; border: none; border-radius: 4px; font-weight: bold; }
input[type="button"]:active { background: #666; }
.op { background: #f55 !important; }
.sci { background: #f93 !important; color: black !important; }
.cte { background: #b8f !important; color: black !important; }
.eq { background: #0fc !important; color: black !important; width: 115px !important; }
    </style>
      </head>
        <body>

        <div class="calc">
<input type="text" id="pantalla" value="0" readonly>

<table border="0" align="center" cellpadding="0" cellspacing="0">
<tr>
<td><input type="button" class="op" value="C" onclick="limpiar()"></td>
<td><input type="button" class="sci" value="√" onclick="cientifica('raiz2')"></td>
<td><input type="button" class="sci" value="∛" onclick="cientifica('raiz3')"></td>
<td><input type="button" class="sci" value="x²" onclick="cientifica('cuadrado')"></td>
<td><input type="button" class="op" value="÷" onclick="operar('/')"></td>
</tr>
<tr>
<td><input type="button" class="sci" value="ln" onclick="cientifica('ln')"></td>
<td><input type="button" class="sci" value="log" onclick="cientifica('log')"></td>
<td><input type="button" class="sci" value="xʸ" onclick="operar('potencia')"></td>
<td><input type="button" class="sci" value="x!" onclick="cientifica('factorial')"></td>
<td><input type="button" class="op" value="×" onclick="operar('*')"></td>
</tr>
<tr>
<td><input type="button" class="sci" value="sin" onclick="cientifica('sin')"></td>
<td><input type="button" class="sci" value="cos" onclick="cientifica('cos')"></td>
<td><input type="button" class="sci" value="tan" onclick="cientifica('tan')"></td>
<td><input type="button" class="cte" value="π" onclick="constante('pi')"></td>
<td><input type="button" class="op" value="-" onclick="operar('-')"></td>
</tr>
<tr>
<td><input type="button" value="7" onclick="numero('7')"></td>
<td><input type="button" value="8" onclick="numero('8')"></td>
<td><input type="button" value="9" onclick="numero('9')"></td>
<td><input type="button" class="cte" value="e" onclick="constante('e')"></td>
<td><input type="button" class="op" value="+" onclick="operar('+')"></td>
</tr>
<tr>
<td><input type="button" value="4" onclick="numero('4')"></td>
<td><input type="button" value="5" onclick="numero('5')"></td>
<td><input type="button" value="6" onclick="numero('6')"></td>
<td><input type="button" class="sci" value="1/x" onclick="cientifica('inverso')"></td>
<td><input type="button" class="sci" value="±" onclick="cientifica('signo')"></td>
</tr>
<tr>
<td><input type="button" value="1" onclick="numero('1')"></td>
<td><input type="button" value="2" onclick="numero('2')"></td>
<td><input type="button" value="3" onclick="numero('3')"></td>
<td colspan="2"><input type="button" class="eq" value="=" onclick="total()"></td>
</tr>
<tr>
<td colspan="2"><input type="button" value="0" style="width:115px;" onclick="numero('0')"></td>
<td><input type="button" value="." onclick="numero('.')"></td>
<td colspan="2"></td>
</tr>
</table>
</div>

<script>
var p = document.getElementById('pantalla');
var n1 = 0;
var sig = "";
var borrar = false;

function numero(n) {
if (p.value === "0" || p.value === "Error" || borrar) {
    p.value = n;
borrar = false;
} else {
if (n === "." && p.value.indexOf(".") !== -1) return;
p.value += n;
}
}

function constante(tipo) {
if (tipo === "pi") p.value = Math.PI;
if (tipo === "e") p.value = Math.E;
borrar = false;
}

function limpiar() {
    p.value = "0";
n1 = 0;
sig = "";
borrar = false;
}

function operar(op) {
    n1 = parseFloat(p.value);
sig = op;
borrar = true;
}

function cientifica(tipo) {
    var v = parseFloat(p.value);
if (isNaN(v)) return;
var r = 0;

if (tipo === "sin") r = Math.sin(v * Math.PI / 180);
if (tipo === "cos") r = Math.cos(v * Math.PI / 180);
if (tipo === "tan") r = Math.tan(v * Math.PI / 180);
if (tipo === "cuadrado") r = Math.pow(v, 2);
if (tipo === "inverso") r = 1 / v;

if (tipo === "signo") {
p.value = v * -1;
return;
}
if (tipo === "log") {
if (v <= 0) { p.value = "Error"; return; }
r = Math.log(v) / Math.LN10;
}
if (tipo === "ln") {
if (v <= 0) { p.value = "Error"; return; }
r = Math.log(v);
}
if (tipo === "raiz2") {
if (v < 0) { p.value = "Error"; return; }
r = Math.sqrt(v);
}
if (tipo === "raiz3") {
r = Math.cbrt(v);
}
if (tipo === "factorial") {
if (v < 0 || v % 1 !== 0) { p.value = "Error"; return; }
r = 1;
for (var i = 1; i <= v; i++) { r *= i; }
}

p.value = Number(r.toFixed(8));
borrar = true;
}

function total() {
if (sig === "") return;
var n2 = parseFloat(p.value);
var r = 0;
if (sig === "+") r = n1 + n2;
if (sig === "-") r = n1 - n2;
if (sig === "*") r = n1 * n2;
if (sig === "/") {
if (n2 === 0) { p.value = "Error"; return; }
r = n1 / n2;
}
if (sig === "potencia") r = Math.pow(n1, n2);

p.value = Number(r.toFixed(8));
sig = "";
borrar = true;
}
</script>

</body>
</html>
