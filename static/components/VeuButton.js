// static/components/VeuButton.js

export default {
  name: 'veu-button',
  data: () => ({}),
  props: {
    animate: {
      default: 'none',
      type: String,
    },
    rounded: {
      default: false,
      type: Boolean
    },
    size: {
      default: 'md',
      type: String
    },
    text: {
      default: 'Submit',
      type: String
    },
    variant: {
      default: 'none',
      type: String
    }
  },
  template: `
    <button
      :class="{
        'veu-button': true,
        'rounded':   rounded, 
        'primary':   variant == 'primary',
        'secondary': variant == 'secondary',
        'info':      variant == 'info',
        'danger':    variant == 'danger',
        'warning':   variant == 'warning',
        'success':   variant == 'success',
        'anim-down': animate == 'down',
        'anim-up':   animate == 'up',
        'size-sm':   size    == 'sm',
        'size-md':   size    == 'md',
        'size-lg':   size    == 'lg'
      }">
      {{ text }}
    </button>
  `
}