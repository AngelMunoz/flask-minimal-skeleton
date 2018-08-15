import { bindable, computedFrom } from "aurelia-framework";

export class NavBar {

  @bindable
  router;

  isActive = false;

  toggleActive() {
    this.isActive = !this.isActive;
  }

  logout() {
    sessionStorage.removeItem('access_token')
    sessionStorage.removeItem('authenticated')
  }
}