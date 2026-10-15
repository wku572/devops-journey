variable "project" {
  description = "Prefix for all resource names"
  type        = string
  default     = "week11"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "appdb"
}

variable "db_user" {
  description = "Database user"
  type        = string
  default     = "appuser"
}

variable "db_password" {
  description = "Database password, supplied at run time and never stored in a file"
  type        = string
  sensitive   = true

  validation {
    condition     = length(var.db_password) >= 8
    error_message = "db_password must be at least 8 characters."
  }
}

variable "web_port" {
  description = "Port on the host for the web app"
  type        = number
  default     = 5002

  validation {
    condition     = var.web_port >= 1024 && var.web_port <= 65535
    error_message = "web_port must be between 1024 and 65535."
  }
}
