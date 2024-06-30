<template>
  <div class="bg-gray-100 min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-2xl">
      <h2 class="mt-6 text-center text-3xl font-medium text-gray-500">
        User Registration
      </h2>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-2xl">
      <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
        <form @submit.prevent="register" class="space-y-6">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">
              Username
            </label>
            <div class="mt-1">
              <input
                id="username"
                name="username"
                type="text"
                autocomplete="username"
                v-model="username"
                required
                class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
              />
            </div>
          </div>

          <div>
            <label for="about" class="block text-sm font-medium text-gray-700">
              About
            </label>
            <div class="mt-1">
              <textarea
                id="about"
                name="about"
                rows="3"
                v-model="about"
                class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                placeholder="Write a few sentences about yourself."
              ></textarea>
            </div>
          </div>

          <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
            <div>
              <label for="firstname" class="block text-sm font-medium text-gray-700">
                First name
              </label>
              <div class="mt-1">
                <input
                  id="firstname"
                  name="firstname"
                  type="text"
                  autocomplete="given-name"
                  v-model="firstname"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>

            <div>
              <label for="lastname" class="block text-sm font-medium text-gray-700">
                Last name
              </label>
              <div class="mt-1">
                <input
                  id="lastname"
                  name="lastname"
                  type="text"
                  autocomplete="family-name"
                  v-model="lastname"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">
                Email address
              </label>
              <div class="mt-1">
                <input
                  id="email"
                  name="email"
                  type="email"
                  autocomplete="email"
                  v-model="email"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>

            <div>
              <label for="mobile_number" class="block text-sm font-medium text-gray-700">
                Mobile Number
              </label>
              <div class="mt-1">
                <input
                  id="mobile_number"
                  name="mobile_number"
                  type="tel"
                  autocomplete="tel"
                  v-model="mobile_number"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>
          </div>

          <div>
            <label for="address1" class="block text-sm font-medium text-gray-700">
              Address 1
            </label>
            <div class="mt-1">
              <input
                id="address1"
                name="address1"
                type="text"
                autocomplete="street-address"
                v-model="address1"
                required
                class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
              />
            </div>
          </div>

          <div>
            <label for="address2" class="block text-sm font-medium text-gray-700">
              Address 2
            </label>
            <div class="mt-1">
              <input
                id="address2"
                name="address2"
                type="text"
                autocomplete="address-line2"
                v-model="address2"
                class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
              />
            </div>
          </div>

          <div>
            <label for="suburb" class="block text-sm font-medium text-gray-700">
              Suburb
            </label>
            <div class="mt-1">
              <input
                id="suburb"
                name="suburb"
                type="text"
                autocomplete="address-line3"
                v-model="suburb"
                class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
              />
            </div>
          </div>

          <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
            <div>
              <label for="city" class="block text-sm font-medium text-gray-700">
                City
              </label>
              <div class="mt-1">
                <input
                  id="city"
                  name="city"
                  type="text"
                  autocomplete="address-level2"
                  v-model="city"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>

            <div>
              <label for="country" class="block text-sm font-medium text-gray-700">
                Country
              </label>
              <div class="mt-1">
                <input
                  id="country"
                  name="country"
                  type="text"
                  autocomplete="country"
                  v-model="country"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
            <div>
              <label for="postal_code" class="block text-sm font-medium text-gray-700">
                Postal Code
              </label>
              <div class="mt-1">
                <input
                  id="postal_code"
                  name="postal_code"
                  type="text"
                  autocomplete="postal-code"
                  v-model="postal_code"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
            <div>
              <label for="password" class="block text-sm font-medium text-gray-700">
                Password
              </label>
              <div class="mt-1">
                <input
                  id="password"
                  name="password"
                  type="password"
                  autocomplete="new-password"
                  v-model="password"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>

            <div>
              <label for="confirm_password" class="block text-sm font-medium text-gray-700">
                Confirm Password
              </label>
              <div class="mt-1">
                <input
                  id="confirm_password"
                  name="confirm_password"
                  type="password"
                  autocomplete="new-password"
                  v-model="confirm_password"
                  required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Register
            </button>
          </div>

          <div v-if="errorMessage" class="mt-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative">
            <span class="block sm:inline">{{ errorMessage }}</span>
          </div>

          <div v-if="successMessage" class="mt-4 bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative">
            <span class="block sm:inline">{{ successMessage }}</span>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const username = ref('');
    const about = ref('');
    const firstname = ref('');
    const lastname = ref('');
    const email = ref('');
    const mobile_number = ref('');
    const address1 = ref('');
    const address2 = ref('');
    const suburb = ref('');
    const city = ref('');
    const country = ref('');
    const postal_code = ref('');
    const password = ref('');
    const confirm_password = ref('');
    const errorMessage = ref('');
    const successMessage = ref('');

    const register = async () => {
      if (password.value !== confirm_password.value) {
        errorMessage.value = 'Passwords do not match';
        return;
      }

      try {
        const response = await axios.post('/register', {
          username: username.value,
          firstName: firstname.value,
          lastName: lastname.value,
          email: email.value,
          mobile_number: mobile_number.value,
          streetAddress: address1.value,
          address2: address2.value,
          suburb: suburb.value,
          city: city.value,
          country: country.value,
          postalCode: postal_code.value,
          about: about.value,
          password: password.value,
        });

        if (response.data.error) {
          errorMessage.value = response.data.error;
        } else {
          successMessage.value = 'Registration successful. You can now log in.';
          // Clear the form
          username.value = '';
          about.value = '';
          firstname.value = '';
          lastname.value = '';
          email.value = '';
          mobile_number.value = '';
          address1.value = '';
          address2.value = '';
          suburb.value = '';
          city.value = '';
          country.value = '';
          postal_code.value = '';
          password.value = '';
          confirm_password.value = '';
          errorMessage.value = '';
        }
      } catch (error) {
        errorMessage.value = 'Failed to register. Please try again later.';
      }
    };

    return {
      username,
      about,
      firstname,
      lastname,
      email,
      mobile_number,
      address1,
      address2,
      suburb,
      city,
      country,
      postal_code,
      password,
      confirm_password,
      errorMessage,
      successMessage,
      register,
    };
  },
};
</script>
