resource "google_composer_environment" "test-environment" {
   provider = "google-beta"
   name = "sample"
   project = "studyproject-224907"
   region = "asia-northeast1"
   config {
      node_count = 3

      node_config {
         zone = "asia-northeast1-c"
         machine_type = "n1-standard-1"
         disk_size_gb = 20
      }

      software_config {
         python_version = "3"
      }
   }
}