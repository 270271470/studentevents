<template>
  <div class="min-h-full">
    <!-- Navigation -->
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
                  <a href="/user/dashboard" class="text-white ml-4">User Dashboard</a>
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
                <a href="/user/user_manage_booking" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50">Manage Your Booking</a>
              </div>
            </li>
          </ol>
        </nav>
      </div>
    </div>

    <!-- Main content -->
    <main class="-mt-10">
      <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
        <div class="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
          <header class="py-10 mb-6 justify-center">
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
              <h1 class="text-3xl font-medium tracking-tight text-gray-500">Manage Your Booking</h1>
            </div>
          </header>
          <div class="mb-10">
            <div v-if="alertMessage" :class="alertClass" class="alert">
              {{ alertMessage }}
            </div>
            <table class="min-w-full bg-white">
              <thead>
                <tr>
                  <th class="py-2 text-left">Event</th>
                  <th class="py-2 text-left">Event Name</th>
                  <th class="py-2 text-left">Location</th>
                  <th class="py-2 text-left">Date & Time</th>
                  <th class="py-2 text-left">Fee</th>
                  <th class="py-2 text-left">Status</th>
                  <th class="py-2 text-left">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="booking in bookings" :key="booking.id">
                  <td class="py-2">
                    <img :src="booking.event.image_path" alt="Event Image" class="h-10 w-10 rounded-full">
                  </td>
                  <td class="py-2">{{ booking.event.name }}</td>
                  <td class="py-2">{{ booking.event.location }}</td>
                  <td class="py-2">{{ booking.event.date }} {{ booking.event.time }}</td>
                  <td class="py-2">$ {{ booking.total_fee }}</td>
                  <td class="py-2">{{ booking.status }}</td>
                  <td class="py-2">
                    <button v-if="booking.status === 'Pending'" @click="confirmCancel(booking.id)" class="bg-red-500 text-white px-2 py-1 rounded">Cancel</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- Confirmation dialog for cancelling booking -->
  <transition name="modal">
    <div v-if="showCancelConfirm" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-lg leading-6 font-medium text-gray-900">Cancel Booking</h3>
                <div class="mt-2">
                  <p>Are you sure you want to cancel this booking?</p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="cancelBooking" type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 sm:ml-3 sm:w-auto sm:text-sm">
              Yes, Cancel
            </button>
            <button @click="showCancelConfirm = false" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
              No, Keep It
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { Bars3Icon, BellIcon, ArrowLeftOnRectangleIcon, XMarkIcon } from '@heroicons/vue/24/outline';

const userName = ref('');
const bookings = ref([]);
const alertMessage = ref('');
const alertClass = ref('');
const showCancelConfirm = ref(false);
const confirmBookingId = ref(null);
let bookingToCancel = null;

const fetchUserName = async () => {
  try {
    const response = await fetch('/api/current_user');
    const data = await response.json();
    userName.value = data.firstname;
  } catch (error) {
    console.error('Failed to fetch user name:', error);
  }
};

const fetchBookings = async () => {
  try {
    const response = await axios.get('/api/user/bookings');
    bookings.value = response.data;
  } catch (error) {
    console.error('Failed to fetch bookings:', error);
  }
};

const confirmCancel = (bookingId) => {
  bookingToCancel = bookingId;
  showCancelConfirm.value = true;
};

const cancelBooking = async () => {
  if (bookingToCancel !== null) {
    try {
      const response = await axios.patch(`/api/bookings/${bookingToCancel}`);
      if (response.data.message === 'Booking cancelled successfully!') {
        const booking = bookings.value.find(b => b.id === bookingToCancel);
        if (booking) {
          booking.status = 'Cancelled';
        }
        showCancelConfirm.value = false;
        bookingToCancel = null;
      } else {
        console.error('Failed to cancel booking:', response.data.error);
      }
    } catch (error) {
      console.error('Failed to cancel booking:', error);
    }
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


onMounted(() => {
  fetchUserName();
  fetchBookings();
});
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