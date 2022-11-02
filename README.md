# Terraform Nomad Levant

This module renders a Levant template and then creates a Nomad job based on that template.

Limited command line arguemnts are exposed as input variables because Levant is only used to render the job spec. The job is not created by Levant directly, but passed as a spec to a `nomad_job` resource.

Requirements:

  * Levant must be installed on the system because the module will call `levant render` to get the result as an external data source.
