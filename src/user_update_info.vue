<!-- /src/user_update_info.vue -->
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
                    <img class="h-9 w-auto ml-5" src="http://studentevents.nz/assets/logo.svg?color=indigo&shade=500" alt="" />
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
            <li>
              <div class="flex items-center">
                <svg class="h-5 w-5 flex-shrink-0 text-slate-400" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path d="M5.555 17.776l8-16 .894.448-8 16-.894-.448z" />
                </svg>
                <a href="/user/user_update_info" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50">Update Contact Information</a>
              </div>
            </li>
          </ol>
        </nav>
      </div>
    </div>

    <main class="-mt-10">
      <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
        <div class="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
          <header class="py-10 mb-6 justify-center">
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
              <h1 class="text-3xl font-bold tracking-tight text-gray-500">Update Your Information</h1>
            </div>
          </header>
          <div class="mb-10">

            <div v-if="alertMessage" :class="alertClass" class="alert">
              {{ alertMessage }}
            </div>

<form @submit.prevent="updateUser">
          <div class="grid grid-cols-6 gap-6">
            <div class="col-span-6 sm:col-span-3">
              <label for="firstname" class="block text-sm font-medium text-gray-700">First Name</label>
              <input v-model="user.firstname" type="text" name="firstname" id="firstname" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="lastname" class="block text-sm font-medium text-gray-700">Last Name</label>
              <input v-model="user.lastname" type="text" name="lastname" id="lastname" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
              <input v-model="user.username" type="text" name="username" id="username" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input v-model="user.email" type="email" name="email" id="email" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="mobile_number" class="block text-sm font-medium text-gray-700">Mobile Number</label>
              <input v-model="user.mobile_number" type="text" name="mobile_number" id="mobile_number" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="address1" class="block text-sm font-medium text-gray-700">Address 1</label>
              <input v-model="user.address1" type="text" name="address1" id="address1" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="address2" class="block text-sm font-medium text-gray-700">Address 2</label>
              <input v-model="user.address2" type="text" name="address2" id="address2" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="suburb" class="block text-sm font-medium text-gray-700">Suburb</label>
              <input v-model="user.suburb" type="text" name="suburb" id="suburb" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="city" class="block text-sm font-medium text-gray-700">City</label>
              <input v-model="user.city" type="text" name="city" id="city" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
              <input v-model="user.country" type="text" name="country" id="country" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label for="postal_code" class="block text-sm font-medium text-gray-700">Postal Code</label>
              <input v-model="user.postal_code" type="text" name="postal_code" id="postal_code" class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
          </div>
          <div class="mt-6 flex justify-center">
            <button type="submit" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Update Information</button>
          </div>
        </form>

          </div>
        </div>
      </div>
    </main>
  </div>

</template>


<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import {
  ArrowLeftOnRectangleIcon,
  Bars3Icon,
  XMarkIcon
} from '@heroicons/vue/24/outline'
import {ref, onMounted} from "vue";
import axios from 'axios';

const userName = ref('');  // Username will be set after fetching from API

const fetchUserName = async () => {
  try {
    const response = await fetch('/api/current_user');
    const data = await response.json();
    userName.value = data.firstname;
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

const user = ref({
  id: '',
  firstname: '',
  lastname: '',
  username: '',
  email: '',
  mobile_number: '',
  address1: '',
  address2: '',
  suburb: '',
  city: '',
  country: '',
  postal_code: ''
});

const loadUserInfo = async () => {
  try {
    const response = await axios.get('/api/current_user');
    if (response.data.error) {
      alert('Failed to load user information.');
    } else {
      user.value = response.data;
    }
  } catch (error) {
    console.error(error);
    alert('Failed to load user information.');
  }
};

const alertMessage = ref('');
const alertClass = ref('');

const updateUser = async () => {
  try {
    const response = await axios.post('/api/update_user_info', user.value);
    if (response.data.error) {
      alert(response.data.error);
    } else {
      alert('User updated successfully');
    }
  } catch (error) {
    console.error(error);
    alert('Failed to update user information.');
  }
};

onMounted(() => {
  loadUserInfo();
});

fetchUserName();  // Fetch username when component is mounted
</script>

<style scoped>
.alert {
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 4px;
  color: white;
}
.alert-success {
  background-color: #4CAF50;
}
.alert-danger {
  background-color: #f44336;
}
</style>