// static/components/VeuInput.js

export default {
  name: 'veu-input',
  props: {
    val: {
      default: 0,
      type: String
    },
    placeholder: {
      default: '',
      type: String
    },
    size: {
      default: 'md',
      type: String
    },
    width: {
      default: 'fit-content',
      type: String
    }
  },
  template: `
    <input :class="{
      'veu-input':      true,
      'fill-available': width == 'fill-available',
      'fit-content':    width == 'fit-content',  
      'size-sm':        size  == 'sm',
      'size-md':        size  == 'md',
      'size-lg':        size  == 'lg'
    }"
    :placeholder='placeholder'
    :value='val'
    @input="$emit('update:val', val)">
  `
};