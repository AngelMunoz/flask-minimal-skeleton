import { PLATFORM } from 'aurelia-framework'

export default [
  { route: ['', 'home'], name: 'home', moduleId: PLATFORM.moduleName('./pages/home'), nav: false, title: 'Home' },
  { route: 'auth/login', name: 'login', moduleId: PLATFORM.moduleName('./pages/auth/login'), nav: true, title: 'Log In' },
  { route: 'auth/signup', name: 'signup', moduleId: PLATFORM.moduleName('./pages/auth/signup'), nav: true, title: 'Sign Up' },
  { route: 'protected/user', name: 'user', moduleId: PLATFORM.moduleName('./pages/protected/user'), nav: false, title: 'User Profile' },
];