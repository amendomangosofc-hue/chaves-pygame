# Chaves Pygame para Android

Este projeto tenta empacotar o programa original Pygame como APK usando GitHub Actions.

## Como usar pelo celular

1. Crie um repositório no GitHub, por exemplo `chaves-pygame`.
2. Envie todos os arquivos e pastas deste projeto para a raiz do repositório, mantendo `.github/workflows/build.yml`.
3. Abra a aba **Actions** do repositório.
4. Escolha **Compilar APK Pygame** e toque em **Run workflow** (ou envie um commit para `main`).
5. Abra a execução concluída e baixe o artefato `chaves-pygame-apk`. Se a compilação falhar, abra os logs da etapa que falhou.

## Observação importante

A compilação Pygame no Android depende de uma receita compatível do python-for-android. O projeto usa o bootstrap SDL2 com `requirements = python3,pygame`; a disponibilidade e compatibilidade da receita Pygame podem variar. Se o workflow falhar nessa etapa, será necessário usar uma receita/fork compatível ou migrar a interface para Kivy. Não é possível garantir um APK válido antes de a compilação concluir e o aplicativo ser testado num aparelho.
