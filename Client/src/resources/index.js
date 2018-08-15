import { PLATFORM } from "aurelia-framework";

export function configure(config) {
  config.globalResources([
    PLATFORM.moduleName('./elements/nav-bar')
  ]);
}
