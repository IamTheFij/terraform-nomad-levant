variable "template_path" {
  type     = string
  nullable = false
  description = "Path to the template to be rendered."
}

variable "render_only" {
  type = bool
  default = false
  description = "Indicates if the module should only render the template and return the spec as output."
}

variable "consul_address" {
  type        = string
  default     = null
  nullable    = true
  description = "Consul host and port for making KeyValue lookups"
}

variable "variables" {
  type        = map(string)
  description = "Variables to be passed into Levant with values in JSON form. Since they are passed over the command line, any lists or dictionaries must be converted to JSON and then parsed in your template. If this is unsuitable, you can use var_files."
  default     = {}
}

variable "var_files" {
  type        = list(string)
  description = "Variable files to be passed to Levant. Eg. *.json, *.tf, *.yml, *.yaml"
  default     = []
}
