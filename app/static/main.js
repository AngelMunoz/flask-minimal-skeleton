const aurelia = new au.Aurelia();
aurelia
  .use
  .standardConfiguration()
  .developmentLogging();
aurelia
  .start()
  .then(() => aurelia.setRoot('/static/app.js', document.body))
  .catch(ex => {
    document.body.textContent = `Bootstrap error: ${ex}`;
  });