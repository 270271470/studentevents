<template>
  <div class="bg-gray-100 min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-2xl text-center">
      <h2 class="mt-5 mb-10 text-3xl font-medium text-gray-700">
        Upcoming Clubs Events
      </h2>
      <div class="flex flex-col md:flex-row md:justify-between md:items-center mb-6">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Search for an event..."
          class="mb-4 md:mb-0 p-2 border rounded-md w-full md:w-1/2 lg:w-1/3 mx-auto md:mx-0"
        />
        <select
          v-model="selectedCategory"
          class="p-2 border rounded-md w-full md:w-1/2 lg:w-1/3 mx-auto md:mx-0 md:ml-4"
        >
          <option value="">All Categories</option>
          <option v-for="category in categories" :key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </div>
    </div>
    <ul role="list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-6 gap-y-8 mx-auto px-4 lg:px-20 xl:px-32">
      <li v-for="event in filteredEvents" :key="event.id" class="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-md">
        <div class="flex flex-col items-center gap-x-4 border-b border-gray-900/5 bg-white p-6">
          <img :src="event.image_path" :alt="event.name" class="h-48 w-full object-cover rounded-lg mb-4" />
          <div class="text-lg font-medium leading-6 text-gray-900 text-center">{{ event.name }}</div>
        </div>
        <dl class="-my-3 divide-y bg-white divide-gray-100 px-6 py-4 text-sm leading-6">
          <div class="flex justify-between gap-x-4 py-3">
            <dt class="text-gray-500">Location</dt>
            <dd class="text-gray-700">{{ event.location }}</dd>
          </div>
          <div class="flex justify-between gap-x-4 py-3">
            <dt class="text-gray-500">Date</dt>
            <dd class="text-gray-700">{{ event.date }}</dd>
          </div>
          <div class="flex justify-between gap-x-4 py-3">
            <dt class="text-gray-500">Time</dt>
            <dd class="text-gray-700">{{ event.time }}</dd>
          </div>
          <div class="flex justify-between gap-x-4 py-3">
            <dt class="text-gray-500">Fee</dt>
            <dd class="text-gray-700">${{ event.fee }}</dd>
          </div>
          <div class="flex justify-between gap-x-4 py-3">
            <dt class="text-gray-500">Category</dt>
            <dd class="text-gray-700">{{ event.category }}</dd>
          </div>
          <div class="flex justify-center py-3">
            <button
              @click="openBookingModal(event)"
              class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700 transition duration-300"
            >
              Book Now
            </button>
          </div>
        </dl>
      </li>
    </ul>

    <transition name="modal">
      <div v-if="showBookingModal" class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 transition-opacity" aria-hidden="true">
            <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4" v-if="userLoggedIn">
              <div class="sm:flex sm:items-start">
                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <h3 class="text-lg leading-6 font-medium text-gray-900">
                    Book Event: {{ selectedEvent.name }}
                  </h3>
                  <div class="mt-2">
                    <form @submit.prevent="handleBooking">
                      <div class="mb-4">
                        <label for="fullname" class="block text-gray-700">Full Name</label>
                        <input v-model="bookingForm.fullname" type="text" id="fullname" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" readonly>
                      </div>
                      <div class="mb-4">
                        <label for="quantity" class="block text-gray-700">Quantity</label>
                        <input v-model="bookingForm.quantity" type="number" id="quantity" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                      </div>
                      <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                        <button type="submit" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-500 text-base font-medium text-white hover:bg-blue-700 transition duration-300 sm:ml-3 sm:w-auto sm:text-sm">
                          Confirm Booking
                        </button>
                        <button @click="closeBookingModal" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 transition duration-300 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                          Cancel
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4" v-else>
              <div class="sm:flex sm:items-start">
                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <h3 class="text-lg leading-6 font-medium text-gray-900">
                    You are not logged in
                  </h3>
                  <div class="mt-2">
                    <p class="text-sm text-gray-500">
                      It seems that you are not logged in. Please log in or register to book an event.
                    </p>
                    <div class="mt-4 flex justify-center">
                      <button @click="redirectToLogin" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-green-500 text-base font-medium text-white hover:bg-green-700 transition duration-300 sm:ml-3 sm:w-auto sm:text-sm">
                        Log In
                      </button>
                      <button @click="redirectToRegister" class="w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-orange-500 text-base font-medium text-white hover:bg-orange-700 transition duration-300 sm:ml-3 sm:w-auto sm:text-sm">
                        Register
                      </button>
                    </div>
                    <div class="mt-4 flex justify-center">
                      <button @click="closeBookingModal" type="button" class="w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-red-500 text-base font-medium text-white hover:bg-red-700 transition duration-300 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                        Cancel
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <!-- Notification -->
    <div v-if="showNotification" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-lg leading-6 font-medium text-gray-900">
                  Booking confirmed!
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">Your booking has been confirmed successfully.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="closeNotification" type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-500 text-base font-medium text-white hover:bg-blue-700 sm:ml-3 sm:w-auto sm:text-sm">
              OK
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const events = ref([]);
const categories = ref(['Festivals', 'Workshops', 'Seminars', 'Clubs', 'Outdoor']);
const searchQuery = ref('');
const selectedCategory = ref('Clubs');

const showBookingModal = ref(false);
const selectedEvent = ref(null);
const userLoggedIn = ref(false);
const bookingForm = ref({
  fullname: '',
  quantity: 1
});
const currentUser = ref(null);

const showNotification = ref(false);

const fetchEvents = async () => {
  try {
    const response = await axios.get('/api/events');
    events.value = response.data;
  } catch (error) {
    console.error('Failed to fetch events:', error);
  }
};

const checkUserLoggedIn = async () => {
  try {
    const response = await axios.get('/api/current_user');
    if (response.data) {
      userLoggedIn.value = true;
      currentUser.value = response.data;
      bookingForm.value.fullname = `${response.data.firstname} ${response.data.lastname}`;
    } else {
      userLoggedIn.value = false;
    }
  } catch (error) {
    userLoggedIn.value = false;
    console.error('Failed to check user login status:', error);
  }
};

const openBookingModal = (event) => {
  selectedEvent.value = event;
  showBookingModal.value = true;
  checkUserLoggedIn();
};

const closeBookingModal = () => {
  showBookingModal.value = false;
};

const redirectToLogin = () => {
  window.location.href = '/login';
};

const redirectToRegister = () => {
  window.location.href = '/register';
};

const handleBooking = async () => {
  try {
    const totalFee = selectedEvent.value.fee * bookingForm.value.quantity;
    const bookingData = {
      user_id: currentUser.value.id,
      event_id: selectedEvent.value.id,
      fullname: bookingForm.value.fullname,
      location: selectedEvent.value.location,
      date: selectedEvent.value.date,
      time: selectedEvent.value.time,
      quantity: bookingForm.value.quantity,
      total_fee: totalFee
    };

    console.log('Booking request data:', bookingData); // Add this line

    const response = await axios.post('/api/bookings', bookingData);
    console.log('Booking response:', response.data); // Add this line

    if (response.data.message === 'Booking confirmed!') {
      showNotification.value = true;
      closeBookingModal();
    } else {
      throw new Error('Failed to book event');
    }
  } catch (error) {
    console.error('Failed to book event:', error);
    alert('Failed to book event');
  }
};

const closeNotification = () => {
  showNotification.value = false;
  window.location.href = '/user/user_manage_booking';
};

const filteredEvents = computed(() => {
  return events.value
    .filter(event =>
      event.name.toLowerCase().includes(searchQuery.value.toLowerCase()) &&
      (selectedCategory.value === '' || event.category === selectedCategory.value))
    .sort((a, b) => new Date(a.date) - new Date(b.date));
});

onMounted(() => {
  fetchEvents();
});
</script>

<style scoped>
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.25s ease;
}
.modal-enter, .modal-leave-to {
  opacity: 0;
}
</style>
