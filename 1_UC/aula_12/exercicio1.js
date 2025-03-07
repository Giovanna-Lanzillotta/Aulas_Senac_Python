/*Crie uma classe pessoa com os atributos: nome, cpf, data de nascimento e,com um método calcular salario
crie uma classe funcionário com os atributos: salario bruto, salario liquido,dias de trabalho
crie uma classe professor com os atributos: salário liquido, horas de trabalho, valor hora/aula
faça com que as classes professor e funcionario herdem de pessoa*/

class Pessoa {
    constructor(nome, cpf, dataNascimento) {
        this.nome = nome;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
    }
    calcularSalario() { }
}
class Funcionario extends Pessoa {
    constructor(nome, cpf, dataNascimento, salarioBruto, salarioLiquido, diasTrabalho) {
        super(nome, cpf, dataNascimento)
        this.salarioBruto = salarioBruto;
        this.salarioLiquido = salarioLiquido;
        this.diasTrabalho = diasTrabalho;
    }
    //calcularSalario() {
    //console.log("Salário Funcionário:" + ((this.salarioBruto / 30) * this.diasTrabalho).toFixed(2))
    // } 
    calcularSalario(salarioBruto, diasTrabalho) {
        if (this.salarioBruto < 1400) {
            console.log("salário não encontrado!")
        } else {
            let valordiasTrabalho = this.salarioBruto / 30
            let diasTrabalho = this.diasTrabalho
            console.log("Valor dias trabalho: " + valordiasTrabalho)
            console.log("Dias trabalho: " + diasTrabalho)
            let salarioLiquido = valordiasTrabalho * diasTrabalho
            console.log("Salário calculado: " + salarioLiquido)
            return salarioLiquido;
        }
    }
}

class Professor extends Pessoa {
    constructor(nome, cpf, dataNascimento, salarioLiquido, horasTrabalho, valorHoraAula) {
        super(nome, cpf, dataNascimento)
        this.salarioLiquido = salarioLiquido;
        this.horasTrabalho = horasTrabalho;
        this.valorHoraAula = valorHoraAula;
    }
   //calcularSalario() {
   // console.log("Salário Professor:" + this.horasTrabalho * this.valorHoraAula)
   //} 
calcularSalario(horasTrabalho,valorHoraAula){
        if (this.salarioLiquido < 1400) {
            console.log("salário não encontrado!")
        } else {
            let salarioHora = this.horasTrabalho * this.valorHoraAula
            console.log("As horas trabalhadas são "+this.horasTrabalho)
            console.log("O valor da hora é "+this.valorHoraAula)
            console.log("Total do professor é "+salarioHora)
        }
    }
}

var pessoa1 = new Pessoa("Fulano", "123.456.788-76", "12/12/88")
console.log(pessoa1)
var funcionario1 = new Funcionario("Sicrano", "123.444.567-81", "23/12/93", 1500, 1000, 25)
console.log(funcionario1)
var professor1 = new Professor("Beltrano", "776.655.439-87", "01/02/78", 1450, 8, 250)
console.log(professor1)
funcionario1.calcularSalario()
professor1.calcularSalario()

/*exemplo da professora 
calcularSalario(salarioBruto,diasTrabalho){
    if (this.salarioBruto < 1400 ){
        console.log("salario não encontrado")
    }else{
        let valordiasTrabalho = this.salarioBruto/30
        console.log(valordiasTrabalho)
        console.log(diasTrabalho)
        let salarioLiquido = valordiasTrabalho * diasTrabalho
        return salarioLiquido;
    } 
}  */