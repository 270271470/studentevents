<template>
    <header class="bg-slate-800">
      <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
        <div class="flex lg:flex-1">
          <a href="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Student Events</span>
            <img class="h-9 w-auto ml-5" src="http://studentevents.nz/assets/logo.svg?color=indigo&shade=500" alt="" />
          </a>
        </div>
        <div class="flex lg:hidden">
          <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded p-2.5 text-gray-400" @click="mobileMenuOpen = true">
            <span class="sr-only">Open main menu</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end lg:space-x-8">
          <a v-for="item in navigation" :key="item.name" :href="item.href" class="text-sm font-semibold leading-6 text-white py-2 px-4">
            {{ item.name }}
          </a>
          <template v-if="user">
            <div class="flex items-center space-x-4">
              <a href="/user/dashboard" class="bg-indigo-600 hover:bg-indigo-800 text-white font-semibold py-2 px-4 rounded transition duration-300">
                User Dashboard
              </a>
              <span class="text-gray-400">Hi, {{ user.firstname }}</span>
              <button @click="logout" class="bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                <span class="sr-only">Logout</span>
                <ArrowLeftOnRectangleIcon class="h-6 w-6" aria-hidden="true" />
              </button>
            </div>
          </template>
          <template v-else>
            <button v-if="!isLoginPage" @click="navigateTo('/login')" class="bg-green-500 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded">
              Log in
            </button>
            <button v-if="!isRegisterPage" @click="navigateTo('/register')" class="bg-indigo-600 hover:bg-indigo-800 text-white font-semibold py-2 px-4 rounded">
              Register
            </button>
          </template>
        </div>
      </nav>
      <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
        <div class="fixed inset-0 z-50" />
        <DialogPanel class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-gray-900 px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-white/10">
          <div class="flex items-center justify-between">
            <a href="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Student Events</span>
              <img class="h-8 w-auto" src="http://studentevents.nz/assets/StudentEvents.svg?color=indigo&shade=500" alt="" />
            </a>
            <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-400" @click="mobileMenuOpen = false">
              <span class="sr-only">Close menu</span>
              <XMarkIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-6 flow-root">
            <div class="-my-6 divide-y divide-gray-500/25">
              <div class="space-y-2 py-6">
                <a v-for="item in navigation" :key="item.name" :href="item.href" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-white hover:bg-gray-800">{{ item.name }}</a>
              </div>
              <div class="py-6">
                <template v-if="user">
                  <a href="/user/dashboard" class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-gray-800">User Dashboard</a>
                  <span class="block text-gray-400 px-3 py-2.5">Hi, {{ user.firstname }}</span>
                  <button @click="logout" class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-gray-800">Logout</button>
                </template>
                <template v-else>
                  <button v-if="!isLoginPage" @click="navigateTo('/login')" class="block w-full text-left rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-gray-800">Log in</button>
                  <button v-if="!isRegisterPage" @click="navigateTo('/register')" class="block w-full text-left rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-gray-800">Register</button>
                </template>
              </div>
            </div>
          </div>
        </DialogPanel>
      </Dialog>
    </header>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { Bars3Icon, ArrowLeftOnRectangleIcon } from '@heroicons/vue/24/outline'
import { Dialog, DialogPanel } from '@headlessui/vue'
import axios from 'axios'

const navigation = [
  { name: 'About Us', href: '/about-us' },
  { name: 'Contact Us', href: '/contact-us' },
]

const mobileMenuOpen = ref(false)
const user = ref(null)

// Fetch current user
const fetchCurrentUser = async () => {
  try {
    const response = await axios.get('/api/current_user')
    if (response.data) {
      user.value = response.data
    }
  } catch (error) {
    console.error('Failed to fetch current user:', error)
  }
}

onMounted(() => {
  fetchCurrentUser()
})

// Computed property to get the current URL path
const currentPath = computed(() => window.location.pathname)

// Computed properties to check if the current URL matches /login or /register
const isLoginPage = computed(() => currentPath.value === '/login')
const isRegisterPage = computed(() => currentPath.value === '/register')

// Method to navigate to a different route
const navigateTo = (path) => {
  window.location.href = path
}

// Logout method
const logout = async () => {
  try {
    await axios.post('/logout')
    user.value = null
    navigateTo('/')
  } catch (error) {
    console.error('Failed to logout:', error)
  }
}
</script>

<style scoped>
/* Add any custom styles here */
</style>
