# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

# Set the working directory to all stages
ARG WORKDIR="/app"

# Stage 1: Build from python 3.9
FROM python:3.11-slim AS builder

# Activate argument
ARG WORKDIR

# Do not buffer stdout:
ENV PYTHONUNBUFFERED=1
# Do not create .pyc files:
ENV PYTHONDONTWRITEBYTECODE=1

# Install poetry with project-specific virtual environment (good practice)
RUN pip install poetry && poetry config virtualenvs.in-project true

# Change directory
WORKDIR ${WORKDIR}
# Copy all the project into the container (except those in .dockerignore)
COPY . .

# Install the project using poetry
RUN poetry install --only main

# Stage 2: running app with python 3.9
FROM python:3.11-alpine

# Activate argument
ARG WORKDIR

# Change directory
WORKDIR ${WORKDIR}

# Copy the result from the builder container
COPY --from=builder ${WORKDIR} .

# As good practice, create a user for the application
# For options, see https://boxmatrix.info/wiki/Property:adduser
# -D: no password
# -H: no default home
# -h: use this as home
# -u: use this UID
RUN adduser app -DHh ${WORKDIR} -u 1000
# Switch to this user
USER 1000

# Run some script
CMD [ "./.venv/bin/python", "-c", "import template_sandbox.greeter as gt; gt.main()" ]
#
# Can also use entry points
# ENTRYPOINT ["./.venv/bin/python", "-i"]

# Exposing ports, you can use docker run -p 8182:8000 [...] to map the port 8182
# of the host to the container's 8000
# EXPOSE 8000
#
# Run a simple web server
# CMD [ "./.venv/bin/python", "-m", "http.server" ]
