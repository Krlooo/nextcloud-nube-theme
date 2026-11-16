#!/bin/sh
# Deploy helper used by Hermes: unpacks the theme into apps/ and enables it. Run on the StorageBox.
set -eu
W=$HOME/domains/cloud.krlo.dev/public_html
OCC="php -d memory_limit=1G $W/occ"
rm -rf $HOME/hermes/nube_theme_new
mkdir -p $HOME/hermes/nube_theme_new
tar -xzf $HOME/hermes/nube_theme.tgz -C $HOME/hermes/nube_theme_new
rm -rf $W/apps/nube_theme
mv $HOME/hermes/nube_theme_new $W/apps/nube_theme
rm -f $HOME/hermes/nube_theme.tgz
$OCC app:enable nube_theme 2>&1 | grep -v -e i360 -e 'memory limit' || true
# Bust the CSS cache so browsers load the new version.
$OCC maintenance:theme:update 2>&1 | grep -v -e i360 -e 'memory limit' || true
