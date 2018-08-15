import { inject } from "aurelia-framework";
import { Router } from "aurelia-router";

@inject(Router)
export class Login {
  constructor(router) {
    this.router = router;
    this.payload = {
      email: '',
      password: ''
    }
  }

  /**
   * Check aurelia-authentication for a more complete plugin on auth
   */
  async login() {
    let response;
    try {
      response = await fetch('/auth/login', {
        body: JSON.stringify(this.payload),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => {
        if (!res.ok) {
          throw { status: res.status, response: res.json() };
        }
        return res.json()
      })
      sessionStorage.setItem('access_token', response.access_token);
      sessionStorage.setItem('authenticated', true);
    } catch (error) {
      sessionStorage.removeItem('access_token');
      sessionStorage.removeItem('authenticated');
      const res = await error.response;
      return console.warn({ status: error.status, res });
    }
    return this.router.navigateToRoute('user')
  }
}