#!/bin/bash

# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

docker run --rm -it --net host node:alpine npx --yes localtunnel --port 8082
