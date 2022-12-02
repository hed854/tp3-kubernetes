# TP 3 

## problem to solve

[source](https://k8s-mise-en-oeuvre.github.io/docs/index/kubernetes-exploitation/#tp-version-2-on-k3s-instead-of-aws)

* DB with pv, pvc (hostpath), configmap and secret
* Expose DB nodeport
* Frontend app calling DB
* Expose frontend app

## about the solution

This solution uses:

* a Postgresql database engine with a `docker` database which has a `test` table
* a custom Python frontend. 

The frontend is packaged in its own Docker image and made available to the cluster through a private registry.

## howto run

run private registry

```
docker run -d -p 5000:5000 --restart always --name registry registry
```

configure k3s to use this registry `/etc/rancher/k3s/registries.yaml`

```
mirrors:
  "lx-8-9:5000":
    endpoint:
      - "http://lx-8-9:5000"

```

restart k3s

```
sudo systemctl restart k3s
```

apply everything excepted the frontend 

* configmaps, secrets
* pc, pvc
* postgres deploy
* postgres service

run custom frontend build (build, tag, push and apply)

```
./deploy-frontend.sh
```

## create the db init configmap

edit db-init.sh

run 

```
kubectl create configmap toto --from-file=init-db.sh --dry-run=client -o yaml
```
