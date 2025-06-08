<script setup>
import { ref } from 'vue'

// Reactive form data.
const formData = ref(
    {
        username : '',
        password : ''
    }
)

// Form submission handler.
const handleSubmit = async () => {
    try {
        // Form submission handler
        // 1. Make API call to the backend.
        // 2. Handle authentication.
        // 3. Store tokens/session data.
        const response = await fetch('/api/login',
            {
                method : 'POST',
                headers : {
                    'Content-Type' : 'application/json'
                },
                body: JSON.stringify(formData.value)
            }
        )

        const data = await response.json()
        // Handle response...
    }
    catch (error) {
        console.error('Login failed:', error)
    }
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <input
        v-model="formData.username"
        type="text"
        required
        placeholder="Username"
      />
    </div>
    <div>
      <input
        v-model="formData.password"
        type="password"
        required
        placeholder="Password"
      />
    </div>
    <button type="submit">Login</button>
  </form>
</template>
