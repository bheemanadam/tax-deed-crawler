---
name: Abyssal Precision
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1c1b1d'
  surface-container: '#201f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e5e1e4'
  on-surface-variant: '#bbcabf'
  inverse-surface: '#e5e1e4'
  inverse-on-surface: '#313032'
  outline: '#86948a'
  outline-variant: '#3c4a42'
  surface-tint: '#4edea3'
  primary: '#4edea3'
  on-primary: '#003824'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#006c49'
  secondary: '#bdc7db'
  on-secondary: '#273140'
  secondary-container: '#404a5a'
  on-secondary-container: '#afb9cc'
  tertiary: '#ffb3ad'
  on-tertiary: '#68000a'
  tertiary-container: '#ff7a73'
  on-tertiary-container: '#79000e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#d9e3f7'
  secondary-fixed-dim: '#bdc7db'
  on-secondary-fixed: '#121c2a'
  on-secondary-fixed-variant: '#3d4757'
  tertiary-fixed: '#ffdad7'
  tertiary-fixed-dim: '#ffb3ad'
  on-tertiary-fixed: '#410004'
  on-tertiary-fixed-variant: '#930013'
  background: '#131315'
  on-background: '#e5e1e4'
  surface-variant: '#353437'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1'
  data-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter-desktop: 24px
  gutter-mobile: 16px
  margin-desktop: 64px
  margin-mobile: 16px
  container-max: 1440px
---

## Brand & Style
The design system is engineered for a high-stakes, data-intensive real estate auction environment. It prioritizes technical authority and rapid information processing through an "Abyssal" aesthetic—leveraging pure black depths to make critical data points and live auction statuses emerge with extreme clarity.

The style is a hybrid of **Minimalism** and **Glassmorphism**, emphasizing high-density layouts that remain legible through strict grid alignment and sharp contrast. It evokes a sense of "digital luxury"—the feeling of a high-end financial terminal tailored specifically for the Texas property market. The emotional response should be one of professional confidence, urgency, and absolute precision.

## Colors
The palette is anchored in a pure black (`#000000`) foundation to eliminate visual noise and maximize OLED contrast. 

- **Primary Emerald Mint:** Reserved for "Live," "Active," and "Winning" states. It is the heartbeat of the portal.
- **Secondary Steel Gray:** Used for structural elements like borders, icons, and inactive states to maintain a sophisticated, non-distracting hierarchy.
- **Coral Crimson:** Exclusively for alerts, outbid notifications, and closing-soon timers to trigger immediate user attention.
- **Neutral Deep Charcoal:** Defines the "surface" layer, creating subtle separation between the infinite background and interactive card spaces.

## Typography
This design system utilizes a dual-font strategy to balance readability with technical precision.

**Inter** handles all core UI elements, headlines, and descriptive text, providing a neutral, professional tone that stays out of the way of the content. 

**JetBrains Mono** is utilized for all "Data Metrics"—including bid amounts, lot numbers, square footage, and timestamps. The monospaced nature ensures that fluctuating numbers do not cause layout jitters during live updates and reinforces the portal's data-centric personality.

## Layout & Spacing
The layout follows a strict **Fixed Grid** model on desktop (12 columns) and a **Fluid Grid** on mobile (4 columns). 

To achieve a "high-density" feel, the spacing rhythm is built on a 4px base unit. 
- **Tight grouping:** Use 8px or 12px for related items within a card.
- **Sectional breathing:** Use 48px to 64px for vertical separation between major dashboard sections.
- **Mobile-first approach:** Elements are designed to span full-width on mobile to maximize the display of property photography and bidding controls.

## Elevation & Depth
Depth in the design system is achieved through **Tonal Layers** and **Low-contrast Outlines** rather than traditional shadows.

1.  **Level 0 (Background):** Pure `#000000`.
2.  **Level 1 (Cards/Containers):** Deep Charcoal `#0A0A0C`.
3.  **Level 2 (Modals/Popovers):** Slightly lighter charcoal with a subtle 1px border of Steel Gray (`#374151`).

**Glassmorphism** is applied specifically to "Sticky" elements (Top Navigation, Mobile Bid Bar). These use a background blur (12px) with 80% opacity on the Deep Charcoal surface to maintain context of the scroll position without sacrificing legibility.

## Shapes
The shape language is "Soft-Precision." By using a **0.25rem (4px)** base radius, the UI avoids the coldness of sharp corners while maintaining a structured, engineered appearance.

- **Standard Elements:** 4px radius (Buttons, Input fields, Small cards).
- **Large Containers:** 8px radius (Property image galleries, Main auction cards).
- **Status Pills:** Fully rounded (pill-shaped) to distinguish them from interactive buttons.

## Components

- **Buttons:** Primary buttons use Emerald Mint with black text for maximum "Call to Action" punch. Secondary buttons are outlined in Steel Gray.
- **Auction Cards:** Feature a Level 1 Charcoal surface, a 1px Steel Gray border, and top-aligned JetBrains Mono labels for Lot Numbers.
- **Input Fields:** Flat black background with a 1px Steel Gray border that illuminates to Emerald Mint on focus.
- **Live Status Indicators:** A pulsing Emerald Mint dot paired with "LIVE" in `label-caps`.
- **Data Tables:** High-density rows with 1px horizontal dividers. Alternating "Zebra" stripes are not used; instead, hover states utilize a subtle highlight to maintain the abyssal look.
- **Sticky Bid Bar (Mobile):** A glassmorphic bar at the bottom of the viewport containing a "Quick Bid" button and the current high bid in `data-lg`.