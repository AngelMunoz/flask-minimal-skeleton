
export class NavBar {

  router;

  isActive = false;

  toggleActive() {
    this.isActive = !this.isActive;
  }

  logout() {
    sessionStorage.removeItem('access_token');
    sessionStorage.removeItem('authenticated');
  }

  static get $resource() {
    return {
      bindables: ['router']
    };
  }
}