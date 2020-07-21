import { HTTP } from './common'

export const Template = {
  show () {
    return HTTP.get('/pass').then(response => {
      return response.data
    })
  }
}
