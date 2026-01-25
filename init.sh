echo "[fonts] Instalando UbuntuMono Nerd Font..."

FONT_DIR="$HOME/.local/share/fonts"
mkdir -p "$FONT_DIR"

if ! fc-list | grep -qi "`UbuntuMono Nerd Font`"; then
  TMP_DIR=$(mktemp -d)
  cd "$TMP_DIR"

  curl -LO https://github.com/ryanoasis/nerd-fonts/releases/latest/download/UbuntuMono.zip
  unzip UbuntuMono.zip
  cp *.ttf "$FONT_DIR"

  fc-cache -fv
  rm -rf "$TMP_DIR"
else
  echo "UbuntuMono Nerd Font ya está instalada"
fi
