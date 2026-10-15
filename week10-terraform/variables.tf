variable "container_name" {
  description = "Name of the nginx container"
  type        = string
  default     = "tf-nginx"
}

variable "host_port" {
  description = "Port on the host that maps to nginx"
  type        = number
  default     = 8082

  validation {
    condition     = var.host_port >= 1024 && var.host_port <= 65535
    error_message = "host_port must be between 1024 and 65535."
  }
}

variable "nginx_tag" {
  description = "nginx image tag"
  type        = string
  default     = "latest"
}
