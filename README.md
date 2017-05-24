# TWELVE-MONKEYS
Experiências com Python / Python first learning experiments

O ano é 2029. O mundo foi devastado por uma infeccção ou vírus (os cientistas ainda não conseguiram descobrir com exatidão) que traz os mortos de volta a vida. Como se não bastasse o problema populacional, os mortos voltam com uma característica bastante peculiar: eles se alimentam de outros humanos normais ou mesmo zumbis. A civilização como a conhecíamos ruiu, e com ela, ruiram também os meios de produção de alimento. No meio do planeta devastado ainda existem humanos sobreviventes, divididos basicamente em duas castas: os frugívoros, que se alimentam basicamente de frutas e os semi-onívoros, que se alimentam de cereais e, se for necessário, de frutas.

O único resquício de civilização é uma célula da ONU, que funciona em um submarino movido à energia solar que agora está localizado em um ponto desconhecido do Pacífico. Eu, Cristiano Roberto Franco, fui atacado por zumbis enquanto fazia o commit de um código fonte. Meus dois braços tiveram que ser amputados, para evitar que a infeccção se espalhasse e com isso, fiquei impedido de programar. E é aqui que você entra. Sua missão, se você decidir aceitar, é implementar um programa que, dado um número de humanos (zumbis, frugivoros e semi-onívoros) e determinada quantia de frutas e cereais, demonstre um cenário para a raça humana em ambiente fechado. Eu não posso programar, mas seguem abaixo algumas instruções para você cumprir a missão:

Devem existir 3 tipos de humanos, conforme o enunciado acima;
Os 3 tipos de humanos iniciam com 5 de vida. A cada vez que um humano come, sua vida sobe um ponto. A cada vez que um humano é chamado para comer e não consegue pois a comida acabou, é retirado um ponto. Com 0 pontos o humano morre de inanição (inclusive zumbis);
Cada humano somente pode comer o que está descrito no enunciado (talvez exista alguma solução por polimorfismo). Um zumbi não pode comer a si mesmo;
Talvez fosse interessante criar uma classe MeioAmbiente ou algo assim que controlasse as chamadas dos métodos dos humanos;
O número de humanos, frutas e cerais deverá ser recebido como parâmetro no construtor da classe MeioAmbiente;
Dentre a quantidade de humanos, o programa deverá gerar aleatoriamente os zumbis, frugívoros e semi-onívoros, colocando-os em um vetor ou coleção;
Cada vez que um alimento é consumido, este deve ser retirado da coleção ou vetor respectivos;
Quando acaba um alimento, o humano que depende dele não consegue mais se alimentar;
A classe de meio ambiente deve basicamente criar as intancias dos objetos humanos e alimentos e, sequencialmente, mandá-los se alimentar;
Cada vez que um humano se alimenta, diminui sua vida, ou morre, uma mensagem indicativa deve ser mostrada no console;


