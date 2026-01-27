import {defineStore} from "pinia";
import {ref} from "vue";

export const useUserStore = defineStore('user', () => {
    const id = ref(1)
    const username = ref('majin')
    const photo = ref('http://127.0.0.1:8000/media/user/photos/default.png')
    const profile = ref('111')
    const accessToken = ref('111')

    function isLogin() {
        return !!accessToken.value
    }

    function setAccessToken(token){
        accessToken.value = token
    }

    function setUsserInfo(data){
        id.value = data.user_id
        username.value = data.username
        photo.value = data.photo
        profile.value = data.profile
    }

    function logout(){
        id.value = 0
        usename.value = ''
        photo.value = ''
        accessToken.value = ''
    }

    return {
        id,
        username,
        photo,
        profile,
        accessToken,
        isLogin,
        setAccessToken,
        setUsserInfo,
        logout,
    }

})