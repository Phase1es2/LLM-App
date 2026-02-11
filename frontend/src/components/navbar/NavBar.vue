<script setup>

import MenuIcon from "@/components/navbar/icons/MenuIcon.vue";
import HomepageIcon from "@/components/navbar/icons/HomepageIcon.vue";
import CreateIcon from "@/components/navbar/icons/CreateIcon.vue";
import FriendIcon from "@/components/navbar/icons/FriendIcon.vue";
import SearchIcon from "@/components/navbar/icons/SearchIcon.vue";
import {useUserStore} from "@/stores/user.js";
import UserMenu from "@/components/navbar/UserMenu.vue";
import {ref, watch} from "vue";
import {useRoute, useRouter} from "vue-router";

const user = useUserStore()
const searchQuery = ref('')
const router = useRouter()
const route = useRoute()

watch(() => route.query.q, newQ => {
  searchQuery.value = newQ || ''
})

function handleSearch() {
  router.push({
    name: 'homepage-index',
    query: {
      q: searchQuery.value.trim(),
    }
  })
}

</script>

<template>
<div class="drawer lg:drawer-open">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <!-- Navbar -->
    <nav class="navbar w-full bg-base-100 shadow-sm">
      <div class="navbar-start">
        <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
        <MenuIcon />
        </label>
        <div class="px-2 font-bold text-xl">AIFriends</div>
      </div>
      <div class="navbar-center w-4/5 max-w-180 flex justify-center">
        <form @submit.prevent="handleSearch" class="join w-4/5 flex justify-center">
          <input v-model="searchQuery" class="input join-item rounded-l-full" placeholder="Search What You Like" />
          <button class="btn join-item rounded-r-full gap-0">
            <SearchIcon />
              Search
          </button>
        </form>
      </div>
      <div class="navbar-end">
        <RouterLink v-if="user.isLogin()" :to="{name: 'create-index'}" active-class="menu-btn" class="btn btn-ghost text-base mr-6">
          <CreateIcon />
            Create
        </RouterLink>
        <RouterLink v-if="user.hasPulledUserInfo && !user.isLogin()" :to="{name: 'login-index'}" active-class="btn-active" class="btn btn-ghost text-lg">
          Login
        </RouterLink>
        <UserMenu v-else-if="user.isLogin()" />
      </div>
    </nav>
    <slot></slot>
  </div>

  <div class="drawer-side is-drawer-close:overflow-visible">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-16 is-drawer-open:w-54">
      <ul class="menu w-full grow">
        <li>
          <RouterLink :to="{name: 'homepage-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3" data-tip="Homepage">
            <HomepageIcon />
            <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap">Homepage</span>
          </RouterLink>
        </li>
        <li>
          <RouterLink :to="{name: 'friend-index'}" active-class="menu-focus" class="is-drawer-close:tooltip-right py-3" data-tip="Friend">
            <FriendIcon />
            <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap">Friend</span>
          </RouterLink>
        </li>
        <li>
          <RouterLink :to="{name: 'create-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3" data-tip="Create">
            <CreateIcon />
            <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap">Create</span>
          </RouterLink>
        </li>
      </ul>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>