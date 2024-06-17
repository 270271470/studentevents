import { createApp } from 'vue';  // Import the createApp function from Vue

// Import custom Vue components
import NavMainHero from './nav_main_hero.vue';
import NavOnly from './nav_only.vue';
import RegistrationForm from './registration_form.vue';
import Footer from './footer.vue';

// Create a Vue app instance with the component and mount it to the element with a matching ID
createApp(NavMainHero).mount('#nav_main_hero');
createApp(NavOnly).mount('#nav_only');
createApp(RegistrationForm).mount('#user_registration');
createApp(Footer).mount('#footer');
