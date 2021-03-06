#!/bin/bash

echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-session-manager.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
rpmbuild -ba /root/ukui-session-manager.spec