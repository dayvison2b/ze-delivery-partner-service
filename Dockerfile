FROM python:3.12-alpine3.19
LABEL maintainer="dayvisoncordeiro2001@gmail.com"

# This environment variable is used to control whether Python should
# write bytecode (.pyc) files to disk. 1 = No, 0 = Yes
ENV PYTHONDONTWRITEBYTECODE 1

# This sets Python to immediately flush output to stdout or other output devices, without buffering it first.
# In summary, you'll see Python outputs in real-time.
ENV PYTHONUNBUFFERED 1

# Copy the "djangoapp" and "scripts" folders into the container.
COPY djangoapp /djangoapp
COPY scripts /scripts

# Change the working directory to djangoapp inside the container.
WORKDIR /djangoapp

# Port 8000 will be available for connections external to the container
# It's the port we'll use for Django.
EXPOSE 8000

# RUN executes commands in a shell inside the container to build the image.
# The result of executing the command is stored in the image's file system as a new layer.
# Grouping commands in a single RUN can reduce the number of image layers and make it more efficient.
RUN apk update && \
    apk add --no-cache binutils gdal geos proj-dev && \
  python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  chown -R duser:duser /venv && \
  chmod -R +x /scripts

ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so.34.3.8.4
ENV GEOS_LIBRARY_PATH=/usr/lib/libgeos_c.so.1.18.1

# Add the scripts and venv/bin folder
# to the container's $PATH.
ENV PATH="/scripts:/venv/bin:$PATH"

# Change user to duser
USER duser

# Execute the scripts/commands.sh file
CMD ["commands.sh"]