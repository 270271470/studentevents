<template>
  <div class="min-h-full">
    <div class="bg-slate-800 pb-16">
      <Disclosure as="nav" class="bg-slate-800" v-slot="{ open }">
        <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div class="border-b border-slate-700">
            <div class="flex h-16 items-center justify-between px-4 sm:px-0">
              <div class="flex items-center">
                <div class="flex lg:flex-1">
                  <a href="/admin/dashboard" class="-m-1.5 p-1.5">
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
                <a href="/admin/dashboard" class="text-slate-400 hover:text-slate-50">
                  <svg class="h-5 w-5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M9.293 2.293a1 1 0 011.414 0l7 7A1 1 0 0117 11h-1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-3a1 1 0 00-1-1H9a1 1 0 00-1 1v3a1 1 0 01-1 1H5a1 1 0 01-1-1v-6H3a1 1 0 01-.707-1.707l7-7z" clip-rule="evenodd" />
                  </svg>
                  <span class="sr-only">Admin Dashboard</span>
                </a>
              </div>
            </li>
            <li>
              <div class="flex items-center">
                <svg class="h-5 w-5 flex-shrink-0 text-slate-400" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path d="M5.555 17.776l8-16 .894.448-8 16-.894-.448z" />
                </svg>
                <a href="/admin/dashboard" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50">Admin Dashboard</a>
              </div>
            </li>
            <li>
              <div class="flex items-center">
                <svg class="h-5 w-5 flex-shrink-0 text-slate-400" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path d="M5.555 17.776l8-16 .894.448-8 16-.894-.448z" />
                </svg>
                <a href="/admin/view_all_bookings" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50" aria-current="page">All Bookings</a>
              </div>
            </li>
          </ol>
        </nav>
      </div>
    </div>

    <main class="-mt-10">
      <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
        <div class="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
          <header class="py-10 flex justify-between items-center">
            <div>
              <h1 class="text-3xl font-bold tracking-tight text-slate-800">Admin Dashboard</h1>
              <h2 class="text-2xl font-medium text-gray-500 mt-5">All Bookings</h2>
            </div>
            <input
              type="text"
              v-model="searchQuery"
              placeholder="Search by event or user..."
              class="p-2 border rounded-md w-full md:w-1/2 lg:w-1/3 mx-auto md:mx-0"
            />
          </header>

          <div class="mb-10">
            <table class="min-w-full mt-5 bg-white">
              <thead>
                <tr>
                  <th class="py-2"></th>
                  <th class="py-2 text-left">User</th>
                  <th class="py-2 text-left">Event Name</th>
                  <th class="py-2 text-left">Location</th>
                  <th class="py-2 text-left">Date</th>
                  <th class="py-2 text-left">Time</th>
                  <th class="py-2 text-left">Fee</th>
                  <th class="py-2 text-left">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="booking in filteredBookings" :key="booking.id">
                  <td class="py-2">
                    <img :src="booking.event.image_path" alt="Event Image" class="h-10 w-10 rounded-full">
                  </td>
                  <td class="py-2">{{ booking.user.fullname }}</td>
                  <td class="py-2">{{ booking.event.name }}</td>
                  <td class="py-2">{{ booking.event.location }}</td>
                  <td class="py-2">{{ booking.event.date }}</td>
                  <td class="py-2">{{ booking.event.time }}</td>
                  <td class="py-2">${{ booking.total_fee }}</td>
                  <td class="py-2">
                    <span :class="statusClass(booking.status)">{{ booking.status }}</span>
                  </td>
                </tr>
              </tbody>
            </table>

            <!-- Pagination -->
            <nav class="flex items-center justify-between border-t border-gray-200 px-4 sm:px-0 mt-4">
              <div class="-mt-px flex w-0 flex-1">
                <button @click="previousPage" :disabled="currentPage === 1" class="inline-flex items-center border-t-2 border-transparent pr-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700 disabled:opacity-50">
                  <ArrowLongLeftIcon class="mr-3 h-5 w-5 text-gray-400" aria-hidden="true" />
                  Previous
                </button>
              </div>
              <div class="hidden md:-mt-px md:flex">
                <span v-for="page in totalPages" :key="page" @click="goToPage(page)" :class="pageClass(page)" class="inline-flex items-center border-t-2 px-4 pt-4 text-sm font-medium cursor-pointer">
                  {{ page }}
                </span>
              </div>
              <div class="-mt-px flex w-0 flex-1 justify-end">
                <button @click="nextPage" :disabled="currentPage === totalPages" class="inline-flex items-center border-t-2 border-transparent pl-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700 disabled:opacity-50">
                  Next
                  <ArrowLongRightIcon class="ml-3 h-5 w-5 text-gray-400" aria-hidden="true" />
                </button>
              </div>
            </nav>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { Bars3Icon, BellIcon, ArrowLeftOnRectangleIcon, XMarkIcon, ArrowLongLeftIcon, ArrowLongRightIcon } from '@heroicons/vue/24/outline';
import axios from 'axios';

export default {
  components: {
    DisclosurePanel,
    DisclosureButton,
    Disclosure,
    MenuButton,
    Menu,
    MenuItem,
    Bars3Icon,
    XMarkIcon,
    MenuItems,
    BellIcon,
    ArrowLeftOnRectangleIcon,
    ArrowLongLeftIcon,
    ArrowLongRightIcon
  },

  data() {
    return {
      bookings: [],
      userName: '',
      searchQuery: '',
      currentPage: 1,
      itemsPerPage: 10
    };
  },

  computed: {
    filteredBookings() {
      return this.bookings.filter(booking =>
        booking.user.fullname.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        booking.event.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    paginatedBookings() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.filteredBookings.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.filteredBookings.length / this.itemsPerPage);
    }
  },

  created() {
    this.fetchUserName(); // Call fetchUserName when component is created
    this.fetchAllBookings(); // Fetch all bookings when component is created
  },

  methods: {
    async fetchUserName() {
      try {
        const response = await fetch('/api/current_user');
        const data = await response.json();
        this.userName = data.firstname;
      } catch (error) {
        console.error('Failed to fetch user name:', error);
      }
    },
    async logout() {
      try {
        await fetch('/logout', { method: 'POST' });
        window.location.href = '/';
      } catch (error) {
        console.error('Failed to logout:', error);
      }
    },
    async fetchAllBookings() {
      try {
        const response = await axios.get('/api/bookings/all');
        this.bookings = response.data;
      } catch (error) {
        console.error('Failed to fetch all bookings:', error);
      }
    },
    statusClass(status) {
      if (status === 'Approved') return 'text-green-500';
      if (status === 'Pending') return 'text-orange-500';
      if (status === 'Cancelled') return 'text-red-500';
      return '';
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    goToPage(page) {
      this.currentPage = page;
    },
    pageClass(page) {
      return page === this.currentPage
        ? 'border-indigo-500 text-indigo-600'
        : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300';
    }
  }
};
</script>

<style scoped>
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.25s ease;
}
.modal-enter, .modal-leave-to {
  opacity: 0;
}
</style>
