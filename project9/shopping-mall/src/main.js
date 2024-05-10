import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import  PiniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use([PiniaPluginPersistedstate])

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(pinia)

app.mount('#app')
