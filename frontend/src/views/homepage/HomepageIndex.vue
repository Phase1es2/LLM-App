<script setup>
import {nextTick, onBeforeUnmount, onMounted, ref, useTemplateRef, watch} from "vue";
import {useRoute} from "vue-router";
import api from "@/js/http/api.js";
import Character from "@/components/character/Character.vue";

const userProfile = ref(null)
const characters = ref([])
const isLoading = ref(false)
const hasCharacter = ref(true)
const sentinelRef = useTemplateRef('sentinel-ref')
const route = useRoute()


function checkSentinelVisible() {  // 判断哨兵是否能被看到
  if (!sentinelRef.value) return false

  const rect = sentinelRef.value.getBoundingClientRect()
  return rect.top < window.innerHeight && rect.bottom > 0
}


async function loadMore() {
  if (isLoading.value || !hasCharacter.value) return
  isLoading.value = true
  let newCharacters = []
  try {
    // get must be in the params
    const res = await api.get('/api/homepage/index/', {
      params: {
        items_count: characters.value.length,
        search_query: route.query.q || '',
      }
    })
    const data = res.data
    if (data.result === 'success') {
      newCharacters = data.characters  // 這裡需要match BE
    }
  } catch (err) {

  } finally {
    isLoading.value = false
    if (newCharacters.length === 0) {
      hasCharacter.value = false
    } else {
      characters.value.push(...newCharacters)

      await nextTick()

      if (checkSentinelVisible()) {
        await loadMore()
      }
    }

  }
}

let observer = null

onMounted( async () => {
  await loadMore()

  observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            loadMore()
          }
        })
      },
      {root: null, rootMargin: '2px', threshold: 0}
  )
  observer.observe(sentinelRef.value)
})

function removeCharacter(characterId) {
  characters.value = characters.value.filter(c => c.id !== characterId)
}

function reset() {
  characters.value = []
  isLoading.value = false
  hasCharacter.value = true
  loadMore()
}

watch(() => route.query.q, newQ => {
  reset()
})

onBeforeUnmount( () => {
  observer?.disconnect()
})
</script>

<template>
  <div class="flex flex-col items-center mb-12">
    <div class="grid grid-cols-[repeat(auto-fill,minmax(240px,1fr))] gap-9 mt-12 justify-items-center w-full px-9">
      <Character
        v-for="character in characters"
        :key="character.id"
        :character="character"
      />
    </div>
    <div ref="sentinel-ref" class="h-2 mt-8 w-100"></div>
    <div v-if="isLoading" class="text-gray-500 mt-4">Loading...</div>
    <div v-else-if="!hasCharacter" class="text-gray-500 mt-4">There is not more character</div>
  </div>
</template>

<style scoped>

</style>