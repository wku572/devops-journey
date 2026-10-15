output "url" {
  description = "Where the web app is reachable"
  value       = "http://localhost:${var.web_port}"
}

output "db_container" {
  description = "Name of the database container"
  value       = docker_container.db.name
}
