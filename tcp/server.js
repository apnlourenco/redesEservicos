const net = require('net'); // importa a biblioteca 'net'
const server = net.createServer((socket) => { //cria um novo servidor socket
  console.log('Cliente conectado.'); // conecta o cliente

  socket.write('Bem Vindo!\n'); //imprime mensagem

  socket.on('data', (data) => {
    console.log('Recebido do cliente: ' + data.toString());
  }); // o servidor recebe dados do cliente e armazena os dados

  socket.on('end', () => {
    console.log('Cliente desconectado.'); // finaliza a conexão com cliente 
  });
});

server.listen(5500, () => { // mostra a disponiblidade do servidor para fazer novas conexões
  console.log('Aguardando conexão');
});
