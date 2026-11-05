from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BG=RGBColor(8,13,22); P=RGBColor(17,29,48); P2=RGBColor(24,42,66)
W=RGBColor(244,247,252); M=RGBColor(178,192,210); B=RGBColor(22,133,255)
C=RGBColor(63,187,233); G=RGBColor(70,205,145); Y=RGBColor(255,190,80)

def txt(s,x,y,w,h,t,sz=16,col=W,bold=False,align=PP_ALIGN.LEFT,font="Aptos"):
    sh=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    tf=sh.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=Inches(.05); tf.margin_right=Inches(.05); tf.margin_top=Inches(.03); tf.margin_bottom=Inches(.03)
    p=tf.paragraphs[0]; p.text=t; p.alignment=align
    p.font.name=font; p.font.size=Pt(sz); p.font.bold=bold; p.font.color.rgb=col
    return sh
def newslide(section,heading,sub="",n=1):
    s=prs.slides.add_slide(prs.slide_layouts[6]); s.background.fill.solid(); s.background.fill.fore_color.rgb=BG
    txt(s,.65,.3,11.8,.25,section.upper(),10,C,True)
    txt(s,.65,.72,12,.6,heading,28,W,True)
    if sub: txt(s,.68,1.38,11.8,.48,sub,13,M)
    txt(s,.68,7.12,8,.18,"FINANSYS • PROPOSTA DO PRODUTO",8,M,True)
    txt(s,12.1,7.08,.5,.2,f"{n:02d}",9,C,True,PP_ALIGN.RIGHT)
    return s
def card(s,x,y,w,h,head,body,accent=B,fs=14):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=P; sh.line.color.rgb=P2
    bar=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(x),Inches(y+.12),Inches(.055),Inches(h-.24))
    bar.fill.solid(); bar.fill.fore_color.rgb=accent; bar.line.fill.background()
    txt(s,x+.2,y+.16,w-.38,.35,head,16,W,True)
    txt(s,x+.2,y+.62,w-.38,h-.75,body,fs,M)
def bullets(s,x,y,w,h,items,fs=15):
    txt(s,x,y,w,h,"\n".join("•  "+i for i in items),fs,M)

# cover
s=prs.slides.add_slide(prs.slide_layouts[6]); s.background.fill.solid(); s.background.fill.fore_color.rgb=BG
txt(s,.85,.8,6,.3,"PROPOSTA DE PRODUTO • VISÃO GERAL",11,C,True)
txt(s,.82,1.55,8,1,"FinanSys",52,W,True)
txt(s,.9,2.65,8,1,"Gestão financeira inteligente\ne integrada.",25,M)
for x,w,t,col in [(.92,1.55,"PESSOAL",B),(2.62,1.85,"EMPRESARIAL",C),(4.62,2.0,"DESKTOP + MOBILE",G)]:
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(4.3),Inches(w),Inches(.4))
    sh.fill.solid(); sh.fill.fore_color.rgb=P2; sh.line.color.rgb=col
    txt(s,x+.03,4.36,w-.06,.22,t,10,W,True,PP_ALIGN.CENTER)
for i,h in enumerate([.8,1.25,1.7,2.25]):
    r=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(9+i*.68),Inches(4.8-h),Inches(.4),Inches(h))
    r.fill.solid(); r.fill.fore_color.rgb=[B,B,C,G][i]; r.line.fill.background()
txt(s,.92,6.55,9,.3,"Uma plataforma. Diferentes espaços financeiros. Dados centralizados.",13,M)

# slides data
slides=[
("01 • A PROPOSTA","O que é o FinanSys?","Uma plataforma para organizar, acompanhar e planejar finanças pessoais e empresariais.",
 [("Controle","Registrar receitas, despesas, transferências, contas e compromissos.",B),("Planejamento","Criar orçamentos, metas e limites para tomar decisões melhores.",C),("Visibilidade","Transformar movimentações em indicadores, relatórios e histórico confiável.",G)]),
("02 • PÚBLICO","Um sistema para dois contextos financeiros","A mesma plataforma atende necessidades diferentes sem misturar os dados.",
 [("Finanças pessoais","Contas e cartões pessoais\nReceitas e despesas domésticas\nOrçamentos e metas de economia",B),("Finanças empresariais","Fluxo de caixa\nContas a pagar e receber\nClientes, fornecedores e centros de custo",C)]),
("03 • ORGANIZAÇÃO","Espaços financeiros independentes","Cada espaço possui suas próprias contas, movimentações, membros e permissões.",
 [("João • Pessoal","Conta corrente\nCartão pessoal\nDespesas domésticas\nMeta de economia",B),("Empresa ABC","Conta empresarial\nFornecedores\nDespesas operacionais\nCentros de custo",C),("Acesso de João","João participa dos dois espaços, mas os registros e saldos permanecem separados.",G)]),
("04 • PESSOAS E ACESSOS","Cada pessoa vê e faz somente o que foi autorizado","O acesso será definido por funções e permissões, de acordo com a responsabilidade de cada usuário.",
 [("Proprietário","Controle completo",B),("Administrador","Usuários e configurações",C),("Gestor financeiro","Movimentações e relatórios",G),("Operador","Registros autorizados",Y),("Aprovador","Aprova ou rejeita operações",B),("Visualizador","Consulta sem alterar",C)]),
("05 • APROVAÇÕES","Mais controle sobre operações importantes","Exemplo de uma despesa que precisa da autorização de um responsável.",
 [("1 • Registrar","Um operador cadastra a despesa.",B),("2 • Notificar","O gestor recebe um aviso.",C),("3 • Decidir","O gestor aprova ou rejeita.",Y),("4 • Registrar","A decisão fica no histórico.",G)]),
("06 • ACESSO INTEGRADO","Computador e celular com as mesmas informações","As duas aplicações utilizam os serviços centrais do FinanSys.",
 [("FinanSys Desktop","Tarefas detalhadas, tabelas, relatórios e administração.",B),("FinanSys Mobile","Consultas rápidas, registros e notificações.",C),("Mesma experiência","Identidade visual e regras consistentes nos dois dispositivos.",G)]),
("07 • ARQUITETURA","Uma central conecta todas as partes","Desktop e Android conversam com o Backend; não acessam o banco diretamente.",
 [("Desktop","Aplicação JavaFX",B),("Android","Aplicativo Java",C),("Backend / API","Recebe solicitações, aplica regras e valida permissões.",B),("Banco de dados","Armazena as informações oficiais.",G)]),
("08 • IMPLANTAÇÃO","Instalação local ou na nuvem","A mesma solução poderá ser instalada em infraestruturas diferentes.",
 [("Nuvem","Backend remoto\nAcesso pela internet\nBanco centralizado\nAcesso de diferentes locais",B),("Infraestrutura local","Servidor próprio\nAcesso pela rede interna\nBanco administrado localmente",C)]),
("09 • FUNCIONALIDADES","Os principais módulos do FinanSys","As funções serão organizadas por áreas para facilitar o uso e a evolução.",
 [("Dashboard","Resumo financeiro",B),("Contas","Saldos e carteiras",C),("Movimentações","Receitas e despesas",G),("Cartões","Limites e faturas",Y),("Compromissos","Pagar e receber",B),("Orçamentos","Limites de gastos",C),("Metas","Objetivos financeiros",G),("Empresas","Clientes e fornecedores",Y),("Equipe","Usuários e permissões",B),("Aprovações","Autorizações",C),("Relatórios","Indicadores",G),("Auditoria","Histórico de ações",Y)]),
("10 • RECURSOS ADICIONAIS","Funcionalidades para uma evolução mais completa","Recursos que ampliam a utilidade do sistema e reduzem tarefas manuais.",
 [("Importar extratos","Ler arquivos OFX e CSV.",B),("Conciliação bancária","Comparar extratos e lançamentos.",C),("Recorrências","Programar lançamentos periódicos.",G),("Anexos","Guardar comprovantes e documentos.",Y),("Exportação","Gerar relatórios em PDF e Excel.",B),("Multimoeda","Registrar moedas e taxas utilizadas.",C)]),
("11 • CONFIABILIDADE","Precisão e histórico são fundamentais","O sistema precisa explicar os saldos e preservar o histórico das operações.",
 [("Valores corretos","Tratamento apropriado de valores monetários e arredondamento.",C),("Operações seguras","Transferências e lançamentos concluídos por inteiro ou desfeitos em caso de falha.",B),("Histórico auditável","Correções por estornos ou ajustes, sem apagar o passado.",G)]),
("12 • SEGURANÇA","Proteção em todas as camadas","Dados financeiros exigem controles técnicos e procedimentos operacionais.",
 [("Identidade","Autenticação e proteção de credenciais.",B),("Permissões","Acesso limitado ao espaço e à função.",C),("Comunicação","Conexões HTTPS em produção.",G),("Auditoria","Registro de ações importantes.",Y),("Backups","Cópias e testes de restauração.",B),("Privacidade","Tratamento responsável e atenção à LGPD.",C)]),
("13 • TECNOLOGIA","Ferramentas propostas","Tecnologias para construir uma plataforma Java consistente e sustentável.",
 [("Java 21 LTS","Linguagem principal",B),("Spring Boot","Serviços e API",C),("Spring Security","Autenticação e autorização",G),("PostgreSQL","Banco relacional",Y),("JavaFX","Aplicação Desktop",B),("Android + Java","Aplicativo móvel",C),("Flyway","Evolução do banco",G),("JUnit + Mockito","Testes automatizados",Y)]),
("14 • ORGANIZAÇÃO","Uma estrutura modular e fácil de manter","Cada módulo tem uma responsabilidade clara; o Backend concentra as regras e o acesso aos dados.",
 [("finansys-core","Contratos e componentes compartilhados.",C),("finansys-backend","Módulos financeiros, segurança e API.",B),("finansys-desktop","Interface para computadores.",G),("finansys-android","Aplicativo móvel.",Y),("database","Migrações e scripts do banco.",B),("docs","Documentação do projeto.",C)]),
("15 • DESENVOLVIMENTO","Construir por etapas, com validação contínua","A visão é completa, mas cada etapa precisa entregar uma base funcional e testada.",
 [("01 • Fundação","Arquitetura, banco, API e ambiente.",B),("02 • Acesso","Usuários, espaços e permissões.",C),("03 • Financeiro","Contas, movimentações e compromissos.",G),("04 • Aplicações","Desktop e Android integrados.",Y),("05 • Gestão","Aprovações, orçamento e metas.",B),("06 • Evolução","Relatórios, integrações e implantação.",G)]),
("16 • EVOLUÇÃO","Modo offline com responsabilidade","Acesso sem internet precisa respeitar a integridade dos dados financeiros.",
 [("Consultar","Informações recentes armazenadas localmente, com data da última atualização.",B),("Registrar temporariamente","Operações ficam pendentes e ainda não são confirmadas pelo servidor.",C),("Sincronizar e validar","Verificar duplicidades, permissões e conflitos antes de confirmar.",G)]),
]
for idx,(sec,head,sub,cards) in enumerate(slides, start=2):
    s=newslide(sec,head,sub,idx)
    if len(cards)==2:
        for j,(h,b,c) in enumerate(cards): card(s,.9+j*6.05,2.35,5.5,3.1,h,b,c,16)
    elif len(cards)==3:
        for j,(h,b,c) in enumerate(cards): card(s,.75+j*4.05,2.55,3.75,2.65,h,b,c,14)
    elif len(cards)==4:
        for j,(h,b,c) in enumerate(cards):
            x=.8+(j%2)*6.05; y=2.2+(j//2)*1.8
            card(s,x,y,5.55,1.45,h,b,c,13)
    else:
        cols=4 if len(cards)>=8 else 3
        for j,(h,b,c) in enumerate(cards):
            x=.65+(j%cols)*(12.05/cols); y=2.05+(j//cols)*1.27
            card(s,x,y,12.05/cols-.22,1.05,h,b,c,11 if len(cards)>=8 else 12)

# closing
s=newslide("FINANSYS • VISÃO DE FUTURO","Uma plataforma. Múltiplas possibilidades.","Gestão financeira pessoal e empresarial, com acesso integrado, controle de permissões e informações confiáveis.",len(prs.slides)+1)
card(s,.9,3.0,3.65,1.7,"Organizar","Centralizar contas e movimentações.",B,14)
card(s,4.85,3.0,3.65,1.7,"Controlar","Definir acessos e acompanhar operações.",C,14)
card(s,8.8,3.0,3.65,1.7,"Evoluir","Planejar, analisar e integrar novas funções.",G,14)
txt(s,.95,5.55,11.4,.4,"FinanSys — Gestão financeira inteligente e integrada.",17,W,True,PP_ALIGN.CENTER)

out="F:\documentos\slidesFinanSys_Apresentacao_Atualizada2.pptx"
prs.save(out)
print(out)
