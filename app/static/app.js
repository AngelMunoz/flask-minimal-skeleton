import ROUTES from './routes.js';

export class App {
  constructor() {
    this.message = 'Hello World';
    this.router = null;
  }

  configureRouter(config, router) {
    this.router = router;
    config.title = 'Flask-Aurelia';
    config.map(ROUTES);
  }
}
