terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
    }
  }
}

provider "digitalocean" {
  token = var.do_token
}

variable "do_token" {
  description = "DigitalOcean API token"
  type        = string
  sensitive   = true
}

resource "digitalocean_droplet" "travelguide" {
  name   = "ubuntu-s-1vcpu-512mb-10gb-nyc1"
  region = "nyc1"
  size   = "s-1vcpu-512mb-10gb"
  image  = "ubuntu-24-04-x64"

  tags = [
    "travelguideai",
    "terraform"
  ]
}