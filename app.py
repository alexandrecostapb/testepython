import streamlit as st

st.set_page_config(page_title="Quiz: Mulheres de Destaque na TI", page_icon="💻")

st.title("💻 Quiz: Mulheres de Destaque na TI")
st.write("Responda às 5 perguntas e veja sua pontuação no final.")

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

with st.form("quiz_form"):
    respostas_usuario = []

    for i, item in enumerate(perguntas):
        resposta = st.radio(
            item["pergunta"],
            item["opcoes"],
            key=f"pergunta_{i}"
        )
        respostas_usuario.append(resposta)

    enviar = st.form_submit_button("Ver resultado")

if enviar:
    pontuacao = 0

    for i in range(len(perguntas)):
        if respostas_usuario[i] == perguntas[i]["resposta_correta"]:
            pontuacao += 1

    st.subheader(f"✅ Sua pontuação foi: {pontuacao} de {len(perguntas)}")

    if pontuacao == 5:
        st.success("Excelente! Você acertou todas as perguntas! 🎉")
    elif pontuacao >= 3:
        st.info("Muito bom! Você conhece bem a história das mulheres na TI. 👏")
    else:
        st.warning("Você pode aprender ainda mais sobre mulheres de destaque na TI! 🚀")

    st.write("### Gabarito")
    for item in perguntas:
        st.write(f"**{item['pergunta']}**")
        st.write(f"Resposta correta: {item['resposta_correta']}")
