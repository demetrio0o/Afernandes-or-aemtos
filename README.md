<p align="center"><img src="assets/logo.png" width="120" alt="A Fernandes"></p>

# A Fernandes Orçamentos

App de orçamentos de serviços e materiais: catálogo com fotos, ficha do cliente, itens avulsos, desconto e PDF pronto para enviar.
O mesmo código gera o **programa para Windows (.exe)** e o **APK para Android**.

## Como baixar o programa e o APK (sem instalar nada no seu PC)

O GitHub compila tudo sozinho:

1. Crie um repositório no GitHub e envie esta pasta (veja abaixo).
2. Abra a aba **Actions** > **Gerar programa (PC) e APK (celular)** > **Run workflow**.
3. Espere uns 5 a 10 minutos. Ao terminar, clique na execução e baixe em **Artifacts**:
   - `A-Fernandes-Windows`: instalador (`...Setup...exe`) e versão portátil (`...portable...exe`)
   - `A-Fernandes-Android`: `A-Fernandes-Orcamentos.apk`

Para publicar em **Releases** (link fixo de download), crie uma tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## Enviar para o GitHub

```bash
cd a-fernandes-orcamentos
git init
git add .
git commit -m "Primeira versão"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/a-fernandes-orcamentos.git
git push -u origin main
```

## Instalar no celular

Passe o APK para o celular, abra o arquivo e permita "instalar apps desconhecidos" quando o Android pedir.
O APK é de teste (assinado com a chave de debug do Android) e instala normalmente. Para publicar na Play Store seria preciso gerar uma versão assinada por você.

## Rodar ou compilar no seu computador (opcional)

Precisa do [Node.js 22](https://nodejs.org).

```bash
npm install
npm start            # abre o programa
npm run build:win    # gera o instalador em dist/
```

APK local (precisa de Android Studio e JDK 21):

```bash
npm run android:add
npm run android:assets
npm run android:sync
npm run android:open   # abre o Android Studio: Build > Build APK
```

## Onde ficam os dados

Tudo é salvo **no próprio aparelho** (programa ou app), sem internet. Os dados do PC e do celular são separados.

- **Catálogo de materiais:** use *Baixar lista* num aparelho e *Importar* no outro.
- **Clientes e orçamentos:** não são sincronizados entre aparelhos. Cada ficha pode ser baixada em PDF.
- Desinstalar o app ou limpar os dados dele apaga o que estava salvo. Faça *Baixar lista* de vez em quando como cópia de segurança.

No celular, *Baixar PDF* e *Baixar lista* abrem a folha de compartilhar do Android (salvar em Arquivos, WhatsApp, e-mail...).

## Estrutura

```
www/index.html           o app (HTML + CSS + JS em um arquivo)
electron/main.js         janela do programa de PC
capacitor.config.json    configuração do app Android
scripts/prepare-www.js   copia jsPDF e fontes para funcionar offline
assets/                  logo e ícones/splash do Android
build/                   ícone do Windows
tools/make-icons.py      regenera os ícones a partir de assets/logo.png
.github/workflows/       compilação automática (exe + apk)
```

Para trocar a logo: substitua `assets/logo.png` e rode `python tools/make-icons.py`. A logo que aparece dentro do app e no PDF está embutida em `www/index.html`.
