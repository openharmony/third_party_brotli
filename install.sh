#!/bin/bash

# Copyright (c) 2024 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

SRC_DIR="$1"
CODE_DIR="$2"

set -e
echo "brotli test : $SRC_DIR" > brotlitest.txt
echo "brotli test : $CODE_DIR" > brotlitest.txt
if [ "$SRC_DIR" == "" ] || [ "$CODE_DIR" == "" ]; then
    echo "brotli test :src_dir or code_dir empty" > brotlitest.txt
    exit 1
fi

if [ -d "$CODE_DIR" ]; then
    rm -rf "$CODE_DIR"
fi

mkdir -p $CODE_DIR/brotli-1.1.0
cp -r $SRC_DIR/* $CODE_DIR/brotli-1.1.0
echo "brotli test :copy brotli" > brotlitest.txt