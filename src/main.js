import { createApp } from 'vue';  // Import the createApp function from Vue

// Import custom Vue components
import NavMainHero from './nav_main_hero.vue';
import NavOnly from './nav_only.vue';
import RegistrationForm from './registration_form.vue';
import AdminDash from './admin_dashboard.vue';
import UserDash from './user_dashboard.vue';
import AdminManageUsers from './admin_manage_users.vue';
import UserUpdateInfo from './user_update_info.vue';
import UserLogin from './login.vue';
import SupportCenter from './support-center.vue';
import PrivacyPolicy from './privacy-policy.vue';
import ServiceTerms from './terms-of-service.vue';
import ContactUs from './contact-us.vue';
import Footer from './footer.vue';

// Create a Vue app instance with the component and mount it to the element with a matching ID
createApp(NavMainHero).mount('#nav_main_hero');
createApp(NavOnly).mount('#nav_only');
createApp(RegistrationForm).mount('#user_registration');
createApp(AdminDash).mount('#admin-dashboard');
createApp(UserDash).mount('#user-dashboard');
createApp(AdminManageUsers).mount('#admin-manage-users');
createApp(UserUpdateInfo).mount('#user-update-info');
createApp(UserLogin).mount('#user-login');
createApp(SupportCenter).mount('#support-center');
createApp(PrivacyPolicy).mount('#privacy-policy');
createApp(ServiceTerms).mount('#terms-of-service');
createApp(ContactUs).mount('#contact-us');
createApp(Footer).mount('#footer');
