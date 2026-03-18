import streamlit as st

st.set_page_config(page_title="Quiz: Mulheres de Destaque na TI", page_icon="💻")

# Lista de perguntas
perguntas = [
    {
        "pergunta": "1) Quem é frequentemente reconhecida como a primeira programadora da história?",
        "opcoes": [
            "a) Grace Hopper",
            "b) Ada Lovelace",
            "c) Margaret Hamilton",
            "d) Radia Perlman"
        ],
        "resposta_correta": "b) Ada Lovelace"
    },
    {
        "pergunta": "2) Qual mulher teve grande destaque no desenvolvimento de compiladores e na popularização do COBOL?",
        "opcoes": [
            "a) Hedy Lamarr",
            "b) Carol Shaw",
            "c) Grace Hopper",
            "d) Susan Kare"
        ],
        "resposta_correta": "c) Grace Hopper"
    },
    {
        "pergunta": "3) Quem liderou a equipe de software do projeto Apollo 11, da NASA?",
        "opcoes": [
            "a) Margaret Hamilton",
            "b) Ada Lovelace",
            "c) Radia Perlman",
            "d) Jean Sammet"
        ],
        "resposta_correta": "a) Margaret Hamilton"
    },
    {
        "pergunta": "4) Qual cientista da computação ficou conhecida como a 'mãe da internet' por criar o protocolo Spanning Tree?",
        "opcoes": [
            "a) Carol Shaw",
            "b) Frances Allen",
            "c) Radia Perlman",
            "d) Grace Hopper"
        ],
        "resposta_correta": "c) Radia Perlman"
    },
    {
        "pergunta": "5) Quem foi uma das primeiras mulheres desenvolvedoras de jogos eletrônicos, com destaque na Atari?",
        "opcoes": [
            "a) Susan Kare",
            "b) Carol Shaw",
            "c) Hedy Lamarr",
            "d) Annie Easley"
        ],
        "resposta_correta": "b) Carol Shaw"
    }
]

# Inicialização do estado da sessão
if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0

if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

if "respostas_usuario" not in st.session_state:
    st.session_state.respostas_usuario = []

if "quiz_finalizado" not in st.session_state:
    st.session_state.quiz_finalizado = False


# Função para reiniciar o quiz
def reiniciar_quiz():
    st.session_state.indice_pergunta = 0
    st.session_state.pontuacao = 0
    st.session_state.respostas_usuario = []
    st.session_state.quiz_finalizado = False


st.title("💻 Quiz: Mulheres de Destaque na TI")

# Se o quiz ainda não terminou
if not st.session_state.quiz_finalizado:
    indice = st.session_state.indice_pergunta
    pergunta_atual = perguntas[indice]

    st.subheader(f"Pergunta {indice + 1} de {len(perguntas)}")
    st.write(pergunta_atual["pergunta"])

    resposta = st.radio(
        "Escolha uma alternativa:",
        pergunta_atual["opcoes"],
        key=f"resposta_{indice}"
    )

    if st.button("Próxima"):
        st.session_state.respostas_usuario.append(resposta)

        if resposta == pergunta_atual["resposta_correta"]:
            st.session_state.pontuacao += 1

        st.session_state.indice_pergunta += 1

        if st.session_state.indice_pergunta >= len(perguntas):
            st.session_state.quiz_finalizado = True

        st.rerun()

# Se o quiz terminou
else:
    st.success("Quiz finalizado!")
    st.subheader(
        f"Sua pontuação foi: {st.session_state.pontuacao} de {len(perguntas)}"
    )

    if st.session_state.pontuacao == 5:
        st.balloons()
        st.write("Excelente! Você acertou tudo! 🎉")
    elif st.session_state.pontuacao >= 3:
        st.write("Muito bom! Você conhece bem a história das mulheres na TI. 👏")
    else:
        st.write("Continue estudando, você pode aprender ainda mais! 🚀")

    st.write("### Gabarito")
    for i, item in enumerate(perguntas):
        st.write(f"**{item['pergunta']}**")
        st.write(f"Sua resposta: {st.session_state.respostas_usuario[i]}")
        st.write(f"Resposta correta: {item['resposta_correta']}")
        st.write("---")

    if st.button("Reiniciar Quiz"):
        reiniciar_quiz()
        st.rerun()
