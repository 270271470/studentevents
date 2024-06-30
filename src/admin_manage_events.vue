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
                <a href="/admin/admin_manage_events" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50" aria-current="page">Manage Events</a>
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
              <h1 class="text-3xl font-bold tracking-tight text-slate-800">Admin Dashboard</h1>
            </div>
          </header>

          <div class="mb-10">
            <h2 class="text-2xl font-medium text-gray-500 mt-5 mb-5">Manage Events</h2>
            <div class="flex justify-end">
              <button @click="openModal('add')" class="bg-teal-500 text-white px-4 py-2 rounded">Add New Event</button>
            </div>
            <table class="min-w-full mt-5 bg-white">
              <thead>
                <tr>
                  <th class="py-2"></th>
                  <th class="py-2 text-left">Event Name</th>
                  <th class="py-2 text-left">Category</th>
                  <th class="py-2 text-left">Location</th>
                  <th class="py-2 text-left">Date</th>
                  <th class="py-2 text-left">Time</th>
                  <th class="py-2 text-left">Fee</th>
                  <th class="py-2 text-left">Manage</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="event in paginatedEvents" :key="event.id">
                  <td class="py-2">
                    <img :src="`/${event.image_path}`" alt="Event Image" class="h-10 w-10 rounded-full">
                  </td>
                  <td class="py-2">{{ event.name }}</td>
                  <td class="py-2">{{ event.category }}</td>
                  <td class="py-2">{{ event.location }}</td>
                  <td class="py-2">{{ event.date }}</td>
                  <td class="py-2">{{ event.time }}</td>
                  <td class="py-2">{{ event.fee }}</td>
                  <td class="py-2">
                    <button @click="openModal('edit', event)" class="bg-indigo-500 text-white px-2 py-1 rounded mr-2.5">Edit</button>
                  </td>
                </tr>
              </tbody>
            </table>

            <nav class="flex items-center justify-between border-t border-gray-200 px-4 sm:px-0 mt-4">
              <div class="-mt-px flex w-0 flex-1">
                <button
                  @click="prevPage"
                  :disabled="currentPage === 1"
                  class="inline-flex items-center border-t-2 border-transparent pr-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700 disabled:opacity-50"
                >
                  <ArrowLongLeftIcon class="mr-3 h-5 w-5 text-gray-400" aria-hidden="true" />
                  Previous
                </button>
              </div>
              <div class="hidden md:-mt-px md:flex">
                <span
                  v-for="page in totalPages"
                  :key="page"
                  @click="setPage(page)"
                  :class="['inline-flex items-center border-t-2 px-4 pt-4 text-sm font-medium', currentPage === page ? 'border-indigo-500 text-indigo-600' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300']"
                  aria-current="page"
                >
                  {{ page }}
                </span>
              </div>
              <div class="-mt-px flex w-0 flex-1 justify-end">
                <button
                  @click="nextPage"
                  :disabled="currentPage === totalPages"
                  class="inline-flex items-center border-t-2 border-transparent pl-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700 disabled:opacity-50"
                >
                  Next
                  <ArrowLongRightIcon class="ml-3 h-5 w-5 text-gray-400" aria-hidden="true" />
                </button>
              </div>
            </nav>

            <!-- Add/Edit Event Modal -->
            <transition name="modal">
              <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto">
                <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                  <div class="fixed inset-0 transition-opacity" aria-hidden="true">
                    <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
                  </div>
                  <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                  <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                      <div class="sm:flex sm:items-start">
                        <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                          <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                            {{ modalType === 'add' ? 'Add New Event' : 'Edit Event' }}
                          </h3>
                          <div class="mt-2">
                            <form @submit.prevent="handleSubmit">
                              <div class="mb-4">
                                <label for="name" class="block text-gray-700">Event Name</label>
                                <input v-model="eventForm.name" type="text" id="name" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                              </div>
                              <div class="mb-4">
                                <label for="category" class="block text-gray-700">Category</label>
                                <select v-model="eventForm.category" id="category" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                                  <option value="Festivals">Festivals</option>
                                  <option value="Workshops">Workshops</option>
                                  <option value="Seminars">Seminars</option>
                                  <option value="Clubs">Clubs</option>
                                  <option value="Outdoor">Outdoor</option>
                                </select>
                              </div>
                              <div class="mb-4">
                                <label for="location" class="block text-gray-700">Location</label>
                                <input v-model="eventForm.location" type="text" id="location" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                              </div>
                              <div class="mb-4">
                                <label for="date" class="block text-gray-700">Date</label>
                                <input v-model="eventForm.date" type="date" id="date" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                              </div>
                              <div class="mb-4">
                                <label for="time" class="block text-gray-700">Time</label>
                                <input v-model="eventForm.time" type="time" id="time" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                              </div>
                              <div class="mb-4">
                                <label for="fee" class="block text-gray-700">Fee</label>
                                <input v-model="eventForm.fee" type="number" id="fee" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                              </div>
                              <div class="mb-4">
                                <label for="image" class="block text-gray-700">Event Image</label>
                                <input @change="handleImageUpload" type="file" id="image" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                              </div>
                              <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                                <button type="submit" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-500 text-base font-medium text-white hover:bg-blue-600 sm:ml-3 sm:w-auto sm:text-sm">
                                  {{ modalType === 'add' ? 'Add Event' : 'Update Event' }}
                                </button>
                                <button @click="closeModal" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                                  Cancel
                                </button>
                              </div>
                            </form>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { Bars3Icon, BellIcon, ArrowLeftOnRectangleIcon, ArrowLongLeftIcon, ArrowLongRightIcon, XMarkIcon } from '@heroicons/vue/24/outline';

const events = ref([]);
const showModal = ref(false);
const modalType = ref('add');
const eventForm = ref({
  id: null,
  name: '',
  location: '',
  date: '',
  time: '',
  fee: '',
  image_path: '',
  category: ''
});
const eventImage = ref(null);

const userName = ref('');
const currentPage = ref(1);
const itemsPerPage = ref(5);

const paginatedEvents = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return events.value.slice(start, end);
});

const totalPages = computed(() => Math.ceil(events.value.length / itemsPerPage.value));

const setPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const fetchEvents = async () => {
  try {
    const response = await axios.get('/api/events');
    events.value = response.data;
  } catch (error) {
    console.error('Failed to fetch events:', error);
  }
};

const openModal = (type, event = null) => {
  modalType.value = type;
  if (type === 'edit' && event) {
    eventForm.value = { ...event };
  } else {
    eventForm.value = {
      id: null,
      name: '',
      location: '',
      date: '',
      time: '',
      fee: '',
      image_path: '' // Initialize image_path field
    };
  }
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

const handleImageUpload = (event) => {
  eventImage.value = event.target.files[0];
};

const handleSubmit = async () => {
  try {
    const formData = new FormData();
    for (const key in eventForm.value) {
      formData.append(key, eventForm.value[key]);
    }
    if (eventImage.value) {
      formData.append('file', eventImage.value);
    }

    if (modalType.value === 'add') {
      await axios.post('/api/events', formData);
      alert('Event added successfully');
    } else {
      await axios.put(`/api/events/${eventForm.value.id}`, formData);
      alert('Event updated successfully');
    }
    await fetchEvents();
    closeModal();
  } catch (error) {
    console.error('Failed to submit event:', error);
    alert('Failed to submit event');
  }
};

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

onMounted(() => {
  fetchEvents();
  fetchUserName();
});
</script>

<style scoped>
/* Add your custom styles here */
</style>
