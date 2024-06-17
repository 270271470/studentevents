import { createApp } from 'vue';
import NavMainHero from './nav_main_hero.vue';
import NavOnly from './nav_only.vue';
import UserRegistration from './registration_form.vue';
import Footer from './footer.vue';

createApp(NavMainHero).mount('#nav_main_hero');
createApp(NavOnly).mount('#nav_only');
createApp(UserRegistration).mount('#user_registration');
createApp(Footer).mount('#footer');
