const net = require('net'); // importa a biblioteca do Node.js

const client = net.createConnection({ porta: 5500 }, () => { // cria uma instância do servidor (cria um servidor novo)
  console.log('Conectado ao servidor.'); // mostra que alguem se conectou na porta 5500 com sucesso.
  client.write('!\n');
});

client.on('data', (data) => {
  console.log('Recebido do servidor: ' + data.toString());
  client.end();
}); // manipula os dados do cliente, recebe dados do servidor e exibi dados dos clientes

client.on('end', () => {
  console.log('Desconectado do servidor.'); // desconecta o cliente encerrando a conexão com servidor 
});

