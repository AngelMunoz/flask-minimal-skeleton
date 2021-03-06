export class User {
  static get $resource() {
    return {
      inject: [au.Router]
    };
  }


  constructor(router) {
    this.router = router;
  }

  /**
   * Check aurelia-authentication for a more complete plugin on auth
   * @param {*} params 
   * @param {*} routeConfig 
   * @param {*} navigationInstruction 
   */
  activate(params, routeConfig, navigationInstruction) {
    // this is not the safest way to check if the user is logged in
    if (!sessionStorage.getItem('access_token')) {
      return this.router.navigateToRoute('login');
    }
    return true;
  }
}