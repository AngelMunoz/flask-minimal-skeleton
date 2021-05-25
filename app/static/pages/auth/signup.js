
export class Signup {
  static get $resource() {
    return {
      inject: [au.Router]
    };
  }
  constructor(router) {
    this.router = router;
    this.payload = {
      name: '',
      last_name: '',
      password: '',
      email: '',
    };

    this.repeatPassword = '';
  }
  /**
   * Check aurelia-authentication For a more Complete Auth Solution
   */
  async signup() {
    let response;
    if (this.payload.password !== this.repeatPassword) {
      return alert('The Passwords Must Match!');
    }
    try {
      response = fetch('/auth/signup', {
        body: JSON.stringify(this.payload),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => {
        if (!res.ok) {
          throw { status: res.status, response: res.json() };
        }
        return res.json();
      });
    } catch (error) {
      const res = await error.response;
      return console.warn({ status: error.status, res });
    }
    return this.router.navigateToRoute('login');
  }

}