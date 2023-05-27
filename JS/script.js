let heroName = prompt('Insira o nome do personagem:');
let heroPower = prompt(`Insira o poder de ataque do ${heroName}`);

let enemyName = prompt('Insira o nome do inimigo:');
let enemyHealth = prompt(`Insira a quantidade de pontos de vida do ${enemyName}:`);
let enemyDefense = prompt(`Insira o poder de defesa ${enemyDefense}`);
let enemyShield = confirm(`Aperte OK se ${enemyName} possuir um escudo`);

let damage;

if (heroPower > enemyDefense ) {
    if (enemyShield == false){
        damage = heroPower - enemyDefense;
    }
    else {
        damage = (heroPower - enemyDefense)/2;
    }
}
else {
    damage = 0;
}

enemyHealth -= damage;

alert(`${damage} de dano causado em ${enemyName}`);
alert(`A vida total de ${enemyName} é ${enemyHealth}`)