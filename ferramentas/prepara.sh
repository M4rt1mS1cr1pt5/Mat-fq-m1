#!/bin/sh
# Prepara as ferramentas do build em ferramentas/bin:
#  - MicroPython 1.12, porta unix de 32 bits (com -X heapsize), e mpy-cross;
#  - Luna 2.1 (converte .py em .tns).
# Precisa de git, make, gcc, gcc-multilib e zlib (zlib1g-dev).
set -e
AQUI=$(cd "$(dirname "$0")" && pwd)
TMP=${TMPDIR:-/tmp}/m1tr4m-ferramentas
mkdir -p "$TMP" "$AQUI/bin"
cd "$TMP"
[ -d mp112 ] || git clone --depth 1 --branch v1.12 https://github.com/micropython/micropython.git mp112
make -C mp112/mpy-cross -j4
make -C mp112/ports/unix -j4 MICROPY_FORCE_32BIT=1 MICROPY_PY_FFI=0 \
     MICROPY_PY_BTREE=0 MICROPY_PY_USSL=0 MICROPY_PY_AXTLS=0 CWARN="-Wall -Wno-error"
[ -d luna ] || git clone --depth 1 https://github.com/ndless-nspire/Luna.git luna
make -C luna
cp mp112/ports/unix/micropython mp112/mpy-cross/mpy-cross luna/luna "$AQUI/bin/"
echo "ferramentas em $AQUI/bin"
