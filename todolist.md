# Comediq Webapp Checklist

## Issues
- [ ] Tiles too bulky: 13 data points are overwhelming. Show only 2-3 main pieces of info in the subheader (e.g., day, neighborhood, start time). Move the rest to the main description/details.
- [ ] Map not yet functional
- [ ] List and Map buttons too close: List button should be atop both detailed and glance views (left section). Map button should be on the right and show pinpointed mics.
- [ ] Comediq logo not on page
- [ ] Public like/dislike backend not functional
- [ ] Private review backend not functional: Should allow 5 planned jokes, 5 performed jokes, 1-10 slider for each, and notes for each joke.

## Fixed/Closed
- [x] List a Mic modal only opens on "+ List a Mic" button
- [x] Removed duplicate/overwhelming fields from List a Mic form
- [x] Only mic name shown as title in detailed view
- [x] "None at None" and duplicate subheader removed
- [x] Modal hidden by default, not shown on tab/view changes

## Next Steps
- [ ] Refactor detailed and glance views to show only key info in subheader, rest in details
- [ ] Implement map functionality (Mapbox or Google Maps)
- [ ] Redesign List/Map button layout for clarity
- [ ] Add Comediq logo to the page
- [ ] Implement backend for public like/dislike (one per user per mic, show tally)
- [ ] Implement backend for private reviews (with joke planning, performance, sliders, and notes)
- [ ] (Optional) Pre-fill private review form with user's previous review if it exists

## Later Next Steps (Lower Priority)
- Home page with personalized dashboard
- Full-featured open mic finder with advanced filters and analytics
- Mic scheduler and Google Calendar integration
- Community tab with comedy circles, group chat, and mic exchange
- Comedy metrics dashboard and analytics
- Locked tab for user voting on next features
- Recordings, transcriptions, and content portfolio features
- Gamification and progress tracker 