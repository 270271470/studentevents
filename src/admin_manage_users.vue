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
                <a href="/admin/admin_manage_users" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50" aria-current="page">Manage Users</a>
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
  <h2 class="text-2xl font-medium text-gray-500 mt-5 mb-5">Manage Users</h2>

  <div>
    <table class="min-w-full bg-white">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b text-left">Firstname</th>
          <th class="py-2 px-4 border-b text-left">Lastname</th>
          <th class="py-2 px-4 border-b text-left">Email</th>
          <th class="py-2 px-4 border-b text-left">Role</th>
          <th class="py-2 px-4 border-b text-left">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td class="py-2 px-4 border-b">{{ user.firstname }}</td>
          <td class="py-2 px-4 border-b">{{ user.lastname }}</td>
          <td class="py-2 px-4 border-b">{{ user.email }}</td>
          <td class="py-2 px-4 border-b">{{ user.role }}</td>
          <td class="py-2 px-4 border-b">
            <button @click="openEditModal(user)" class="bg-indigo-500 text-white px-2 py-1 rounded mr-2.5">Edit</button>
            <button @click="deleteUser(user.id)" class="bg-rose-500 text-white px-2 py-1 rounded">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Edit Modal -->
    <div v-if="showEditModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
          <h3 class="text-lg leading-6 font-medium text-gray-900">Edit User</h3>
          <div class="mt-2">
            <input v-model="editUser.firstname" placeholder="Firstname" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.lastname" placeholder="Lastname" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.username" placeholder="Username" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.email" placeholder="Email" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.mobile_number" placeholder="Mobile Number" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.address1" placeholder="Address 1" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.address2" placeholder="Address 2" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.suburb" placeholder="Suburb" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.city" placeholder="City" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.country" placeholder="Country" class="w-full border rounded px-3 py-2 mb-2" />
            <input v-model="editUser.postal_code" placeholder="Postal Code" class="w-full border rounded px-3 py-2 mb-2" />
            <select v-model="editUser.role" class="w-full border rounded px-3 py-2 mb-2">
              <option value="user">User</option>
              <option value="admin">Admin</option>
            </select>
          </div>
          <div class="mt-4">
            <button @click="updateUser" class="bg-blue-500 text-white px-4 py-2 rounded">Save</button>
            <button @click="closeEditModal" class="ml-2 bg-gray-500 text-white px-4 py-2 rounded">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>






        </div>
      </div>
    </main>
  </div>
</template>


<script>
import { ref } from 'vue';
import {Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems} from "@headlessui/vue";
import { Bars3Icon, BellIcon, ArrowLeftOnRectangleIcon, XMarkIcon } from '@heroicons/vue/24/outline';


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
    ArrowLeftOnRectangleIcon
  },
  data() {
    return {
      users: [],
      showEditModal: false,
      editUser: {
        id: null,
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
        postal_code: '',
        role: ''
      },
      userName: '' // Add userName here
    };
  },
  created() {
    this.fetchUsers();
    this.fetchUserName(); // Call fetchUserName when component is created
  },
  methods: {
    async fetchUsers() {
      const response = await fetch('/api/users');
      const data = await response.json();
      this.users = data;
    },
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
    openEditModal(user) {
      this.editUser = { ...user };
      this.showEditModal = true;
    },
    closeEditModal() {
      this.showEditModal = false;
      this.editUser = {
        id: null,
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
        postal_code: '',
        role: ''
      };
    },
    async updateUser() {
      const response = await fetch(`/api/users/${this.editUser.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.editUser),
      });
      if (response.ok) {
        this.fetchUsers();
        this.showEditModal = false;
        alert('User updated successfully');
      } else {
        alert('Failed to update user');
      }
    },
    async deleteUser(userId) {
      if (confirm('Are you sure you want to delete this user?')) {
        await fetch(`/api/users/${userId}`, {
          method: 'DELETE',
        });
        this.fetchUsers();
      }
    }
  }
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
