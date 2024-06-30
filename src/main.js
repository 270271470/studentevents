import { createApp } from 'vue';  // Import createApp function from Vue

// Import custom Vue components
import NavMainHero from './nav_main_hero.vue';
import NavOnly from './nav_only.vue';
import RegistrationForm from './registration_form.vue';
import AdminDash from './admin_dashboard.vue';
import UserDash from './user_dashboard.vue';
import AdminManageUsers from './admin_manage_users.vue';
import AdminManageEvents from './admin_manage_events.vue';
import AdminPendingBookings from './admin_pending_bookings.vue';
import AdminViewAllBookings from './admin_view_all_bookings.vue';
import UserUpdateInfo from './user_update_info.vue';
import UserLogin from './login.vue';
import UserManageBooking from './user_manage_booking.vue';
import SupportCenter from './support-center.vue';
import PrivacyPolicy from './privacy-policy.vue';
import ServiceTerms from './terms-of-service.vue';
import ContactUs from './contact-us.vue';
import EventsAll from './events-all.vue';
import EventsAdventure from './events-adventure.vue';
import EventsClubs from './events-clubs.vue';
import EventsOutdoor from './events-outdoor.vue';
import EventsWorkshops from './events-workshops.vue';
import Footer from './footer.vue';

// Create Vue app instance with the component and mount it to the element with matching ID
createApp(NavMainHero).mount('#nav_main_hero');
createApp(NavOnly).mount('#nav_only');
createApp(RegistrationForm).mount('#user_registration');
createApp(AdminDash).mount('#admin-dashboard');
createApp(UserDash).mount('#user-dashboard');
createApp(AdminManageUsers).mount('#admin-manage-users');
createApp(AdminManageEvents).mount('#admin-manage-events');
createApp(AdminPendingBookings).mount('#admin-pending-bookings');
createApp(AdminViewAllBookings).mount('#admin-view-all-bookings');
createApp(UserUpdateInfo).mount('#user-update-info');
createApp(UserManageBooking).mount('#user-manage-booking');
createApp(UserLogin).mount('#user-login');
createApp(SupportCenter).mount('#support-center');
createApp(PrivacyPolicy).mount('#privacy-policy');
createApp(ServiceTerms).mount('#terms-of-service');
createApp(ContactUs).mount('#contact-us');
createApp(EventsAll).mount('#events-all');
createApp(EventsAdventure).mount('#events-adventure');
createApp(EventsClubs).mount('#events-clubs');
createApp(EventsOutdoor).mount('#events-outdoor');
createApp(EventsWorkshops).mount('#events-workshops');
createApp(Footer).mount('#footer');