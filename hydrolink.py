import os

# Função para exibir o nome do programa
def exibir_nome_programa():
    print('HydroLink\n')

# Função para exibir as opções do menu principal
def exibir_opcoes():
    print('1. Poluições dos Continentes', '2. Contribuições dos Continentes com meio ambiente', '3. Sobre', '4. Sair\n', sep='\n')

# Função para exibir a lista de continentes
def exibir_continentes():
    continentes = ['America do Sul', 'America do Norte', 'Africa', 'Europa', 'Asia', 'Oceania', 'Sair']
    for idx, continente in enumerate(continentes, 1):
        print(f'{idx}. {continente}')

# Função para exibir a lista de anos
def exibir_anos():
    anos = ['2021', '2022', '2023', '2024', 'futuro']
    for idx, ano in enumerate(anos, 1):
        print(f'{idx}. {ano}')

# Função para finalizar o aplicativo
def finalizar_app():
    exibir_subtitulo('Finalizar o app\n')

# Função para voltar ao menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

# Função para tratar opções inválidas
def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

# Função para exibir subtítulos formatados
def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    print()

# Função para exibir informações de poluição por ano e continente
def exibir_informacao_por_ano(ano, informacoes):
    if ano in informacoes:
        print(f'*{ano}*\n{informacoes[ano]}')
    else:
        opcao_invalida()

# Função para obter a escolha de um ano e exibir as informações correspondentes
def escolher_ano(informacoes):
    exibir_subtitulo('Escolha um ano')
    exibir_anos()
    try:
        opcao_escolhida = int(input('Escolha um ano: '))
        anos = ['2021', '2022', '2023', '2024', 'futuro']
        if 1 <= opcao_escolhida <= 5:
            exibir_informacao_por_ano(anos[opcao_escolhida - 1], informacoes)
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

# Função para tratar as opções de continentes para poluição
def continentes_poluicao():
    exibir_subtitulo('Escolha um continente')
    exibir_continentes()
    try:
        opcao_escolhida = int(input('Escolha um continente: '))
        informacoes = {
            1: {
                '2021': 'Em 2021, a poluição nos oceanos banhados pela América do Sul continuou a ser uma preocupação significativa, com a presença de plásticos, resíduos industriais e esgoto não tratado como principais contribuintes. As áreas costeiras próximas a grandes cidades, como Rio de Janeiro e Buenos Aires, foram as mais afetadas. Iniciativas de limpeza e campanhas de conscientização ambiental começaram a ganhar força. No entanto, a implementação de políticas ambientais foi desigual entre os países. Dados mostraram um aumento na quantidade de microplásticos nas águas costeiras.',
                '2022': 'Em 2022, a poluição oceânica na América do Sul viu um aumento na mobilização de ONGs e governos locais em resposta ao crescente problema dos resíduos plásticos. Estudos indicaram que a pesca excessiva e a poluição por petróleo também agravaram a situação em regiões como a Amazônia Azul e o Atlântico Sul. A pressão internacional levou a mais acordos regionais para combater a poluição marinha. Programas educativos começaram a ser implementados em escolas para sensibilizar as novas gerações sobre a importância de proteger os oceanos.',
                '2023': 'Em 2023, a situação dos oceanos banhados pela América do Sul enfrentou desafios contínuos com a poluição. O lixo plástico permaneceu uma ameaça crítica, especialmente com o aumento de resíduos decorrentes da pandemia de COVID-19, como máscaras e luvas descartáveis. Novas políticas de reciclagem e gestão de resíduos sólidos começaram a ser implementadas em algumas cidades costeiras. A tecnologia de drones e satélites foi cada vez mais utilizada para monitorar a poluição marinha. Houve também um aumento nas campanhas de limpeza de praias envolvendo voluntários locais.',
                '2024': 'Em 2024, a poluição dos oceanos continuou a ser um problema premente na América do Sul, com alguns avanços e muitos desafios. As cidades costeiras implementaram melhores sistemas de gestão de resíduos, mas a aplicação eficaz ainda variava. O uso de biotecnologia para degradar plásticos e a promoção de materiais biodegradáveis ganharam destaque. A cooperação internacional para proteger a biodiversidade marinha se intensificou. Programas de restauração de ecossistemas marinhos começaram a mostrar resultados positivos em algumas áreas.',
                'futuro': 'Para o futuro, espera-se que a poluição oceânica na América do Sul seja combatida por meio de políticas ambientais mais rigorosas e tecnologias inovadoras. A transição para uma economia circular, onde o desperdício é minimizado, será crucial. A conscientização e educação ambiental continuarão a ser fundamentais para mobilizar ações comunitárias. O aumento na pesquisa sobre os impactos da poluição e as soluções possíveis deverá informar políticas públicas mais eficazes. A colaboração internacional e os acordos regionais serão essenciais para enfrentar a poluição de forma holística e sustentável.'
            },
            2: {
                '2021': 'Em 2021, os oceanos da América do Norte, particularmente o Atlântico e o Pacífico, continuaram a enfrentar altos níveis de poluição por plásticos, esgoto e produtos químicos. Grandes cidades costeiras como Nova York e Los Angeles contribuíram significativamente para essa poluição. Iniciativas de limpeza de praias e campanhas de conscientização ambiental começaram a se intensificar. Estudos mostraram níveis alarmantes de microplásticos na vida marinha. A legislação ambiental variava entre os países, com o Canadá avançando em políticas mais rigorosas.',
                '2022': 'Em 2022, a poluição oceânica na América do Norte viu um aumento na conscientização pública e na ação governamental. Os resíduos plásticos continuaram a ser um problema crítico, com uma grande quantidade chegando aos oceanos devido ao manejo inadequado de resíduos. O uso de tecnologias de monitoramento, como drones, foi expandido para identificar e mitigar pontos críticos de poluição. Campanhas de reciclagem e redução de uso de plásticos de uso único ganharam impulso. Houve uma maior colaboração entre países para abordar a poluição transfronteiriça.',
                '2023': 'Em 2023, os esforços para combater a poluição oceânica na América do Norte mostraram sinais de progresso, mas os desafios persistiram. Programas de reciclagem foram ampliados e novas leis ambientais foram implementadas em vários estados dos EUA. O impacto dos resíduos médicos da pandemia ainda era visível nas águas costeiras. A parceria público-privada para a limpeza dos oceanos foi intensificada, com grandes empresas investindo em soluções sustentáveis. Projetos de restauração de habitats marinhos começaram a ser mais frequentes.',
                '2024': 'Em 2024, a poluição dos oceanos na América do Norte continuou a ser uma questão crítica, embora houvesse melhorias em certas áreas. O aumento no uso de materiais biodegradáveis e a aplicação de biotecnologia para a degradação de plásticos começaram a mostrar resultados positivos. A educação ambiental nas escolas foi reforçada, aumentando a conscientização entre os jovens. As tecnologias de monitoramento avançaram, permitindo uma melhor rastreabilidade da origem dos poluentes. Os acordos internacionais sobre a proteção dos oceanos foram ampliados, promovendo uma cooperação mais eficaz.',
                'futuro': 'Para o futuro, a poluição oceânica na América do Norte deverá ser combatida com políticas ambientais mais rigorosas e avanços tecnológicos. Espera-se um aumento significativo na reciclagem e na redução de plásticos de uso único. A economia circular será um pilar fundamental para minimizar o desperdício. A colaboração entre governos, ONGs e setor privado será essencial para implementar soluções eficazes. A educação e a conscientização ambiental continuarão a ser vitais para mobilizar a sociedade na proteção dos oceanos.'
            },
            3: {
                '2021': 'Em 2021, a poluição dos oceanos que banham a África foi uma preocupação crescente, com plásticos, resíduos industriais e poluentes químicos afetando as águas costeiras. Países como Nigéria, África do Sul e Egito enfrentaram desafios significativos devido à falta de infraestrutura de gestão de resíduos. Iniciativas de limpeza de praias e campanhas de conscientização foram lançadas em várias regiões. A presença de microplásticos na vida marinha levantou alarmes sobre os impactos ambientais e na saúde humana.',
                '2022': 'Em 2022, a poluição oceânica na África continuou a ser uma questão crítica, com esforços crescentes para enfrentar o problema. Programas de gestão de resíduos foram ampliados em muitos países africanos, embora a implementação fosse desigual. Tecnologias de monitoramento marinho foram introduzidas para rastrear fontes de poluição e avaliar seu impacto nos ecossistemas costeiros. A cooperação regional foi incentivada para abordar a poluição transfronteiriça.',
                '2023': 'Em 2023, os esforços para combater a poluição oceânica na África mostraram alguns progressos, mas os desafios persistiram. A implementação de políticas ambientais mais rigorosas resultou em uma redução gradual dos resíduos plásticos em algumas áreas costeiras. Projetos de reciclagem e gestão sustentável de resíduos foram fortalecidos com parcerias público-privadas. A conscientização ambiental foi aumentada através de programas educacionais e campanhas de sensibilização.',
                '2024': 'Em 2024, a poluição dos oceanos na África continuou a ser uma preocupação, apesar dos avanços em certas frentes. A promoção de práticas de consumo sustentável e a redução de plásticos de uso único ganharam destaque em políticas e campanhas públicas. Investimentos em infraestrutura de tratamento de resíduos e reciclagem foram priorizados em várias nações africanas. A pesquisa sobre os impactos da poluição marinha e as soluções inovadoras foram incentivadas para enfrentar os desafios emergentes.',
                'futuro': 'Para o futuro, espera-se que a poluição oceânica na África seja abordada com uma abordagem holística, envolvendo políticas ambientais robustas, investimentos em infraestrutura e educação ambiental. A cooperação regional e internacional será fundamental para enfrentar os desafios da poluição transfronteiriça. O desenvolvimento de tecnologias sustentáveis e a inovação em gestão de resíduos serão cruciais para mitigar os impactos da poluição nos ecossistemas marinhos. O envolvimento da comunidade e a conscientização pública serão essenciais para promover uma mudança de comportamento em direção a práticas mais sustentáveis.'
            },
            4: {
                '2021': 'Em 2021, os oceanos que banham a Europa, especialmente o Atlântico e o Mediterrâneo, enfrentaram sérios problemas de poluição por plásticos, produtos químicos e resíduos industriais. Países como Espanha, França e Itália registraram altos níveis de poluentes nas águas costeiras. A União Europeia intensificou suas políticas de redução de plásticos de uso único. Iniciativas de limpeza e campanhas de conscientização ganharam força. A presença de microplásticos na vida marinha e nos alimentos foi uma grande preocupação.',
                '2022': 'Em 2022, a poluição oceânica na Europa continuou a ser um problema crítico, com foco crescente na redução de resíduos plásticos. Programas de reciclagem foram ampliados e campanhas de sensibilização ambiental foram intensificadas. A poluição por resíduos farmacêuticos e químicos industriais recebeu maior atenção. A União Europeia introduziu novas regulamentações ambientais para proteger as águas costeiras. Projetos de monitoramento e limpeza do Mediterrâneo começaram a mostrar resultados positivos.',
                '2023': 'Em 2023, os esforços para combater a poluição oceânica na Europa apresentaram progressos notáveis, mas desafios persistiram. A implementação de políticas ambientais mais rígidas resultou em uma ligeira redução dos resíduos plásticos. Tecnologias inovadoras, como barreiras flutuantes para capturar plásticos, foram testadas em diversas regiões. A cooperação transfronteiriça entre países europeus foi intensificada para enfrentar a poluição marinha. Projetos de restauração de ecossistemas costeiros começaram a ser mais visíveis.',
                '2024': 'Em 2023, os esforços para combater a poluição oceânica na Europa apresentaram progressos notáveis, mas desafios persistiram. A implementação de políticas ambientais mais rígidas resultou em uma ligeira redução dos resíduos plásticos. Tecnologias inovadoras, como barreiras flutuantes para capturar plásticos, foram testadas em diversas regiões. A cooperação transfronteiriça entre países europeus foi intensificada para enfrentar a poluição marinha. Projetos de restauração de ecossistemas costeiros começaram a ser mais visíveis.',
                'futuro': 'Para o futuro, espera-se que a poluição dos oceanos na Europa seja abordada de forma mais eficaz através de uma combinação de políticas rigorosas, inovações tecnológicas e educação ambiental. A transição para uma economia circular será essencial para reduzir a geração de resíduos. A colaboração entre governos, indústrias e ONGs será crucial para implementar soluções sustentáveis. A pesquisa contínua sobre os impactos da poluição e as melhores práticas de mitigação informará políticas públicas mais eficazes. A proteção dos ecossistemas marinhos será uma prioridade contínua para garantir a saúde dos oceanos.'
            },
            5: {
                '2021': 'Em 2021, a poluição dos oceanos na Ásia, especialmente no Pacífico e no Índico, foi um grande problema, com plásticos e resíduos industriais como principais contaminantes. Países como China, Índia e Indonésia contribuíram significativamente para a poluição marinha. A falta de infraestrutura adequada de gestão de resíduos agravou a situação. Campanhas de limpeza de praias e iniciativas de reciclagem começaram a ganhar mais atenção. O impacto dos resíduos plásticos na vida marinha e nas economias costeiras foi amplamente documentado.',
                '2022': 'Em 2022, a poluição oceânica na Ásia continuou a ser crítica, com um aumento na conscientização pública e esforços governamentais. Programas de redução de plásticos e melhorias na gestão de resíduos começaram a ser implementados em várias cidades costeiras. As parcerias entre ONGs e governos locais se intensificaram para abordar o problema. Tecnologias de monitoramento marinho foram ampliadas para identificar fontes de poluição. O impacto da pandemia de COVID-19 ainda era visível com o aumento de resíduos médicos nos oceanos.',
                '2023': 'Em 2023, os esforços para mitigar a poluição dos oceanos na Ásia mostraram alguns progressos, embora os desafios continuassem. A adoção de políticas ambientais mais rigorosas em países como Japão e Coreia do Sul resultou em uma leve redução nos níveis de poluição. Iniciativas regionais para a limpeza de rios que deságuam nos oceanos começaram a mostrar resultados positivos. A educação ambiental foi intensificada, com programas focados na redução de plásticos. A colaboração internacional para proteger os ecossistemas marinhos foi fortalecida.',
                '2024': 'Em 2024, a poluição dos oceanos na Ásia continuou a ser uma questão urgente, com avanços em várias áreas. A implementação de tecnologias para a biodegradação de plásticos e a promoção de materiais alternativos começou a ter impacto. Melhores sistemas de gestão de resíduos foram implementados em cidades costeiras, resultando em uma redução de resíduos oceânicos. A cooperação entre países asiáticos foi intensificada para combater a poluição transfronteiriça. Projetos de restauração de habitats marinhos foram expandidos, mostrando benefícios ecológicos.',
                'futuro': 'Para o futuro, espera-se que a poluição oceânica na Ásia seja combatida com estratégias inovadoras e políticas ambientais mais eficazes. A transição para uma economia circular será crucial para reduzir a geração de resíduos. A conscientização pública e a educação ambiental continuarão a ser vitais para mobilizar ações locais e regionais. A pesquisa e o desenvolvimento de novas tecnologias para a limpeza e monitoramento dos oceanos serão essenciais. A colaboração internacional e os acordos regionais serão fundamentais para proteger e restaurar os ecossistemas marinhos asiáticos.'
            },
            6: {
                '2021': 'Em 2021, a poluição dos oceanos na Oceania, especialmente no Pacífico, foi dominada por plásticos e resíduos industriais. A Austrália e a Nova Zelândia enfrentaram desafios significativos com resíduos marinhos, impactando a biodiversidade costeira. Pequenas nações insulares do Pacífico também sofreram com a poluição devido à limitada infraestrutura de gestão de resíduos. Iniciativas de limpeza e campanhas de conscientização começaram a ganhar tração. Houve um foco crescente na redução de plásticos de uso único e no aprimoramento da reciclagem.',
                '2022': 'Em 2022, a poluição oceânica na Oceania viu um aumento na conscientização pública e em ações governamentais. A Austrália introduziu novas políticas de gestão de resíduos e programas de reciclagem. Pequenos estados insulares receberam apoio internacional para melhorar suas práticas de gestão de resíduos. Tecnologias de monitoramento marinho começaram a ser mais amplamente utilizadas para identificar e mitigar fontes de poluição. Campanhas educativas sobre a redução do uso de plásticos foram intensificadas.',
                '2023': 'Em 2023, os esforços para combater a poluição oceânica na Oceania mostraram progresso, mas desafios continuaram. A implementação de políticas ambientais mais rigorosas na Austrália e Nova Zelândia resultou em uma leve redução nos resíduos plásticos. Projetos regionais focados na limpeza de praias e na restauração de ecossistemas costeiros começaram a mostrar resultados positivos. A colaboração entre países da Oceania foi fortalecida para abordar a poluição transfronteiriça. A conscientização ambiental nas escolas foi ampliada, focando na proteção dos oceanos.',
                '2024': 'Em 2024, a poluição dos oceanos na Oceania continuou a ser monitorada de perto, com avanços em várias frentes. Tecnologias para a biodegradação de plásticos e a promoção de materiais alternativos começaram a ser implementadas. A gestão de resíduos em cidades costeiras foi aprimorada, resultando em uma redução nos resíduos oceânicos. Pequenas nações insulares receberam mais apoio para enfrentar os desafios da poluição marinha. Projetos de restauração de recifes de coral e habitats marinhos foram expandidos, mostrando benefícios ecológicos significativos.',
                'futuro': 'Para o futuro, espera-se que a poluição oceânica na Oceania seja combatida com políticas ambientais mais rigorosas e tecnologias inovadoras. A transição para uma economia circular será essencial para reduzir a geração de resíduos. A educação ambiental e a conscientização pública continuarão a ser vitais para mobilizar ações locais e regionais. A pesquisa e o desenvolvimento de novas tecnologias para a limpeza e monitoramento dos oceanos serão cruciais. A cooperação internacional e os acordos regionais serão fundamentais para proteger e restaurar os ecossistemas marinhos da Oceania.'
            }
        }

        if opcao_escolhida in informacoes:
            escolher_ano(informacoes[opcao_escolhida])
        elif opcao_escolhida == 7:
            voltar_ao_menu_principal()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    voltar_ao_menu_principal()

# Função para tratar as opções de continentes para ajuda ambiental
def continentes_ajuda():
    exibir_subtitulo('Escolha um continente')
    exibir_continentes()
    try:
        opcao_escolhida = int(input('Escolha um continente: '))
        informacoes = {
            1: {
                '2021': 'Em 2021, a ajuda internacional para combater a poluição dos oceanos na América do Sul incluiu apoio técnico e financeiro de organizações como o Banco Mundial e a ONU. Projetos de limpeza costeira foram realizados com a participação de voluntários e ONGs locais. Iniciativas de reciclagem e programas de redução de plásticos de uso único foram promovidos em várias cidades costeiras. A cooperação regional foi incentivada através de acordos como o Tratado de Cooperação Amazônica. Estudos sobre os impactos da poluição marinha nos ecossistemas e na economia local receberam financiamento.',
                '2022': 'Em 2022, a ajuda internacional aumentou com a implementação de programas de gestão de resíduos sólidos financiados por entidades globais, como a União Europeia. A pesquisa e o monitoramento marinho foram ampliados com o apoio de universidades e instituições científicas internacionais. Programas de capacitação e treinamento em gestão de resíduos e proteção costeira foram oferecidos a comunidades locais. Parcerias público-privadas foram estabelecidas para desenvolver infraestrutura de tratamento de resíduos. Campanhas de conscientização sobre a poluição marinha foram intensificadas através de mídias sociais e workshops.',
                '2023': 'Em 2023, a colaboração internacional incluiu novos acordos bilaterais e multilaterais para combater a poluição dos oceanos na América do Sul. Organizações como Greenpeace e WWF aumentaram seu envolvimento em projetos de conservação marinha. Tecnologias limpas, como sistemas de coleta e reciclagem de resíduos mais eficientes, foram introduzidas. O financiamento de projetos de restauração de habitats marinhos foi ampliado através de doações internacionais. Programas de intercâmbio de conhecimento permitiram a transferência de melhores práticas ambientais entre países sul-americanos e parceiros globais.',
                '2024': 'Em 2024, a ajuda internacional focou em soluções inovadoras e sustentáveis para a poluição oceânica na América do Sul. Novas tecnologias de biodegradação de plásticos e materiais alternativos começaram a ser implementadas. Programas de educação ambiental nas escolas foram ampliados com o apoio de ONGs internacionais e agências de desenvolvimento. Investimentos em infraestrutura de saneamento básico e tratamento de águas residuais foram priorizados em áreas costeiras. A cooperação regional foi reforçada através de conferências e fóruns sobre sustentabilidade marinha.',
                'futuro': 'Para o futuro, espera-se que a ajuda internacional continue a evoluir para combater a poluição dos oceanos na América do Sul. A implementação de políticas ambientais mais rigorosas e práticas de economia circular será fundamental. Inovações tecnológicas, incluindo novos materiais e métodos de reciclagem, serão essenciais para reduzir os resíduos marinhos. A educação contínua e a conscientização pública sobre a proteção dos oceanos serão vitais. A colaboração entre governos, ONGs e o setor privado será crucial para alcançar soluções duradouras e sustentáveis.'
            },
            2: {
                '2021': 'Em 2021, a ajuda internacional para combater a poluição dos oceanos na América do Norte envolveu esforços conjuntos de governos, ONGs e entidades globais como a ONU. Os Estados Unidos e o Canadá implementaram programas de reciclagem e redução de plásticos de uso único. Organizações como a Ocean Conservancy lideraram iniciativas de limpeza costeira e campanhas de conscientização. Parcerias público-privadas foram estabelecidas para desenvolver tecnologias de monitoramento e mitigação da poluição marinha. Projetos de pesquisa sobre os impactos dos microplásticos na vida marinha foram financiados.',
                '2022': 'Em 2022, a cooperação internacional foi intensificada com o apoio de entidades como a União Europeia e o Banco Mundial. Programas de gestão sustentável de resíduos foram ampliados nas principais cidades costeiras. Tecnologias avançadas de tratamento de resíduos e monitoramento de poluentes foram implementadas com apoio financeiro internacional. A educação ambiental foi promovida através de campanhas nas escolas e mídias sociais. Iniciativas de restauração de habitats marinhos e proteção de ecossistemas costeiros começaram a mostrar resultados positivos.',
                '2023': 'Em 2023, os esforços internacionais para combater a poluição dos oceanos na América do Norte incluíram novos acordos bilaterais e multilaterais. Organizações ambientais como a WWF e a Greenpeace intensificaram suas ações de conservação marinha. Tecnologias inovadoras, como sistemas de coleta de plásticos em rios antes que cheguem ao oceano, foram testadas e implementadas. Projetos de reciclagem e redução de resíduos plásticos foram ampliados com parcerias internacionais. Programas de capacitação para comunidades costeiras foram realizados para melhorar as práticas de gestão de resíduos.',
                '2024': 'Em 2024, a ajuda internacional focou em soluções sustentáveis e de longo prazo para a poluição marinha na América do Norte. Novas tecnologias de biodegradação de plásticos e materiais alternativos foram amplamente adotadas. Investimentos em infraestrutura de saneamento e tratamento de águas residuais foram priorizados, especialmente em áreas urbanas costeiras. A cooperação regional foi fortalecida através de conferências sobre sustentabilidade e proteção marinha. Programas de educação ambiental foram expandidos para aumentar a conscientização pública sobre a importância da preservação dos oceanos.',
                'futuro': 'Para o futuro, espera-se que a ajuda internacional continue a ser crucial na luta contra a poluição dos oceanos na América do Norte. A implementação de políticas ambientais rigorosas e a transição para uma economia circular serão fundamentais. Inovações tecnológicas em gestão de resíduos e monitoramento ambiental serão essenciais para reduzir a poluição marinha. A educação e a conscientização pública permanecerão vitais para promover práticas sustentáveis. A colaboração entre governos, ONGs e o setor privado será crucial para alcançar soluções eficazes e duradouras.'
            },
            3: {
                '2021': 'Em 2021, a ajuda internacional contra a poluição dos oceanos na África incluiu apoio financeiro e técnico de ONGs e agências da ONU, como o Programa das Nações Unidas para o Meio Ambiente (PNUMA). Projetos de limpeza costeira foram realizados em várias regiões, com a participação de voluntários locais. Iniciativas de reciclagem e educação ambiental foram implementadas em parceria com governos africanos. A colaboração entre países africanos para combater a poluição marinha foi incentivada através de programas regionais. Estudos sobre os impactos da poluição plástica nos ecossistemas marinhos africanos foram financiados.',
                '2022': 'Em 2022, a ajuda internacional aumentou com a implementação de programas de gestão sustentável de resíduos financiados pela União Europeia e outras entidades globais. Iniciativas de pesquisa e monitoramento marinho foram ampliadas com o apoio de universidades e instituições científicas. Programas de treinamento e capacitação para a gestão de resíduos e proteção costeira foram oferecidos a comunidades locais. Parcerias público-privadas foram estabelecidas para desenvolver infraestrutura de tratamento de resíduos. A conscientização sobre os efeitos da poluição marinha foi promovida através de campanhas de mídia social e workshops educacionais.',
                '2023': 'Em 2023, a colaboração internacional para combater a poluição dos oceanos na África incluiu novos acordos bilaterais e multilaterais. Organizações como a Ocean Conservancy e a WWF aumentaram seu envolvimento em projetos de conservação marinha. Iniciativas de tecnologia limpa foram introduzidas, como sistemas avançados de coleta e reciclagem de resíduos. O financiamento de projetos de restauração de habitats marinhos foi ampliado por meio de doações internacionais. Programas de intercâmbio de conhecimento permitiram a transferência de melhores práticas de gestão ambiental entre países africanos e parceiros globais.',
                '2024': 'Em 2024, a ajuda internacional focou em soluções inovadoras e sustentáveis para a poluição oceânica na África. Novas tecnologias de biodegradação de plásticos e materiais alternativos foram testadas e implementadas com sucesso. Programas de educação ambiental nas escolas foram ampliados, com o apoio de ONGs internacionais e agências de desenvolvimento. Investimentos em infraestrutura de saneamento básico e tratamento de águas residuais foram priorizados. A cooperação regional foi fortalecida através de conferências e fóruns sobre sustentabilidade marinha.',
                'futuro': 'Para o futuro, espera-se que a ajuda internacional continue a evoluir para combater a poluição dos oceanos na África. A implementação de políticas ambientais robustas e práticas de economia circular será fundamental. A inovação tecnológica, incluindo a criação de novos materiais e métodos de reciclagem, será crucial para reduzir os resíduos marinhos. A educação contínua e a conscientização pública sobre a proteção dos oceanos serão essenciais. A colaboração entre governos, ONGs e o setor privado será vital para alcançar soluções duradouras e sustentáveis.'
            },
            4: {
                '2021': 'Em 2021, a União Europeia intensificou suas políticas ambientais para combater a poluição dos oceanos, focando na redução de plásticos de uso único. Projetos financiados pela UE, como o programa Horizonte 2020, promoveram pesquisas sobre tecnologias de limpeza marinha. Organizações como a Ocean Cleanup realizaram operações de limpeza no Mediterrâneo e no Atlântico. Países como França, Espanha e Itália colaboraram em iniciativas regionais para monitorar e reduzir poluentes marinhos. Campanhas de conscientização pública foram lançadas para educar sobre a importância da reciclagem e da redução de resíduos.',
                '2022': 'Em 2022, a cooperação internacional para combater a poluição oceânica na Europa foi fortalecida através de parcerias com ONGs e entidades globais como a ONU. Programas de gestão sustentável de resíduos foram expandidos nas cidades costeiras europeias. Tecnologias de monitoramento e tratamento de resíduos marinhos receberam investimentos significativos. A UE introduziu novas regulamentações para limitar a produção e uso de plásticos de uso único. Projetos de restauração de ecossistemas marinhos, como recifes artificiais, começaram a mostrar resultados positivos.',
                '2023': 'Em 2023, os esforços internacionais para combater a poluição dos oceanos na Europa incluíram novos acordos bilaterais e multilaterais. Organizações como a Greenpeace e a WWF intensificaram suas ações de conservação marinha. Tecnologias inovadoras de coleta de plásticos e reciclagem foram testadas e implementadas em várias regiões costeiras. A educação ambiental foi promovida através de programas escolares e campanhas de mídia social. A colaboração entre países europeus foi fortalecida para abordar a poluição transfronteiriça de maneira mais eficaz.',
                '2024': 'Em 2024, a ajuda internacional focou em soluções sustentáveis e de longo prazo para a poluição marinha na Europa. Novas tecnologias de biodegradação de plásticos e materiais alternativos foram amplamente adotadas. Investimentos em infraestrutura de saneamento e tratamento de águas residuais foram priorizados, especialmente em áreas urbanas costeiras. A cooperação regional foi intensificada através de conferências e fóruns sobre sustentabilidade marinha. Programas de educação ambiental foram expandidos para aumentar a conscientização pública sobre a importância da preservação dos oceanos.',
                'futuro': 'Para o futuro, espera-se que a ajuda internacional continue a ser crucial na luta contra a poluição dos oceanos na Europa. A implementação de políticas ambientais rigorosas e a transição para uma economia circular serão fundamentais. Inovações tecnológicas em gestão de resíduos e monitoramento ambiental serão essenciais para reduzir a poluição marinha. A educação e a conscientização pública permanecerão vitais para promover práticas sustentáveis. A colaboração entre governos, ONGs e o setor privado será crucial para alcançar soluções eficazes e duradouras.'
            },
            5: {
                '2021': 'Em 2021, a ajuda contra a poluição dos oceanos na Ásia incluiu iniciativas de organizações internacionais como a ONU e o Banco Mundial, que financiaram projetos de gestão de resíduos e redução de plásticos. Países como Japão, China e Índia implementaram programas nacionais de reciclagem e limpeza costeira. ONGs como a Ocean Conservancy lideraram campanhas de conscientização e limpeza. A cooperação regional foi fortalecida através de acordos no âmbito da ASEAN. Programas de educação ambiental foram lançados para aumentar a conscientização pública sobre a poluição marinha.',
                '2022': 'No ano de 2022, a ajuda internacional aumentou com a implementação de tecnologias avançadas de gestão de resíduos e tratamento de efluentes, financiadas por entidades globais. Iniciativas de pesquisa sobre os impactos dos microplásticos e poluentes químicos nos ecossistemas marinhos foram ampliadas. Parcerias público-privadas promoveram o desenvolvimento de infraestrutura sustentável em áreas costeiras. Programas de capacitação e treinamento em gestão de resíduos foram oferecidos a comunidades locais. Campanhas de mídia social e workshops educacionais intensificaram a conscientização sobre a poluição oceânica.',
                '2023': 'Em 2023, novos acordos bilaterais e multilaterais foram firmados para combater a poluição marinha na Ásia. Organizações ambientais como a WWF e a Greenpeace aumentaram suas atividades de conservação e limpeza de praias. Tecnologias de coleta e reciclagem de plásticos foram introduzidas em cidades costeiras, com apoio internacional. Projetos de restauração de habitats marinhos, como manguezais e recifes de coral, receberam financiamento adicional. A colaboração entre países asiáticos e parceiros globais permitiu a troca de melhores práticas ambientais.',
                '2024': 'Em 2024, a ajuda internacional focou em soluções inovadoras e sustentáveis, como a implementação de bioplásticos e alternativas ecológicas. A pesquisa e o desenvolvimento de tecnologias de biodegradação de plásticos foram expandidos com financiamento global. Programas de educação ambiental nas escolas foram intensificados, com o apoio de ONGs e agências de desenvolvimento. Investimentos em infraestrutura de saneamento básico e tratamento de águas residuais foram priorizados. Conferências regionais e globais sobre sustentabilidade marinha reforçaram a cooperação internacional.',
                'futuro': 'Para o futuro, espera-se que a ajuda contra a poluição dos oceanos na Ásia se concentre na transição para uma economia circular, eliminando resíduos e promovendo a reutilização de materiais. A inovação tecnológica, incluindo novos métodos de monitoramento e limpeza marinha, será crucial. A cooperação entre governos, ONGs e o setor privado continuará a ser vital. A educação ambiental será ampliada, aumentando a conscientização pública e promovendo práticas sustentáveis. Políticas ambientais mais rigorosas e acordos internacionais fortalecerão os esforços para proteger os oceanos asiáticos.'
            }
            
        }

        if opcao_escolhida in informacoes:
            escolher_ano(informacoes[opcao_escolhida])
        elif opcao_escolhida == 7:
            voltar_ao_menu_principal()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    voltar_ao_menu_principal()

# Função para tratar a escolha de opção no menu principal
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            continentes_poluicao()
        elif opcao_escolhida == 2:
            continentes_ajuda()
        elif opcao_escolhida == 3:
            exibir_subtitulo('Sobre')
            print('Este programa foi desenvolvido para informar sobre a poluição e as contribuições ambientais dos continentes.')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

# Função principal para iniciar o programa
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
