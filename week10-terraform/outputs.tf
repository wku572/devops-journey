output "url" {
  description = "Where the web server is reachable"
  value       = "http://localhost:${var.host_port}"
}

output "container_id" {
  description = "ID of the nginx container"
  value       = docker_container.web.id
}
