
export default [
  { route: ['', 'home'], name: 'home', moduleId: './pages/home.js', nav: false, title: 'Home' },
  { route: 'auth/login', name: 'login', moduleId: './pages/auth/login.js', nav: true, title: 'Log In' },
  { route: 'auth/signup', name: 'signup', moduleId: './pages/auth/signup.js', nav: true, title: 'Sign Up' },
  { route: 'protected/user', name: 'user', moduleId: './pages/protected/user.js', nav: false, title: 'User Profile' },
];