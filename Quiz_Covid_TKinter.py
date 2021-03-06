import tkinter
from tkinter import *

root = Tk()
root.title('Quiz - Corona Vírus')
root.geometry("1450x1180")
image=tkinter.PhotoImage(file='covid01.png')
image=image.subsample(1,1)
labelimage=tkinter.Label(image=image)
labelimage.place(x=0, y=0, relwidth = 1.0, relheight = 1.0)
rotu_tit=Label(root, text='Super Quiz - Covid 19', font=('Berlin Sans FB Demi' , 70), bg = 'crimson' )
rotu_tit.place(x=230, y=90)
rotu_nome=Label(root, text='Nome:', font=('Berlin Sans FB Demi', 30), bg='crimson')
rotu_nome.place(x=340, y=250)
ent01=Entry(root, font=('Berlin Sans FB Demi', 30))
ent01.place(x=480, y = 250 )
count = 0
def comm1():
    nome=ent01.get()
    rotuq01=Label(root, text='Questão 01: Onde foi identificada pela primeira vez um caso de Covid-19?', font=('Berlin Sans FB Demi', 30), bg = 'crimson')
    rotuq01.place(x=20, y=80)
    botq1r1 = Button(root, text='a) Nova York, EUA.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg = 'dimgrey')
    botq1r1.place(x=200, y=300)
    botq1r2 = Button(root, text='b) Tóquio, Japão.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg = 'dimgrey')
    botq1r2.place(x=750, y=300)
    botq1r3 = Button(root, text='c) Roma, Itália.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg = 'dimgrey')
    botq1r3.place(x=200, y=450)
    def comm2():
        global  count
        count += 1
        rotuq02 = Label(root, text='Questão 02: Qual das alternativas abaixo é associada a uma produção de \nvitamina D pelo corpo humano?', font=('Berlin Sans FB Demi', 30), bg='crimson')
        rotuq02.place(x=10, y=80)
        botq2r1 = Button(root, text='a) Dormir tarde.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
        botq2r1.place(x=200, y=300)
        botq2r2 = Button(root, text='b) Diminuir a ingestão de açúcares.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
        botq2r2.place(x=550, y=300)
        botq2r4 = Button(root, text='d) Isolamento social.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
        botq2r4.place(x=800, y=450)
        def comm3():
            global count
            count += 1
            rotuq03 = Label(root, text='Questão 03: Segundo a mais recente atualização protocolar da Anvisa, \npessoas infectadas com a Covid-19, que forem assintomáticos ou \napresentarem sintomas leves. Devem praticar isolamento de quantos dias?', font=('Berlin Sans FB Demi', 30), bg='crimson')
            rotuq03.place(x=10, y=80)
            botq3r2 = Button(root, text='b) 15 dias de isolamento.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
            botq3r2.place(x=750, y=300)
            botq3r3 = Button(root, text='c) 20 dias de isolamento.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
            botq3r3.place(x=200, y=450)
            botq3r4 = Button(root, text='d) 25 dias de isolamento.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
            botq3r4.place(x=750, y=450)
            def comm4():
                global count
                count += 1
                rotuq04 = Label(root, text='Questão 04: Quais exames são usados para o diagnóstico do coronavírus?', font=('Berlin Sans FB Demi', 30), bg='crimson')
                rotuq04.place(x=20, y=80)
                botq4r1= Button(root, text='a) Teste de reflexos e PCR.', relief=FLAT, font=('Berlin Sans FB Demi', 30),bg='dimgrey')
                botq4r1.place(x=50, y=300)
                botq4r2 = Button(root, text='b) Contagem de plaquetas e hemácias.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                botq4r2.place(x=600, y=300)
                botq4r3 = Button(root, text='c) Teste de temperatura e reflexo.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                botq4r3.place(x=50, y=450)
                def comm5():
                    global count
                    count +=1
                    rotuq05 = Label(root, text='Questão 05: Qual foi a primeira vacina aprovada pela ANVISA?', font=('Berlin Sans FB Demi', 30), bg='crimson')
                    rotuq05.place(x=80, y=180)
                    botq5r1 = Button(root, text='a) CoronaVac.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                    botq5r1.place(x=200, y=300)
                    botq5r2 = Button(root, text='b) AstraZeneca.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                    botq5r2.place(x=700, y=300)
                    botq5r4 = Button(root, text='d) Janssen.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                    botq5r4.place(x=700, y=450)
                    def comm6():
                        global count
                        count += 1
                        rotuq06 = Label(root, text='Questão 06: Em qual período iniciou-se a vacinação contra \na covid-19 no Brasil?', font=('Berlin Sans FB Demi', 30), bg='crimson')
                        rotuq06.place(x=130, y=160)

                        botq6r2 = Button(root, text='b) Maio de 2020.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                        botq6r2.place(x=700, y=300)
                        botq6r3 = Button(root, text='c) Outubro de 2021.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey', command=comm6)
                        botq6r3.place(x=200, y=450)
                        botq6r4 = Button(root, text='d) Dezembro de 2019.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey')
                        botq6r4.place(x=700, y=450)
                        def comm7():
                            rotuq07 =Label(root, text= 'Parabéns!!! Você respondeu a todas as perguntas do Quiz \nE agora conhece muito mais sobre o assunto', font=('Berlin Sans FB Demi', 30), bg='crimson')
                            rotuq07.place(x=120, y=250)

                            rotuq06.destroy()
                            botq6r1.destroy()
                            botq6r2.destroy()
                            botq6r3.destroy()
                            botq6r4.destroy()
                        botq6r1 = Button(root, text='a) Janeiro de 2021.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey', command = comm7)
                        botq6r1.place(x=200, y=300)

                        rotuq05.destroy()
                        botq5r1.destroy()
                        botq5r2.destroy()
                        botq5r3.destroy()
                        botq5r4.destroy()
                    botq5r3 = Button(root, text='c) Pfizer.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey', command = comm6)
                    botq5r3.place(x=200, y=450)

                    rotuq04.destroy()
                    botq4r1.destroy()
                    botq4r2.destroy()
                    botq4r3.destroy()
                    botq4r4.destroy()
                botq4r4 = Button(root, text='d) PCR e testes sorológicos..', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey', command = comm5)
                botq4r4.place(x=750, y=450)

                rotuq03.destroy()
                botq3r1.destroy()
                botq3r2.destroy()
                botq3r3.destroy()
                botq3r4.destroy()
            botq3r1 = Button(root, text='a) 10 dias de isolamento.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey', command = comm4)
            botq3r1.place(x=200, y=300)

            rotuq02.destroy()
            botq2r1.destroy()
            botq2r2.destroy()
            botq2r3.destroy()
            botq2r4.destroy()
        botq2r3 = Button(root, text='c) Exposição a luz solar', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg='dimgrey', command = comm3)
        botq2r3.place(x=200, y=450)

        rotuq01.destroy()
        botq1r1.destroy()
        botq1r2.destroy()
        botq1r3.destroy()
        botq1r4.destroy()
    botq1r4 = Button(root, text='d) Wuhan, China.', relief=FLAT, font=('Berlin Sans FB Demi', 30), bg = 'dimgrey', command = comm2)
    botq1r4.place(x=750, y=450)

    rotu_tit.destroy()
    rotu_nome.destroy()
    ent01.destroy()
    bot01.destroy()
bot01 = Button(root, text= 'Iniciar', font = ('Berlin Sans FB Demi', 30), bg = 'dimgrey', command=comm1)
bot01.place(x=580, y=350)

root.mainloop()