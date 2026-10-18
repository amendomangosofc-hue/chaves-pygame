import random
import string
import pygame
import sys

__version__ = "1.0.0"

def gerar_chave(tamanho=10):
    return ''.join(random.choices(string.digits, k=tamanho))

chaves = []

pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w or 720, info.current_h or 1280
tela = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

font_g = pygame.font.SysFont("Arial", 32, bold=True)
font_m = pygame.font.SysFont("Arial", 26, bold=True)
font_p = pygame.font.SysFont("Arial", 22)

AZUL = (0, 150, 255)
VERDE = (0, 210, 110)
VERMELHO = (255, 70, 70)
CINZA = (45, 45, 58)
CINZA2 = (30, 30, 40)
BRANCO = (255, 255, 255)

btn_criar = pygame.Rect(20, 20, WIDTH // 2 - 30, 85)
btn_criar_varias = pygame.Rect(WIDTH // 2 + 10, 20, WIDTH // 2 - 30, 85)
btn_deletar = pygame.Rect(20, 120, WIDTH - 40, 75)

mensagem = "Toque em + para criar!"
scroll = 0
input_ativo = False
qtd_texto = "5"

def desenhar_botao(rect, cor, texto):
    pygame.draw.rect(tela, cor, rect, border_radius=18)
    txt = font_m.render(texto, True, (0, 0, 0) if cor != CINZA else BRANCO)
    tela.blit(txt, (rect.x + rect.width // 2 - txt.get_width() // 2,
                    rect.y + rect.height // 2 - txt.get_height() // 2))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = e.pos
            if btn_criar.collidepoint(mx, my):
                nova = gerar_chave(10)
                chaves.append(nova)
                mensagem = f"Criada: {nova}"
            elif btn_criar_varias.collidepoint(mx, my):
                input_ativo = not input_ativo
                mensagem = "Digite a qtd e aperte ENTER"
            elif btn_deletar.collidepoint(mx, my):
                if chaves:
                    removida = chaves.pop()
                    mensagem = f"Deletada: {removida}"
                else:
                    mensagem = "Nenhuma chave!"
            elif my > 260:
                idx = (my - 270 + scroll) // 68
                if 0 <= idx < len(chaves):
                    removida = chaves.pop(idx)
                    mensagem = f"Deletada: {removida}"

        if e.type == pygame.KEYDOWN and input_ativo:
            if e.key == pygame.K_RETURN:
                try:
                    qtd = int(qtd_texto)
                    if not 1 <= qtd <= 1000:
                        raise ValueError
                    for _ in range(qtd):
                        chaves.append(gerar_chave(10))
                    mensagem = f"{qtd} chaves criadas!"
                    input_ativo = False
                    qtd_texto = "5"
                except ValueError:
                    mensagem = "Digite um número de 1 a 1000!"
            elif e.key == pygame.K_BACKSPACE:
                qtd_texto = qtd_texto[:-1]
            elif e.unicode.isdigit() and len(qtd_texto) < 4:
                qtd_texto += e.unicode

        if e.type == pygame.MOUSEWHEEL:
            scroll = max(0, scroll - e.y * 35)

    tela.fill((15, 15, 22))

    desenhar_botao(btn_criar, VERDE, "+ 1 Chave")
    desenhar_botao(btn_criar_varias, AZUL, f"+ {qtd_texto} Chaves")
    desenhar_botao(btn_deletar, VERMELHO, "Deletar Última")

    tela.blit(font_p.render(mensagem, True, BRANCO), (20, 210))

    if input_ativo:
        pygame.draw.rect(tela, BRANCO, (20, 210, WIDTH - 40, 50), border_radius=12)
        tela.blit(font_g.render(f"Qtd: {qtd_texto} | ENTER", True, (0, 0, 0)), (30, 218))

    y = 270 - scroll
    for i, c in enumerate(chaves):
        if 230 < y < HEIGHT - 60:
            pygame.draw.rect(tela, CINZA, (20, y, WIDTH - 40, 60), border_radius=15)
            tela.blit(font_g.render(c, True, BRANCO), (30, y + 8))
            tela.blit(font_p.render(f"#{i} - toque pra apagar", True, (170, 170, 170)), (30, y + 35))
        y += 68

    if not chaves:
        tela.blit(font_m.render("Nenhuma chave ainda.", True, (100, 100, 110)), (20, 300))
        tela.blit(font_p.render("Toque em +1 Chave", True, (100, 100, 110)), (20, 340))

    pygame.draw.rect(tela, CINZA2, (0, HEIGHT - 55, WIDTH, 55))
    tela.blit(font_p.render(f"Total: {len(chaves)} chaves", True, (200, 200, 200)), (20, HEIGHT - 35))

    pygame.display.flip()
    clock.tick(30)
