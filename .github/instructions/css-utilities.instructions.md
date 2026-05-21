---
description: CSS utility classes and styling practices for this Python/Jinja2 project.
---

# CSS Utility Guide

## Overview
This project uses custom CSS utility classes defined in [app/static/css/app.css](app/static/css/app.css).

When styling templates:
- Prefer existing utility classes over adding new component-specific CSS.
- Compose small utilities in templates for layout, spacing, and typography.
- Keep styling changes consistent with the existing utility naming style.

## Available Utilities

### Layout
```css
.flex, .flex-col, .flex-1
.grid, .grid-cols-5
.items-center, .justify-center, .justify-between
.h-full, .min-h-full, .w-full, .w-16
.max-w-xs, .max-w-sm, .max-w-md
.aspect-square
```

### Spacing
```css
/* Padding */
.p-1, .p-3, .p-4, .p-6
.px-3, .px-4, .px-6, .px-8
.py-1\.5, .py-2, .py-3, .py-4

/* Margin */
.mb-2, .mb-3, .mb-4, .mb-6, .mb-8, .mx-auto

/* Gap and stack */
.gap-1
.space-y-2
```

### Colors
```css
/* Backgrounds */
.bg-white, .bg-gray-50, .bg-gray-100
.bg-amber-100, .bg-amber-200
.bg-accent, .bg-marked
.bg-black\/50

/* Text */
.text-white
.text-gray-500, .text-gray-600, .text-gray-700, .text-gray-800, .text-gray-900
.text-green-600, .text-green-800
.text-amber-500, .text-amber-800, .text-amber-900
```

### Typography
```css
.text-xs, .text-sm, .text-lg, .text-3xl, .text-4xl, .text-5xl
.font-semibold, .font-bold
.text-left, .text-center
.leading-tight
.wrap-break-word
.hyphens-auto
```

### Borders, Radius, and Shadows
```css
.border, .border-b
.border-gray-200, .border-gray-300
.border-amber-400, .border-marked-border
.rounded, .rounded-lg, .rounded-xl
.shadow-sm, .shadow-xl
```

### Positioning and Layering
```css
.fixed, .absolute, .relative
.inset-0
.top-0\.5, .right-0\.5
.z-50
```

### Interaction and Motion
```css
.select-none
.transition-all, .transition-colors, .duration-150
.active\:bg-gray-100, .active\:bg-accent-light
.animate-[bounce_0\.5s_ease-out]
```

### Special Size Utility
```css
.min-h-[60px]
```

## Styling Rules
- Reuse utilities in [app/static/css/app.css](app/static/css/app.css) before introducing any new class.
- Do not add inline styles in templates.
- Do not add external CSS frameworks.
- If a new utility is needed, follow existing naming style and keep it generic/reusable.
- Keep visual behavior predictable across mobile and desktop.

## Template Usage Pattern
Prefer composable utilities in Jinja templates:

```html
<div class="max-w-md mx-auto p-4 bg-white rounded-xl shadow-sm">
  <h2 class="text-lg font-bold text-gray-900 mb-2">Title</h2>
  <p class="text-sm text-gray-700 leading-tight wrap-break-word hyphens-auto">
    Body text
  </p>
  <button class="mt-3 px-4 py-2 bg-accent text-white rounded transition-colors duration-150">
    Action
  </button>
</div>
```

## Where To Apply
This guide is most relevant when editing:
- [app/templates/base.html](app/templates/base.html)
- [app/templates/home.html](app/templates/home.html)
- [app/templates/components/bingo_board.html](app/templates/components/bingo_board.html)
- [app/templates/components/bingo_modal.html](app/templates/components/bingo_modal.html)
- [app/templates/components/game_screen.html](app/templates/components/game_screen.html)
- [app/templates/components/start_screen.html](app/templates/components/start_screen.html)
- [app/static/css/app.css](app/static/css/app.css)
