terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "app" {
  name = "${var.project}-net"
}

resource "docker_volume" "db_data" {
  name = "${var.project}-db-data"
}

resource "docker_image" "postgres" {
  name         = "postgres:18-alpine"
  keep_locally = true
}

resource "docker_image" "web" {
  name = "${var.project}-web:latest"

  build {
    context = "${path.module}/../app"
  }

  triggers = {
    source_hash = sha1(join("", [
      filesha1("${path.module}/../app/app.py"),
      filesha1("${path.module}/../app/Dockerfile"),
      filesha1("${path.module}/../app/requirements.txt"),
    ]))
  }
}

resource "docker_container" "db" {
  name  = "${var.project}-db"
  image = docker_image.postgres.image_id

  env = [
    "POSTGRES_DB=${var.db_name}",
    "POSTGRES_USER=${var.db_user}",
    "POSTGRES_PASSWORD=${var.db_password}",
  ]

  networks_advanced {
    name = docker_network.app.name
  }

  volumes {
    volume_name    = docker_volume.db_data.name
    container_path = "/var/lib/postgresql"
  }

  healthcheck {
    test     = ["CMD-SHELL", "pg_isready -U ${var.db_user} -d ${var.db_name}"]
    interval = "5s"
    timeout  = "3s"
    retries  = 10
  }

  wait         = true
  wait_timeout = 60
}

resource "docker_container" "web" {
  name  = "${var.project}-web"
  image = docker_image.web.image_id

  env = [
    "DB_HOST=${docker_container.db.name}",
    "POSTGRES_DB=${var.db_name}",
    "POSTGRES_USER=${var.db_user}",
    "POSTGRES_PASSWORD=${var.db_password}",
  ]

  networks_advanced {
    name = docker_network.app.name
  }

  ports {
    internal = 5000
    external = var.web_port
  }
}
