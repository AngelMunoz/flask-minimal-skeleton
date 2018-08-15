import ROUTES from './routes';
import './app.scss';

export class App {
  constructor() {
    this.message = 'Hello World'
    this.router = null;
  }

  configureRouter(config, router) {
    this.router = router;
    config.title = 'Flask-Aurelia';
    config.map(ROUTES);
  }
}
