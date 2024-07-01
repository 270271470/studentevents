<template>
  <footer class="bg-slate-800" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="mx-auto max-w-7xl px-6 pb-8 pt-16 sm:pt-24 lg:px-8 lg:pt-32">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <img class="rounded-lg w-1/2 h-auto mx-2 opacity-75" src="https://www.studentevents.nz/assets/nz-land.png?color=indigo&shade=500" alt="NZ Land">
        <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Events</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li v-for="item in navigation.events" :key="item.name">
                  <a :href="item.href" class="text-sm leading-6 text-gray-300 hover:text-white">{{ item.name }}</a>
                </li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Quick Links</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li v-for="item in navigation.quicklinks" :key="item.name">
                  <a v-if="item.name !== 'Newsletter'" :href="item.href" class="text-sm leading-6 text-gray-300 hover:text-white">{{ item.name }}</a>
                  <a v-else href="#" @click.prevent="openNewsletterModal" class="text-sm leading-6 text-gray-300 hover:text-white">{{ item.name }}</a>
                </li>
              </ul>
            </div>
          </div>
          <div class="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold leading-6 text-white">Company</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li v-for="item in navigation.company" :key="item.name">
                  <a :href="item.href" class="text-sm leading-6 text-gray-300 hover:text-white">{{ item.name }}</a>
                </li>
              </ul>
            </div>
            <div class="mt-10 md:mt-0">
              <h3 class="text-sm font-semibold leading-6 text-white">Legal</h3>
              <ul role="list" class="mt-6 space-y-4">
                <li v-for="item in navigation.legal" :key="item.name">
                  <a :href="item.href" class="text-sm leading-6 text-gray-300 hover:text-white">{{ item.name }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-8 border-t border-white/10 pt-8 md:flex md:items-center md:justify-between">
        <div class="flex space-x-6 md:order-2">
          <a v-for="item in navigation.social" :key="item.name" :href="item.href" class="text-gray-500 hover:text-gray-400">
            <span class="sr-only">{{ item.name }}</span>
            <component :is="item.icon" class="h-6 w-6" aria-hidden="true" />
          </a>
        </div>
        <p class="mt-8 text-xs leading-5 text-gray-400 md:order-1 md:mt-0">&copy; 2024 Student Events, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- Subscribe Modal -->
  <TransitionRoot as="template" :show="openNewsletter">
    <Dialog class="relative z-10" @close="openNewsletter = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
              <div>
                <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-green-100">
                  <CheckIcon class="h-6 w-6 text-green-600" aria-hidden="true" />
                </div>
                <div class="mt-3 text-center sm:mt-5">
                  <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Subscribe to our newsletter</DialogTitle>
                  <div class="mt-2">
                    <input type="email" name="newsletter-email" id="newsletter-email" autocomplete="email" required="" class="w-full appearance-none rounded-md border-0 bg-white/5 px-3 py-1.5 text-base text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-500 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:w-full sm:text-sm sm:leading-6" placeholder="Enter your email" v-model="newsletterEmail" />
                    <div class="mt-2 flex items-start">
                      <input id="confirm" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" v-model="newsletterConfirm">
                      <label for="confirm" class="ml-2 block text-sm text-gray-900">I confirm that I want to subscribe to the newsletter</label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="mt-5 sm:mt-6">
                <button type="button" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="subscribeToNewsletter" :disabled="!newsletterEmail || !newsletterConfirm">Subscribe</button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { CheckIcon } from '@heroicons/vue/24/outline'

const open = ref(false)
const openNewsletter = ref(false)
const email = ref('')
const newsletterEmail = ref('')
const newsletterConfirm = ref(false)

const navigation = {
  events: [
    { name: 'Workshops', href: '/events-workshops' },
    { name: 'Adventure', href: '/events-adventure' },
    { name: 'Outdoor Seminars', href: '/events-outdoor' },
    { name: 'Clubs', href: '/events-clubs' },
  ],
  quicklinks: [
    { name: 'Featured Events', href: '/events' },
    { name: 'All Events', href: '/events' },
    { name: 'Newsletter', href: '#' },
  ],
  company: [
    { name: 'About Us', href: '/about-us' },
    { name: 'Contact Us', href: '/contact-us' },
  ],
  legal: [
    { name: 'Privacy Policy', href: '/privacy-policy' },
    { name: 'Terms of Service', href: '/terms-of-service' },
  ]
}

const handleSubscribe = () => {
  // Handle form submission logic here if needed
  open.value = true
}

const openNewsletterModal = () => {
  openNewsletter.value = true
}

const subscribeToNewsletter = () => {
  if (newsletterEmail.value && newsletterConfirm.value) {
    openNewsletter.value = false
    // Handle newsletter subscription logic here if needed
    alert(`Thank you! ${newsletterEmail.value} has been subscribed to the newsletter.`)
  }
}
</script>