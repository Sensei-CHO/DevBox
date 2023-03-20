<template>
  <NavBar />
  <div class="my-10 mx-auto p-6 container-fluid max-w-6xl bg-gray-700 rounded-xl">
    <div class="container-fluid flex mx-7 text-center justify-center py-2">
      <img src="./assets/logo.png" alt="DevBox Logo" class="w-48">
    </div>
    <div class="container-fluid flex mx-7 text-center justify-center py-2">
      <p class="text-xl text-neutral-300">
        DevBox is a personal project for learning Kubernetes and optimization based on a Raspberry Pi 3B+.
        Through this project, I am learning to deploy and create applications, as well as document the process.
        With DevBox, I am able to gain a better understanding of Kubernetes and optimize the performance of applications
        on a Raspberry Pi.
      </p>
    </div>
  </div>
  <div class="container-fluid flex mx-7 text-center justify-center">
    <h1 class="text-xl text-[#7842e6]">Apps that I run:</h1>
  </div>
  <section class="pt-3 pb-10">
    <div class="mx-auto grid max-w-6xl grid-cols-1 gap-6 p-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3">
      <article class="bg-gray-700 rounded-xl p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
        <a href="https://ubuntu.com/">
          <div class="relative flex items-end overflow-hidden rounded-xl justify-center">
            <img src="https://assets.ubuntu.com/v1/ff6a9a38-ubuntu-logo-2022.svg" alt="Ubuntu logo" class="h-20" />
          </div>
        </a>
        <div class="pt-5">
          <h1 class="text-[#7842e6] text-center font-bold">Cloud ready OS</h1>
          <p class="text-neutral-300">DevBox is running ubuntu as its operating system.</p>
        </div>
      </article>
      <article class="bg-gray-700 rounded-xl p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
        <a href="https://k0sproject.io/">
          <div class="relative flex items-end overflow-hidden rounded-xl justify-center">
            <img src="https://repository-images.githubusercontent.com/271250363/24ce1400-3eff-11eb-8720-eef3bec4324b"
              alt="k0s logo" class="h-20" />
          </div>
        </a>
        <div class="pt-5">
          <h1 class="text-[#7842e6] text-center font-bold">A lightweight Kubernetes alternative</h1>
          <p class="text-neutral-300">I use k0s my main CAAS infrastructure to deploy apps and learn kubernetes
            management.</p>
        </div>
      </article>
      <article class="bg-gray-700 rounded-xl p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
        <a href="https://www.netdata.cloud/">
          <div class="relative flex items-end overflow-hidden rounded-xl justify-center">
            <img src="https://www.laub-home.de/images/thumb/7/72/Netdata_Logo.png/150px-Netdata_Logo.png"
              alt="Netdata logo" class="h-20" />
          </div>
        </a>
        <div class="pt-5">
          <h1 class="text-[#7842e6] text-center font-bold">Monitoring made easy</h1>
          <p class="text-neutral-300">Netdata allows me to monitor the DevBox with low comsumption.</p>
        </div>
      </article>
    </div>
  </section>
  <div class="container-fluid flex flex-col mx-7 text-center justify-center mx-auto">
    <h1 class="text-xl text-[#7842e6]">Some metrics:</h1>
    <div class="my-10 mx-auto p-1 container-fluid max-w-6xl bg-gray-700 rounded-xl flex justify-center">
      <table class="rounded-xl pt-5 table-auto text-center w-auto">
      <thead>
        <tr>
          <th class="text-[#7842e6]">CPU</th>
          <th class="text-[#7842e6]">RAM</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class=""> <embed
              src="https://netdata.devbox.senseicloud.fr//api/v1/badge.svg?chart=system.cpu&alarm=10min_cpu_usage"
              type="image/svg+xml" height="20" /></td>
          <td class=""> <embed
              src="https://netdata.devbox.senseicloud.fr//api/v1/badge.svg?chart=system.ram&alarm=ram_in_use"
              type="image/svg+xml" height="20" /></td>
        </tr>
        <tr>
          <td class=""> <embed
              src="https://netdata.devbox.senseicloud.fr//api/v1/badge.svg?chart=system.load&alarm=load_average_1"
              type="image/svg+xml" height="20" /></td>
          <td class=""> <embed
              src="https://netdata.devbox.senseicloud.fr//api/v1/badge.svg?chart=mem.available&alarm=ram_available"
              type="image/svg+xml" height="20" /></td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>
</template>

<script>
import NavBar from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>
