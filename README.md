# ProjetoUrnaFlet app

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

### Anotações:
- cadastro.py -> O formulário de cadastro, usuário novo (PUBLICO)
- criacao_votacao.py -> O formulario para criar uma votação (ADM)
- dashboard_publico.py -> Que aparece as votações recentes, funcionalidades limitadas (PUBLICO)
- dashboard.py -> Dashboard do ADM, pode excluir votações e ver dandidatos (ADM)
- login.py -> Area de login, quando ja tenho uma conta (PUBLICO)
- sobre_a_votacao.py -> Tela que mostra detalhes de uma votação (USUÁRIO)
- tela_downloads.py -> Tela que mostra os downloads (PUBLICO)
- tela_inicio.py -> Tela principal, falando do projeto (PUBLICO)
- tela_votacao.py -> Tela para realizar a votação (USUÁRIO)
- dashboard_usuario.py -> Mostra informações gerais das votações no momento (USUÁRIO)
- status_votacao_adm.py -> Mostra Informações pro adm sobre a votação, com mais algumas funcionalidades (ADM)
- enviar_candidatura.py -> Confirmar sua candidatura para a votação