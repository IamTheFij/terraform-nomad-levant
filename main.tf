data "external" "levant" {
  program = ["${path.module}/levant.py"]

  query = {
    template_path  = var.template_path
    consul_address = var.consul_address
    variables      = jsonencode(var.variables)
    var_files      = jsonencode(var.var_files)
  }
}

resource "nomad_job" "levant" {
  count = var.render_only ? 0 : 1
  jobspec = data.external.levant.result.template
}
