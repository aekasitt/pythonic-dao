// static/components/VeuPane.js

export default {
  name: 'veu-pane',
  props: {
    theme: {
      default: 'grey',
      type: String
    }
  },
  template: `
    <div :class="{
      'veu-pane': true,
      'cloud': theme == 'cloud',
      'dark':  theme == 'dark',
      'grey':  theme == 'grey',
      'sepia': theme == 'sepia',
      }">
      <slot></slot>
    </div>
  `
};