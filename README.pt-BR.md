# auto-subtitle-renamer
[![Doe](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?hosted_button_id=86XUMMWCBSTZY)  
**Um pequeno projeto que renomeia os seus arquivos de legenda para corresponder aos seus arquivos de video.**  
Então, se você tiver um video 'hello world s01e42.mkv' e um legenda 'hello world sub s01e42-webrip.srt' na sua pasta, o programa irá renomear a legenda 'hello world sub s01e42-webrip.srt' para 'hello world s01e42.srt'.  
Baixe: [Aqui](https://github.com/matheusbucater/auto-subtitle-renamer/releases)  
  
**Se você quiser apoiar esse projeto, sinta-se avontade para doar usando o botão no topo ou com o QR Code abaixo**  
  
![alt text](https://github.com/matheusbucater/auto-subtitle-renamer/blob/master/resources/QR%20Code.png)

  
**IMPORTANTE! LEIA**  
Para que o programa funcione, seus arquivos de video e legenda **precisam** estar em uma pasta individual e **devem** estar ordenados por temporada/episódio.  
Se você estiver usando a [v2.1](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/V2.1) UI, *tome cuidado com a pasta de testes escolhida*, pois *o programa irá excluir todos os arquivos dentro da pasta*.  
Se você estiver usando a [v2.0](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/v2.0) (não recomendo você usar), tome cuidado pois o programa *NÃO* valida o diretório escolhido. Eu estava tendo muita dificuldade usando o askDirectory do tkinter, então eu mudei para o gooey [v2.1](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/V2.1).  
Se você estiver usando o aquivo .exe sem Inteface de Usuário, você tem que colocar o arquivo dentro da sua pasta contendo seus videos/legendas para depois executa-lo.    
No commit 'asr no ui with tests' [v1.1](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/v1.1) eu adicionei testes automatizados que vão criar uma pasta 'tests' dentro do diretório que estiver sendo executado.  
Todas as pastas de teste geradas em quaisquer umas das versões podem ser deletadas depois do programa ser executado.  
