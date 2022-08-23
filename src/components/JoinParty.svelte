<script>
  // import "./timeline.css";
  let player1;
  let player1State;
  import Youtube from "../lib/Youtube.svelte";
  import { currentTimeLine } from "../store/store";
  let playStatus = true;
  let currentTime = 0;

  currentTimeLine.subscribe((value) => {
    currentTime = value;
  });
</script>

<hr />

<Youtube
  videoId="M7lc1UVf-VE"
  on:PlayerStateChangeString={({ detail }) => (player1State = detail)}
  bind:this={player1}
/><br />
<!-- <button on:click={() => player1.play()}>. </button> -->
<div class="video-controller">
  {#if playStatus}
    <button
      on:click={() => {
        player1.play();
        playStatus = false;
      }}
      class="button play"
    >
      ▶️</button
    >
  {:else}
    <button
      on:click={() => {
        player1.pause();
        playStatus = true;
      }}
      class="button pause">⏸</button
    >
  {/if}
  <input
    type="range"
    value={currentTime}
    on:change={(e) => player1.seekTo(e.target.value / 100, true)}
  />
</div>

<!-- Player 1 State: {player1State} -->
<style>
  input[type="range"] {
    /* padding: 0 10px; */
    width: 80%;
  }
</style>
