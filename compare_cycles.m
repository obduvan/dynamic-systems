fync=load('D:\DEVELOP PROJECTS\В рамках предмета в универе\dynamic-systems\compare_cycles\fync.txt');
x_9=load('D:\DEVELOP PROJECTS\В рамках предмета в универе\dynamic-systems\compare_cycles\x_9.txt');
x_9_1=load('D:\DEVELOP PROJECTS\В рамках предмета в универе\dynamic-systems\compare_cycles\x_9_1.txt');
x_4=load('D:\DEVELOP PROJECTS\В рамках предмета в универе\dynamic-systems\compare_cycles\x_4.txt');
x_eq=load('D:\DEVELOP PROJECTS\В рамках предмета в универе\dynamic-systems\compare_cycles\x_eq.txt');

hold on

plot(fync(:,1),fync(:,2),'.','Color',[76/255,102/255,0/255],'MarkerSize',3,'DisplayName','fync')

plot(x_9(:,1),x_9(:,2),'.','Color',"red",'MarkerSize',3,'DisplayName','9')
plot(x_9_1(:,1),x_9_1(:,2),'.','Color',"blue",'MarkerSize',3,'DisplayName','9_1')
plot(x_4(:,1),x_4(:,2),'.','Color',"green",'MarkerSize',3,'DisplayName','4')
plot(x_eq(:,1),x_eq(:,2),'.','Color',"black",'MarkerSize',3,'DisplayName','eq')

legend('show','Location','southeastoutside')