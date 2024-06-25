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
                <a href="/support-center" class="ml-4 text-sm font-medium text-slate-400 hover:text-slate-50">Support Center</a>
              </div>
            </li>
          </ol>
        </nav>
      </div>
    </div>

    <main class="-mt-10">
      <div class="mx-auto max-w-7xl px-4 pb-6 sm:px-6 lg:px-8">
        <div class="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
          <header class="py-10">
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
              <h1 class="text-3xl font-bold tracking-tight text-gray-500">Support Center</h1>
            </div>
          </header>
  <div class="bg-white">
    <div class="mx-auto max-w-7xl px-1 py-1 sm:py-5 lg:px-1 lg:py-1">
      <div class="mx-auto max-w-4xl divide-y divide-gray-900/10">
        <dl class="mt-10 space-y-6 divide-y divide-gray-900/10">
          <Disclosure as="div" v-for="faq in faqs" :key="faq.question" class="pt-6" v-slot="{ open }">
            <dt>
              <DisclosureButton class="flex w-full items-start justify-between text-left text-gray-600">
                <span class="text-lg font-semibold leading-7">{{ faq.question }}</span>
                <span class="ml-6 flex h-7 items-center">
                  <PlusSmallIcon v-if="!open" class="h-6 w-6" aria-hidden="true" />
                  <MinusSmallIcon v-else class="h-6 w-6" aria-hidden="true" />
                </span>
              </DisclosureButton>
            </dt>
            <DisclosurePanel as="dd" class="mt-2 pr-12">
              <p class="text-base leading-7 text-gray-600">{{ faq.answer }}</p>
            </DisclosurePanel>
          </Disclosure>
        </dl>
      </div>
    </div>
  </div>
        </div>
      </div>
    </main>
  </div>

</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { ArrowLeftOnRectangleIcon, Bars3Icon, XMarkIcon, MinusSmallIcon, PlusSmallIcon} from '@heroicons/vue/24/outline'
import {ref} from "vue";

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

const faqs = [
{
    question: "How can I find upcoming student events in New Zealand?",
    answer:
      "You can visit the 'Events' section on our website where we list all the upcoming seminars, workshops, and social events tailored for students. The events are categorized by date and location for your convenience.",
  },
  {
    question: "Can I book tickets for multiple events at once?",
    answer:
      "Yes, our website allows you to add multiple events to your cart and purchase tickets in a single transaction. This makes it easy to plan your schedule and attend various events.",
  },
  {
    question: "Are there any discounts available for group bookings?",
    answer:
      "We offer special discounts for group bookings. You can check the event details for specific group discounts or contact our support team for more information on bulk purchases.",
  },
  {
    question: "How can I get notifications about new events?",
    answer:
      "You can subscribe to our newsletter or follow us on social media to receive regular updates about new and upcoming events. Additionally, you can enable push notifications on our website to stay informed.",
  },
  {
    question: "Is there a way to filter events by category or interest?",
    answer:
      "Absolutely! Our website features a filtering option that allows you to search for events by category, such as seminars, workshops, sports, or social gatherings. This helps you find events that match your interests.",
  },
  {
    question: "What payment methods are accepted for ticket purchases?",
    answer:
      "We accept various payment methods, including credit/debit cards, PayPal, and bank transfers. All transactions are securely processed to ensure your personal information is protected.",
  },
  {
    question: "Can I cancel or transfer my ticket to another event?",
    answer:
      "Yes, you can cancel your ticket within a specified period before the event date. We also allow ticket transfers to other events or to another person. Please check our cancellation policy for more details.",
  },
  {
    question: "How can I become a volunteer for student events?",
    answer:
      "We welcome volunteers to help us organize and manage events. You can apply to become a volunteer by filling out the form on our 'Volunteer' page. Our team will review your application and get in touch with you.",
  },
  {
    question: "Are there any virtual events available?",
    answer:
      "Yes, we offer a variety of virtual events that you can attend from the comfort of your home. These include webinars, online workshops, and virtual meetups. Check our events page for more information on virtual events.",
  },
  {
    question: "How can event organizers list their events on your website?",
    answer:
      "Event organizers can list their events by creating an account and submitting the event details through our 'List an Event' page. Our team will review the submission and approve it for listing on our website.",
  },
]

fetchUserName();  // Fetch username when component is mounted
</script>