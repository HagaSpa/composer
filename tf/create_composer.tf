resource "google_composer_environment" "test-environment" {
   name = "sample"
   project = "studyproject-224907"
   region = "asia-northeast1"
   config {
      node_count = 4

      node_config {
         zone = "asia-northeast1-c"
         machine_type = "n1-standard-1"
         disk_size_gb = 100
      }
   }
}