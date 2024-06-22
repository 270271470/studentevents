<template>
  <div class="min-h-full">
    <div class="bg-slate-800 pb-16">
      <Disclosure as="nav" class="bg-slate-800" v-slot="{ open }">
        <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div class="border-b border-slate-700">
            <div class="flex h-16 items-center justify-between px-4 sm:px-0">
              <div class="flex items-center">
                <div class="flex lg:flex-1">
                  <a href="/user/dashboard" class="-m-1.5 p-1.5">
                    <span class="sr-only">Student Events</span>
                    <img class="h-10 w-auto ml-5" src="http://studentevents.nz/assets/logo.svg?color=indigo&shade=500" alt="" />
                  </a>
                </div>
              </div>
              <div class="hidden md:block">
                <div class="ml-4 flex items-center md:ml-6">
                  <span class="text-gray-400">Welcome back, {{ userName }}</span>
                  <button @click="logout" class="ml-4 bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                    <span class="sr-only">Logout</span>
                    <ArrowLeftOnRectangleIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
              </div>
              <div class="-mr-2 flex md:hidden">
                <!-- Mobile menu button -->
                <DisclosureButton class="relative inline-flex items-center justify-center rounded-md bg-gray-800 p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                  <span class="absolute -inset-0.5" />
                  <span class="sr-only">Open main menu</span>
                  <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
                  <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
                </DisclosureButton>
              </div>
            </div>
          </div>
        </div>
      </Disclosure>

      <br><br>
      <!-- Breadcrumb Navigation -->
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 pt-4">
        <nav class="flex" aria-label="Breadcrumb">
          <ol role="list" class="flex items-center space-x-4 ml-5">
            <li>
              <div>
                <a href="/user/dashboard" class="text-slate-400 hover:text-slate-50">
                  <svg class="h-5 w-5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M9.293 2.293a1 1 0 011.414 0l7 7A1 1 0 0117 11h-1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-3a1 1 0 00-1-1H9a1 1 0 00-1 1v3a1 1 0 01-1 1H5a1 1 0 01-1-1v-6H3a1 1 0 01-.707-1.707l7-7z" clip-rule="evenodd" />
                  </svg>
                  <span class="sr-only">User Dashboard</span>
                </a>
              </div>
            </li>
            <li>
              <div class="flex items-center">
                <svg class="h-5 w-5 flex-shrink-0 text-slate-400" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path d="M5.555 17.776l8-16 .894.448-8 16-.894-.448z" />
                </svg>
                <a href="/user/dashboard" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50">User Dashboard</a>
              </div>
            </li>
          </ol>
        </nav>
      </div>
    </div>

    <main class="-mt-10">
      <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
        <div class="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
          <header class="py-10">
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
              <h1 class="text-3xl font-bold tracking-tight text-gray-500">User Dashboard</h1>
            </div>
          </header>
          <div class="mb-10">
            <ul role="list" class="mt-3 grid grid-cols-1 gap-5 sm:grid-cols-2 sm:gap-6 lg:grid-cols-3">
              <li class="col-span-1 flex rounded-md shadow-sm h-32">
                <div class="flex w-28 flex-shrink-0 items-center justify-end rounded-l-md bg-violet-500 text-sm font-bold text-violet-300">
                  <CogIcon class="h-10 w-10" aria-hidden="true" />
                </div>
                <div class="flex flex-1 items-center justify-between truncate rounded-r-md border-b border-r border-t border-violet-500 bg-violet-500">
                  <div class="flex-1 truncate px-4 py-2">
                    <a href="/user/user_manage_booking" class="font-medium text-violet-100 hover:via-violet-100 text-xl">Manage Booking</a>
                  </div>
                </div>
              </li>
              <li class="col-span-1 flex rounded-md shadow-sm">
                <div class="flex w-28 flex-shrink-0 items-center justify-end rounded-l-md bg-indigo-500 text-sm font-bold text-indigo-300">
                  <MagnifyingGlassIcon class="h-10 w-10" aria-hidden="true" />
                </div>
                <div class="flex flex-1 items-center justify-between truncate rounded-r-md border-b border-r border-t border-indigo-500 bg-indigo-500">
                  <div class="flex-1 truncate px-4 py-2">
                    <a href="/events" class="font-medium text-indigo-100 hover:text-indigo-100 text-xl">Find An Event</a>
                  </div>
                </div>
              </li>
              <li class="col-span-1 flex rounded-md shadow-sm">
                <div class="flex w-28 flex-shrink-0 items-center justify-end rounded-l-md bg-rose-500 text-sm font-bold text-rose-300">
                  <UserIcon class="h-10 w-10" aria-hidden="true" />
                </div>
                <div class="flex flex-1 items-center justify-between truncate rounded-r-md border-b border-r border-t border-rose-500 bg-rose-500">
                  <div class="flex-1 truncate px-4 py-2">
                    <a href="/admin/admin_manage_events" class="font-medium text-teal-100 hover:text-amber-100 text-xl">Contact Information</a>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  </div>
  <div class="bg-gray-100 px-1 py-1 sm:py-1 lg:px-1">
    <div class="mx-auto max-w-2xl text-center">
      <p class="text-base font-bold leading-7 text-red-500">Need Help?</p>
      <a href="/support-center" class="mt-2 flex items-center justify-center">
        <h2 class="text-2xl font-bold tracking-tight text-gray-700 sm:text-3xl">Visit Support Center</h2>
        <img class="ml-2 h-12 w-12" src="https://www.studentevents.nz/assets/life-saver.svg" alt="Life Preserver Icon">
      </a>
    </div>
  </div>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import {
  ArrowLeftOnRectangleIcon,
  Bars3Icon,
  BellIcon,
  ClockIcon, CogIcon, MagnifyingGlassIcon,
  EyeIcon,
  UserIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'
import {ref} from "vue";

const userName = ref('');  // Username will be set after fetching from API

const fetchUserName = async () => {
  try {
    const response = await fetch('/api/current_user');
    const data = await response.json();
    userName.value = data.name;
  } catch (error) {
    console.error('Failed to fetch user name:', error);
  }
};

const logout = async () => {
  try {
    await fetch('/logout', { method: 'POST' });
    window.location.href = '/';
  } catch (error) {
    console.error('Failed to logout:', error);
  }
};

fetchUserName();  // Fetch username when component is mounted
</script>