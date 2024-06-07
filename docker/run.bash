#!/bin/bash

CMD="$1"

if [ -z $CMD ]; then
  echo "No command specified"
  exit 1
fi

exec_worker() {
  export VIRTUAL_ENV=/app/venv
  cd /app && poetry run celery -A i3worker.celery_app worker ${I3_WORKER_ARGS}
}

case $CMD in
  worker)
    exec_worker
    ;;
  *)
    exec "$@"
    ;;
esac
